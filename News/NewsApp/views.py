from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests,json
from django.views.generic import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
import datetime
from bs4 import BeautifulSoup







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


def stock_price():
    final=[]
    for i in ['NFLX','TATAMOTORS.NS','INFY','MARUTI.NS','ICICIBANK.NS']:

        stock={}
        user_agent = {'User-agent': 'Mozilla/5.0'}
        url=f'https://in.finance.yahoo.com/quote/{i}?p={i}&.tsrc=fin-srch'
        page=requests.get(url,headers=user_agent)
        #print(page.content)

        soup=BeautifulSoup(page.text,'html.parser')
        #print(soup)
        val=(soup.find_all('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px)"}))
        cost=val[0].find_all('span',{'class':'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})
        print(cost[0].text)
        stock['cost']=cost[0].text
        v=soup.find_all('h1',class_="D(ib) Fz(16px) Lh(18px)")
        stock['name']=v[0].text
        price=val[0].find_all('span',{'class':'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)'})

        #print(price[0].text)
        stock['profit']=price[0].text[0]
        stock['percent']=price[0].text
        final.append(stock)
    return final


class HomeView(View):
    def get(self,request,*args,**kwargs):
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=2)

        url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=3e4b5fd607dd40289b24ac5db977cc63"
        
        if request.user.is_authenticated :
            print("Hello",request.user.is_authenticated)
            
            text=test(request.user)
            print(text)
            url2=f'https://newsapi.org/v2/everything?q={text}&apiKey=3e4b5fd607dd40289b24ac5db977cc63&sort-by=popularity'
        else:
            url2="https://newsapi.org/v2/everything?q=corona&apiKey=3e4b5fd607dd40289b24ac5db977cc63&sort-by=popularity"
        url3=f'https://api.covid19api.com/country/india?from={yesterday}T00:00:00Z&to={today}T00:00:00Z'
        #url3='https://api.covid19api.com/country/india?from=2020-04-27T00:00:00Z&to=2020-04-29T00:00:00Z'


        response1=requests.get(url)
        response2=requests.get(url2)
        response3=requests.get(url3)

        val=response1.json()
        val2=response2.json()
        val3=response3.json()
        val3[1]['Active']=val3[1]['Confirmed']-val3[1]['Recovered']

        data={  'ChangeConfirm':val3[1]['Confirmed']-val3[0]['Confirmed'],
                'ChangeRecover':val3[1]['Recovered']-val3[0]['Recovered'],
                'ChangeDeath':val3[1]['Deaths']-val3[0]['Deaths']}
        content={'TopHeadlines':val['articles'][0:9],'Popularity':val2['articles'][0:10],'Cdata':val3[1],'Change':data,'stock':stock_price()}

        return render(self.request,"home.html",content)

    def post(self,request,*args,**kwargs):
        #return HttpResponse(self.request.POST['Type'])
        news_topic=self.request.POST['Type'].lower()
        url3=f'https://newsapi.org/v2/everything?q={news_topic}&apiKey=3e4b5fd607dd40289b24ac5db977cc63'
        print(kwargs,"Keyword arguments")
        response3=requests.get(url3)
        val3=response3.json()
        content={'Topic':val3['articles']}
        return render(self.request,'topic.html',content)

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

def logout_view(request):
	logout(request)
	return redirect('Home')


def test(use):
    all=[]
    s=''
    val=Choices.objects.get(user=use)
    #Choices.objects.create(user=request.user,preferences=('Business','Technology'))
    for i in val.preferences:
        all.append(i)
        s +=' '+i.lower()+' AND' 
        v='(' +s[0:len(s)-3] + ')'
    return v
    #return HttpResponse(s[0:len(s)-3])

def logout_request(request):
    logout(request)
    
    return redirect("Home")