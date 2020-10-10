from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from fresher.models import Resume


# class RegistrationForm(ModelForm):
#     class Meta:
#         model = Registration
#         fields = "__all__"
#         widgets = {
#             'First_Name': forms.TextInput(attrs={'class': 'form-control'}),
#             'Last_Name': forms.TextInput(attrs={'class': 'form-control'}),
#             'Email': forms.TextInput(attrs={'class': 'form-control'}),
#             'Username': forms.TextInput(attrs={'class': 'form-control'}),
#             'Password': forms.PasswordInput(),
#             'Confirm_Password': forms.PasswordInput(),
#         }


# class LoginForm(forms.Form):
#     Username = forms.CharField(max_length=120)
#     Password = forms.CharField(widget=forms.PasswordInput())


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"
        widgets = {
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'Password': forms.TextInput(attrs={'class': 'form-control'}), #if PasswordInput() - Editform will not display password.
            'Full_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'myDateClass',
                                                             'placeholder': 'dd-mm-YYYY'}),
            'Last_Degree': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
