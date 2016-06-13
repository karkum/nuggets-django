from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from nuggetsapp.models import Nugget
from nuggetsapp.serializers import NuggetSerializer
import logging
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'nuggetsapp/home.html', {})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return render(request, 'nuggetsapp/home.html', {'status': 'success'})
        else:
            return render(request, 'nuggetsapp/home.html', {'status': 'inactive'})
    else:
        return render(request, 'nuggetsapp/home.html', {'status': 'invalid'})

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
    nuggets = Nugget.get_nuggets_by_user(request.user.id)
    return render(request, 'nuggetsapp/my-nuggets.html', {'nuggets': nuggets})

@api_view(['GET'])
def nuggets_for_user(request, user_id):
    nuggets = Nugget.get_nuggets_by_user(user_id)
    serializer = NuggetSerializer(nuggets, many=True)
    return Response(serializer.data)
