from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import candidate , applied_job
from django.contrib.auth.models import User


from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 10 or len(phone) > 25:
            raise ValidationError("Phone number must be between 10 and 25 characters.")
        return phone

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'phone', 'password1', 'password2']


class ApplyForm(forms.ModelForm):
    class Meta:
        model = applied_job
        fields = [
            'city',
            'address',
            'experience',
            'cover_letter',
            'resume',
        ]

class Candidate_update(forms.ModelForm):
    class Meta:
        model = candidate
        fields = [
            "name" ,
            "email" ,
            "phone" ,
            "profile" ,
        ]



