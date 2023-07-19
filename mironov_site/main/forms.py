from django import forms


# Форма связи Contacts
class ContactForm(forms.Form):
    first_name = forms.CharField(label="Имя",
                                 widget=forms.TextInput(attrs={"class": "form-control", "id": "fname"}))
    # telephone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={"type": "tel", "class": "form-control", "id": "tel"}))
    telephone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={"class": "form-control", "id": "tel"}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={"class": "form-control", "id": "email"}))
    subject = forms.CharField(label="Тема сообщения", widget=forms.TextInput(attrs={"class": "form-control", "id": "subject"}))
    message = forms.CharField(label="Сообщение",
                              widget=forms.Textarea(attrs={"class": "form-control", "id": "message", "cols": 30, "rows": 7 }))
