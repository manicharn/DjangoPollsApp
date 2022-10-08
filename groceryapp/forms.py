from cProfile import label
from dataclasses import fields
from email.policy import default
from django import forms

class MyForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    item = forms.CharField(max_length=20)
    price=forms.FloatField()
    quantity=forms.IntegerField()
    

