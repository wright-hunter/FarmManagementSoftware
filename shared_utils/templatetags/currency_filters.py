from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    if value is None:
        return '-'
    return f'${value:,.2f}'