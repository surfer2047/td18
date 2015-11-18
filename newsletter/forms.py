from django import forms
from .models import SignUp

class SingUpForm(forms.ModelForm):
	"""Form for email singup"""
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
		