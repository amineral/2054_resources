from django import forms

class ComputerFilter(forms.Form):
    CHOICES = [
        ('PC', 'PC'),
        ('Laptop', 'Laptop'),
    ]
    type = forms.ChoiceField(choices=CHOICES, required=False)
    owner = forms.CharField(max_length=100, required=False)

