from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(required=True,
                    widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control', }))
    password = forms.CharField(required=True,
                    widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', }))
    email = forms.EmailField(
                    widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', }))
    username = forms.CharField(
                    widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', }))

    class Meta:
        model = User
        fields = ('email',
                  'password',
                  'username'
                  )

    def init(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class LoginForm(forms.Form):
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control', }))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', }))