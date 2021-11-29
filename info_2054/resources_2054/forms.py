from django import forms

class CheckBoxFilter(forms.Form):
    pc = forms.BooleanField(required=False)
    laptop = forms.BooleanField(required=False)
    
