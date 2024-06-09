from django import forms

from.models import Exercise


class ExerciseForm(forms.Form):
    description=forms.CharField(widget=forms.Textarea)
    homework_file=forms.CharField(widget=forms.FileInput)
    