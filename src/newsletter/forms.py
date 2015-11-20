from django import forms
from .models import SignUp


class ContactForm(forms.Form): #no ModelForm
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

	def clean_email(self):
		"""This function will override the cleaned_data defined in views.py"""
		email = self.cleaned_data.get('email')
		return email

class SignUpForm(forms.ModelForm):

	class Meta:
		model = SignUp
		fields = ['email', 'full_name']

	def clean_email(self): #Note the function name must be followed by field name with clean_
		email = self.cleaned_data.get('email')
		if not '.edu' in email:
			raise forms.ValidationError("Please enter an academic email")
		
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		if not full_name:
			full_name = "Manoj Gautam"
		return full_name