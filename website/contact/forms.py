from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    """Форма подписки на email"""

    class Meta:
        model = Contact
        fields = ['email']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Your Email...'})
        }
        labels = {
            'email': ''
        }
