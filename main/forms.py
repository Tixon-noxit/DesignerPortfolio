from django import forms


# Форма связи Contacts
class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name",
                                 widget=forms.TextInput(attrs={"class": "form-control", "id": "fname"}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={"class": "form-control", "id": "lname"}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={"class": "form-control", "id": "email"}))
    subject = forms.CharField(label="Subject", widget=forms.TextInput(attrs={"class": "form-control", "id": "subject"}))
    message = forms.CharField(label="Message",
                              widget=forms.Textarea(attrs={"class": "form-control", "id": "message", "cols": 30, "rows": 7 }))
