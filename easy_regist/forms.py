from django import forms
from django.contrib.auth.models import User
 
class UpdateForm(forms.ModelForm):
 
    first_name = forms.CharField(label="名前", required=True)
 
    class Meta:
        model = User
        fields = (
             "first_name", 
        )
 
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
 
