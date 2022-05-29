from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
#@login_required()
def index(request):
    messages.add_message(request, messages.INFO, 'Welcome to Hospital website.')
    return render(request, 'home/base.html')
