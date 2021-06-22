from django.shortcuts import render , redirect
from django.views import View
from django.contrib import auth
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect
from .models import summer , spring , winter , autem
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index( request ):
    return render( request , "profil/index.html" )


def test( request ):
    summers = summer.objects.all()
    springs = spring.objects.all()
    winters = winter.objects.all()
    autems = autem.objects.all()
    return render( request , "profil/user_page.html" , {"title": "Главная страница " ,
                                                        "content_summer": summers ,
                                                        "content_winter": winters ,
                                                        "content_autm": autems ,
                                                        "content_spring": springs
                                                        } )


def about( requset ):
    return render( requset , "profil/about.html" )


def registation( request ):
    return render( request , 'profil/registration.html' )


def user_page( request ):
    summers = summer.objects.all()
    springs = spring.objects.all()
    winters = winter.objects.all()
    autems = autem.objects.all()
    if request.method == 'POST':
        mail_of_user = request.POST['email']
        send_mail("Бесплатная подписка" , "Вы подписались на наш сайт ""Кулпати""",settings.EMAIL_HOST_USER,[mail_of_user])
        messages.info(request ,"Вы отправели запрос на рассылку")
        return render(request,'profil/main_page.html',{'title' : 'Главная страница'})
    return render( request , "profil/main_page.html" , {"title": "Главная страница " ,
                                                        "content_summer": summers ,
                                                        "content_winter": winters ,
                                                        "content_autm": autems ,
                                                        "content_spring": springs ,
                                                        } )


def login( request ):
    if request.method == 'POST':
        username = request.POST[ 'username' ]
        password = request.POST[ 'password' ]
        user = authenticate( username=username , password=password )

        if user is not None:
            auth.login( request , user )
            return redirect( '/' )
    else:
        messages.info( request , 'Введены некоректные данные ' )
        return render( request , 'registration/login.html' )
    messages.info( request , 'Введены некоректные данные ' )
    return render( request , 'registration/login.html' )


def logouts( request ):
    logout( request )
    return redirect( '/' )


# page_of_winter
# page_of_summer
# page_of_autmn
# page_of_spring

def page_of_winter( request ):
    winters = winter.objects.all()
    return render( request , "profil/page_of_winter.html" , {"title": "Главная страница " ,
                                                             "content_winter": winters ,
                                                             } )


def page_of_summer( request ):
    summers = summer.objects.all()
    return render( request , "profil/page_of_summer.html" , {"title": "Летняя страница " ,
                                                             "content_summer": summers ,
                                                             } )


def page_of_autumn( request ):
    autems = autem.objects.all()
    return render( request , "profil/page_of_autumn.html" , {"title": "Осенняя страница " ,
                                                             "content_autm": autems ,
                                                             } )


def page_of_spring( request ):
    springs = spring.objects.all()
    return render( request , "profil/page_of_spring.html" , {"title": "Весенняя страница " ,
                                                             "content_spring": springs
                                                             } )
