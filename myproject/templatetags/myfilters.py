from django import template # 追記 必須
register = template.Library() # 追記 必須

@register.filter
def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.split(sep)