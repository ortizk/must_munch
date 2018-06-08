from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from .models import Options
from .forms import LoginForm, SignupForm
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages



def index(request):
	return render(request, 'index.html')

def categories(request):
	return render(request, 'categories.html')

def options(request, option_cat):
	if option_cat == 'drinks' or option_cat == 'datenight' or option_cat == 'eats':
		options = None
		try:
			options = Options.objects.filter(category=option_cat).values()
			return render(request, 'options.html', { 'option': options, 'option_cat': option_cat })
		except:
			return HttpResponse('EXC: that is not an option')
	else:
		return HttpResponse('ELSE: that is not an option')
	# return render(request, 'options.html', { 'option': options })

def upvote(request, rest_id, option_cat):
    rest = Options.objects.get(pk=rest_id)
    rest.rate += 1
    rest.save(['rate'])
    return render ('options.html')

# class Upvote(UpdateView):
# 	model = Options
# 	fields = ['rate']
# 	success_url = reverse_lazy('[options.html]')
# 	pass

def vote(request, rest_id):
	restaurant = get_object_or_404(Options, pk=rest_id)
	try:
		upvote = options.rate_set.get(pk=request.POST['rate'])
	except (KeyError, Options.DoesNotExist):
		return HttpResponse('except at def vote')
	else:
		upvote.rate += 1
		upvote.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('options:rate', args=(rest.id,)))

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
            user = User.objects.create_user(username = u, email = e, password = p)
            print('created new user', user)
            user.save()
            print("saved new user:", user)
            user = authenticate(username = u, email = e, password = p)
            print("authenticated new user:", user)
            login(request,user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/mustapp/seattle/')
				else:
					print('The account has been disabled.')
			else:
				messages.info(request, 'Your username and/or password in incorrect.')
				print('The username and/or password in incorrect.')
	else:
		form = LoginForm()
		return render(request, 'login.html', {'form': form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/mustapp')




