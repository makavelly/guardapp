from django import template
register = template.Library()

@register.simple_tag
def get_model_field_name(instance, field_name):
    """
    Returns verbose field name by a field_name of a model instance.
    """
    return instance._meta.get_field(field_name).verbose_name.title()
	
@register.simple_tag
def get_all_model_field_names(instance):
    """
    Returns all fields of a model instance.
    """
    return instance._meta.get_fields()
	
@register.simple_tag
def get_model_field_value(instance, field_name):
    """
    Returns field value by a field_name of a model instance.
    """
    return getattr(instance, field_name)
    
@register.filter
def addstr(arg1, arg2):
    """Returns concatenated args"""
    return str(arg1) + str(arg2)