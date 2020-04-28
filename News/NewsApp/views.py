from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests,json
from django.views.generic import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *







# def home(request):
#     url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=3e4b5fd607dd40289b24ac5db977cc63"
#     url2="https://newsapi.org/v2/everything?q=corona&apiKey=3e4b5fd607dd40289b24ac5db977cc63&sort-by=popularity"
#     response1=requests.get(url)
#     response2=requests.get(url2)
#     val=response1.json()
#     val2=response2.json()
#     content={'TopHeadlines':val['articles'],'Popularity':val2['articles'][0:10]}

#     return render(request,"index.html",content)

# def new(request):
#     url3='https://newsapi.org/v2/everything?q=sports&apiKey=3e4b5fd607dd40289b24ac5db977cc63'
#     response3=requests.get(url3)
#     val3=response3.json()
#     content={'Topic':val3['articles']}
#     return render(request,'sports.html',content)


class HomeView(View):
    def get(self,request,*args,**kwargs):
        url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=3e4b5fd607dd40289b24ac5db977cc63"
        url2="https://newsapi.org/v2/everything?q=corona&apiKey=3e4b5fd607dd40289b24ac5db977cc63&sort-by=popularity"
        response1=requests.get(url)
        response2=requests.get(url2)
        val=response1.json()
        val2=response2.json()
        content={'TopHeadlines':val['articles'],'Popularity':val2['articles'][0:10]}

        return render(self.request,"home.html",content)

class TopicView(View):
    def get(self,request,*args,**kwargs):
        news_topic=kwargs['topic']
        url3=f'https://newsapi.org/v2/everything?q={news_topic}&apiKey=3e4b5fd607dd40289b24ac5db977cc63'
        print(kwargs,"Keyword arguments")
        response3=requests.get(url3)
        val3=response3.json()
        content={'Topic':val3['articles']}
        return render(self.request,'topic.html',content)

# def login(request):
#     form=Loginform()
#     return render(request,'login.html',{'form':form})


def loginUser(request):
    error=None
    form=Loginform()

    if request.method == 'POST':
        username =request.POST['username']
        passw =request.POST['password']
        user = authenticate(username=username, password=passw)
        if user is not None:
            login(request, user) # logs User in
            return redirect('Home')
        else:
            #return render(request, 'signup.html', {'error': "Unable to Log you in!"})
            error="Try again"
    return render(request, 'login.html', {'error': error,'form':form})


def register(request):
    form=new_user(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            pref=Choices.objects.create(preferences=request.POST['topics2'],user=User.objects.get(username=request.POST['username']))

            print(request.POST,"Hhhhhhhhhhheeeeeeeeeeeeeeee")
            return redirect('Home')

    return render(request,'signup.html',{'form':form})

def test(request):
    val=Choices.objects.get(user=request.user)
    Choices.objects.create(user=request.user,preferences=('Business','Technology'))
    return HttpResponse(val)