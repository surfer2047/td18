from django.shortcuts import render
from django.conf import settings #Import the project settings file
from django.core.mail import send_mail
from .forms import SignUpForm, ContactForm
from django.http import HttpResponseRedirect
from .models import SignUp

def home(request):
	title = "Welcome"
	#print request.method
	# if request.method == "POST":	
	form = SignUpForm(request.POST or None) #if data or not
	context = {'form': form}
	if form.is_valid():
		# form.save()
		instance = form.save(commit=False) #commit=False preventing from saving us data
		# fullname = form.cleaned_data.get('full_name')
		# if not fullname:
		# 	instance.full_name = "Manoj Gautam"
		# if not instance.full_name:
		# 	instance.full_name = "Ravi prasad"
		# 	print instance.full_name
		instance.save() #It directly save into the database
		form = SignUpForm()
	
	if request.user.is_authenticated():
		emails = SignUp.objects.all().order_by('-timestamp')
		print emails
		context = {'emails': emails}

	return render(request, 'newsletter/home.html', context)


def contact(request):
	form = ContactForm(request.POST or None)
	context = {'form': form,}
	if form.is_valid():
		form_email = form.cleaned_data.get('email') #This will be overrride if it the cleaned_data is defined in forms.py
		form_full_name = form.cleaned_data.get('full_name')
		form_message = form.cleaned_data.get('message')
		subject = "Xterm Nepal Pvt. Ltd contact message"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s %s via %s" %(form_full_name, form_message, form_email)
		mail = send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
		if mail:
			context = {'success': "Your message sent successfully",}
	return render(request, 'newsletter/contact.html', context)