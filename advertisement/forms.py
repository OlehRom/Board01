from django import forms
from .models import Task
from django.forms import ModelForm, TextInput


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'text',)


class SearchForm(forms.Form):
    query = forms.CharField()