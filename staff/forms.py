from django import forms
from .models import Employee

class ModelFormWithCustomErrorMessages(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        error_messages = {'date_of_birth': {'invalid': 'Custom invalid error message'}}