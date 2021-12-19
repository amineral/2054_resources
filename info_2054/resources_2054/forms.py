from django import forms
from django.forms.fields import CharField

class ComputerFilter(forms.Form):
    CHOICES = [
        ('PC', 'PC'),
        ('Laptop', 'Laptop'),
        ('all', 'all')
    ]
    type = forms.ChoiceField(choices=CHOICES, required=False)
    owner = forms.CharField(max_length=100, required=False)

class AddComputerFrom(forms.Form):
    CHOICES = [
        ("PC", "PC"),
        ("Laptop", "Laptop"),
    ]
    comp_type = forms.ChoiceField(choices=CHOICES, required=False)
    brand = forms.CharField(max_length=20, required=True)
    serial_number = forms.CharField(max_length=20, required=False)
    owner = forms.CharField(max_length=30, required=True)
    status = forms.CharField(max_length=10, required=True)
    #dp = forms.ForeignKey('Department', on_delete=models.CASCADE)

class AuthForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = CharField(widget=forms.PasswordInput())

