from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
 
 
class RegisterForm(UserCreationForm):
 
    first_name = forms.CharField(label="姓", required=True)
    last_name = forms.CharField(label="名", required=True)
 
    class Meta:
        model = User
        fields = (
            "username", "password1", "password2",
            "first_name", "last_name",
        )
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'メールアドレス'
 
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = '姓'
 
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = '名'
 
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
 
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワード（確認）'
 
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            validate_email(username)
        except ValidationError:
            raise ValidationError("正しいメールアドレスを指定してください。")
 
        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        else:
            raise ValidationError("既に存在するメールアドレスです。")
 
 
class UpdateForm(forms.ModelForm):
 
    first_name = forms.CharField(label="姓", required=True)
 
    class Meta:
        model = User
        fields = (
             "first_name", 
        )
 
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
 
 
 
class LoginForm(AuthenticationForm):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'メールアドレス'
 
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'パスワード'
 
 
class ForgetPasswordForm(PasswordResetForm):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'
 
 
class ChangePasswordForm(PasswordChangeForm):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
 
 
class PasswordConfirmForm(SetPasswordForm):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = '新パスワード'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = '新パスワード（確認）'
