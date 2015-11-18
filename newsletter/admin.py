from django.contrib import admin
from .models import SignUp
from .forms import SingUpForm

class SignUpAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'email', 'timestamp', 'updated']
	# fields = ['email'] #Used to order the forms, can be done through the meta class using forms
	class Meta:
		model = SignUp
		form = SingUpForm

admin.site.register(SignUp, SignUpAdmin)