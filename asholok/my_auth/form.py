from django import forms
from captcha.fields import CaptchaField
from my_auth.models import User

class CaptchaModelForm(forms.ModelForm):
    # captcha = CaptchaField()
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'user_mail', 
            'username', 
            'password', 
            'confirm_password', 
            'images']
        widgets = {
            'password': forms.PasswordInput(),
        }
