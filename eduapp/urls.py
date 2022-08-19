from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('login/',login_request,name='login'),
    path('regist/',register,name='register'),
    path('loguot/',logout_request,name='logout'),
    path('profil',profil_request,name='profil')
]
