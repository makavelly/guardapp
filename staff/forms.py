from django import forms
#from django.forms import inlineformset_factory
from .models import Employee
from .models import Chief

class ModelFormWithCustomErrorMessages(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        error_messages = {'date_of_birth': {'invalid': 'Custom invalid error message'}}
        
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
#EmployeeFormSet = inlineformset_factory(Chief, Employee, form=EmployeeForm, extra=2)
#EmployeeFormSet = inlineformset_factory(Chief, Employee, fields='__all__', extra=1)