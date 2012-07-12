from django import forms

class signup_form(forms.Form):
    email_address = forms.EmailField(required=True)
    password      = forms.CharField(widget=forms.PasswordInput(), required=True)

class login_form(forms.Form):
    email_address = forms.EmailField(required=True)
    password      = forms.CharField(widget=forms.PasswordInput(), required=True)
