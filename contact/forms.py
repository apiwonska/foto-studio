from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label="Imię i Nazwisko", required=True, widget=forms.TextInput(
		attrs={'class':'form-control', 'placeholder':'Wpisz Imię i Nazwisko'}), min_length=2, max_length=100)
	email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
		attrs={'class':'form-control', 'placeholder':'Wpisz email'}), min_length=5, max_length=100)
	content = forms.CharField(label="Twoja Wiadomość", required=True, widget=forms.Textarea(
		attrs={'class':'form-control','rows':5, 'placeholder':'Treść wiadomości'}), min_length=10, max_length=1000)
