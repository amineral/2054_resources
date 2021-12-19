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

class AddComputerForm(forms.Form):
    CHOICES = [
        ("PC", "PC"),
        ("Laptop", "Laptop"),
    ]
    CHOICES_DP = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]
    comp_type = forms.ChoiceField(choices=CHOICES)
    # brand = forms.CharField(max_length=20)
    # serial_number = forms.CharField(max_length=20)
    owner = forms.CharField(max_length=30)
    # status = forms.CharField(max_length=10)
    # dp = forms.ChoiceField(choices=CHOICES_DP)

class AuthForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = CharField(widget=forms.PasswordInput())

