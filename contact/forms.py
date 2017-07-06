from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    Message = forms.CharField(required=True, label="",
                              widget=forms.Textarea(attrs={'placeholder': 'Type your message here and we\'ll get back to you soon!',
                                                           'cols': '20'}))
