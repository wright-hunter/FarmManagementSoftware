from django.db import models

class Equipment(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    type = models.CharField(max_length=100)  # Remove choices to allow any type
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    class Meta:
        ordering = ['-year']

class EquipmentExpense(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='expenses')
    date = models.DateField()
    expense_type = models.CharField(max_length=100, choices=[
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
        ('fuel', 'Fuel'),
        ('insurance', 'Insurance'),
        ('other', 'Other')
    ])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']