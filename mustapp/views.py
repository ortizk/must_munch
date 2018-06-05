from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Options
from .forms import LoginForm

def index(request):
	return render(request, 'index.html')

def categories(request):
	return render(request, 'categories.html')

def options(request, option_cat):
	if option_cat == 'drinks' or option_cat == 'datenight' or option_cat == 'eats':
		options = None
		try:
			options = Options.objects.filter(category=option_cat).values()
			print('this is the options:', options)
			return render(request, 'options.html', { 'option': options, 'option_cat': option_cat })
		except:
			return HttpResponse('EXC: that is not an option')
	else:
		return HttpResponse('ELSE: that is not an option')
	# return render(request, 'options.html', { 'option': options })