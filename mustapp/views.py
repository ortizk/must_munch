from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from .models import Options
from .forms import LoginForm
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy


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
		return HttpResponseRedirect(reverse('options:rate', args=(rest.id,)))




