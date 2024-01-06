# sentiment_analyzer/forms.py
from django import forms

class UserInputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
