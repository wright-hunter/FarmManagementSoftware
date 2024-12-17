from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name

class YearlyFieldData(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='yearly_data')
    year = models.IntegerField()
    acres = models.FloatField(null=True, blank=True)
    seed_cost = models.FloatField(null=True, blank=True)
    fertilizer_cost = models.FloatField(null=True, blank=True)
    chemical_cost = models.FloatField(null=True, blank=True)
    crop_insurance = models.FloatField(null=True, blank=True)
    yield_amount = models.FloatField(null=True, blank=True)  # In bushels
    crop = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ['field', 'year']
        ordering = ['-year']

    def __str__(self):
        return f"{self.field.name} - {self.year}"

    def total_cost(self):
        costs = [
            self.seed_cost or 0,
            self.fertilizer_cost or 0,
            self.chemical_cost or 0,
            self.crop_insurance or 0
        ]
        return sum(costs)
    
    def yield_per_dollar(self):
        total = self.total_cost()
        if total and self.yield_amount:
            return self.yield_amount / total
        return