from django import template # 追記 必須
register = template.Library() # 追記 必須

@register.filter
def split(string, sep):
    result = string.rstrip(sep).split(sep)
    return result