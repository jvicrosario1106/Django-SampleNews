from django.shortcuts import render,redirect
from newsapi import NewsApiClient

# Create your views here.

def news(request):
    if request.method == "POST":
        news = request.POST["news"]
        news_api = NewsApiClient(api_key="70e906e588e649f2991e4d226971b2ce")
        news_article = news_api.get_everything(q=news, qintitle=news)


        news_headlines = news_article["articles"] 
        title = []
        desc = []
        images = []
        url = []
    
        for n in news_headlines:
            title.append(n["title"])
            desc.append(n["description"])
            images.append(n["urlToImage"])
            url.append(n["url"])

        news_list = zip(title,images,desc,url)
        

        content = {

            "news_list":news_list
        }

    else:
        content = {}

    return render(request, "newsapp/news.html",content)