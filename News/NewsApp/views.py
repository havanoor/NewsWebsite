from django.shortcuts import render
from django.http import HttpResponse
import requests,json


#




def home(request):
    url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=3e4b5fd607dd40289b24ac5db977cc63"
    url2="https://newsapi.org/v2/everything?q=corona&apiKey=3e4b5fd607dd40289b24ac5db977cc63&sort-by=popularity"
    response1=requests.get(url)
    response2=requests.get(url2)
    val=response1.json()
    val2=response2.json()
    content={'TopHeadlines':val['articles'],'Popularity':val2['articles'][0:10]}

    return render(request,"index.html",content)