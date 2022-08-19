from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,'home.html')


def login_request(request):
  if request.method=='POST':
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      login(request, user)
      return redirect('/profil')
    else:
      return HttpResponse('bunday malumot yoq    <a href="/login">ortga</a>')
  return render(request, 'login.html')

def register(request):
  if request.method=='POST':
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    password1=request.POST['password1']
    if password1==password:
      user=User.objects.create_user(username=username , email = email , password = password)
      user.save()  
      if user is not None:
        login (request, user)
      return redirect('/profil')
    
  return render(request,'register.html')



def logout_request(request):
  logout(request)
  return redirect('/login')

def profil_request(request):
    Ism = request.user.username
    return render(request,'profil_home.html',{'Ism':Ism})
    