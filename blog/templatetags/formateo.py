from django import template

register = template.Library()

@register.filter
def precio_formato(value):
    try:
        value = float(value)
        return f"{value:,.0f}".replace(",", ".")
    except:
        return value
