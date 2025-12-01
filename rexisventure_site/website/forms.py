from django import forms
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ["full_name", "email", "phone", "company", "subject", "message"]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Full name",
                "class": "form-control",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Work email",
                "class": "form-control",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Phone (optional)",
                "class": "form-control",
            }),
            "company": forms.TextInput(attrs={
                "placeholder": "Company / agency",
                "class": "form-control",
            }),
            "subject": forms.TextInput(attrs={
                "placeholder": "How can we help?",
                "class": "form-control",
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Tell us about your safety, industrial or lab supply needs...",
                "class": "form-control",
                "rows": 5,
            }),
        }
