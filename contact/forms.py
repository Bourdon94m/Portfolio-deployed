from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form form-control', 'placeholder': 'Name*', }))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email*'}))
    subject = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject*'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message*'}))
