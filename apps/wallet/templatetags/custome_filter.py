from django import template

register = template.Library()


@register.filter(name='cuter')
def cut(value, args):
    arg1, *args = args.split(':')
    arg2 = args[0] if args else ""
    return value.replace(arg1, arg2)


@register.filter(name='to_som')
def to_som(value):
    return f"{value} сом"