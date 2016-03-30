from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from nuggetsapp.models import Nugget
import json
import logging
logger = logging.getLogger(__name__)

def home(request):
    next_url = request.GET.get('next')
    return render(request,
                  'nuggetsapp/home.html',
                  {
                      'next_url': next_url,
                      'form': UserCreationForm()
                  })

def signup(request):
    next_url = request.POST.get('next_url')
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
        auth_login(request, new_user)
        if next_url:
            return redirect(next_url)
        return redirect('/react')
    else:
        return render(request,
                      'nuggetsapp/home.html',
                      {
                          'next_url': next_url,
                          'form': UserCreationForm()
                      })

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            return redirect('/react')
        else:
            return render(request, 'nuggetsapp/home.html', {'status': 'inactive'})
    else:
        return render(request, 'nuggetsapp/home.html', {'status': 'invalid'})

def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required
def add_nugget(request):
    return render(request, 'nuggetsapp/add-nugget.html', {})

@login_required
def add_nugget_post(request):
    user = request.user
    text = request.POST['text']
    tags = request.POST['tags']
    source = request.POST['source']
    logger.info('user %s, text %s, tags %s, source %s' % (user, text, tags, source))
    nugget = Nugget.create_new_nugget(user, text, tags, source)
    return render(request, 'nuggetsapp/add-nugget.html', {'nugget': nugget})

@login_required
def my_nuggets(request):
    nuggets = Nugget.get_nuggets_by_user(request.user)
    return render(request, 'nuggetsapp/my-nuggets.html', {'nuggets': nuggets})

@login_required
def get_my_nuggets(request):
    from django.core import serializers # we should probably use something like http://www.django-rest-framework.org/api-guide/serializers/
    nuggets = Nugget.get_nuggets_by_user(request.user)
    return HttpResponse(json.dumps([nugget['fields'] for nugget in json.loads(serializers.serialize('json', nuggets))]))

@login_required
def react(request):
    app_state = {}
    app_state['user'] = {
        'username': request.user.get_username(),
        'is_authenticated': request.user.is_authenticated(),
        'is_active': request.user.is_active,
        'email': request.user.email,
        'id': request.user.id,
        'full_name': request.user.get_full_name()
    }
    return render(request, 'nuggetsapp/index.html', {'app_state': json.dumps(app_state)})
