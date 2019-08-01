from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import auth
from .models import Team

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user( username= request.POST['username'], password = request.POST['password'])
            auth.login(request, user)
            return redirect('index')
    return redirect('index')

def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(request, username=username , password = password)
                if user is not None:
                        auth.login(request,user)
                        return redirect('index')
                else:
                        return redirect('index')
        else:
                return redirect('index')

def delete(request, account_id):
        account = Account.objects.get(id=account_id)
        account.delete()
        return redirect('index')

def home(request):

    return render(request,'index.html')

def loginhome(request):
    return render(request,'login.html')