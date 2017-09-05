from django import forms

from .models import Record

class PostForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('time',)
