from django import template

register = template.Library()

@register.filter
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

register = template.Library()

@register.filter
def zip_lists(list1, list2):
    return zip(list1, list2)