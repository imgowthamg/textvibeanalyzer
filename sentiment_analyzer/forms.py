# sentiment_analyzer/forms.py

from django import forms

class UserInputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    language = forms.ChoiceField(choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish')])  # Add more languages as needed
