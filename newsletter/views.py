from django.shortcuts import render
from .forms import SignUpForm

def home(request):
	title = "Welcome"
	#print request.method
	# if request.method == "POST":	
	form = SignUpForm(request.POST or None) #if data or not
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
	context = {'form': form}
	return render(request, 'newsletter/home.html', context)