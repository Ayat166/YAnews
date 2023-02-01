from django.shortcuts import render 
import requests
# Create your views here.

def index(request):   
       r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           content.append(i['content'])
           newid.append(c)
           c+=1
       news = zip(title,description,image,url,newid,content)
       #request.session['news'] = news

       tobic="Headlines"
       context={
            'news':news,
            'tobic':tobic
        }
       return render(request,'pages/index.html',context)
    
def search(request):
    if 'search' in request.GET and 'btnsearch' in request.GET:
        search=request.GET['search']
        SEARCH_NEWS = "https://newsapi.org/v2/everything?apiKey=bbb83246743a4927bee52dcc7e7fb48e&q="
        s=SEARCH_NEWS+search
        r = requests.get(s)
        res = r.json()
        data = res['articles']
        title = []
        description = []
        image = []
        url = []
        content=[]
        tobic="Search"
        name = search
        newid=[] 
        c=0
        for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           content.append(i['content'])
           newid.append(c)
           c+=1
        news = zip(title,description,image,url,newid,content)
        context={
            'news':news,
            'tobic':tobic,
            'name':name
        }
        return render(request,'pages/index.html',context)
    
def genral(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=general&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           c+=1
       news = zip(title,description,image,url,newid,content)
       tobic="General"
       context={
            'news':news,
            'tobic':tobic
        }
       return render(request,'pages/index.html',context)
   
def business(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=business&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           c+=1
       news = zip(title,description,image,url,newid,content)
       tobic="Business"
       context={
            'news':news,
            'tobic':tobic
        }
       return render(request,'pages/index.html',context)
   
def sport(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=sport&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           c+=1
       news = zip(title,description,image,url,newid,content)
       tobic="Sport"
       context={
            'news':news,
            'tobic':tobic
        }
       return render(request,'pages/index.html',context)
   
def technology(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=technology&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           c+=1
       news = zip(title,description,image,url,newid,content)
       tobic="Technology"
       context={
            'news':news,
            'tobic':tobic
        }
       return render(request,'pages/index.html',context)

def entertainment(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=entertainment&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           c+=1
       news = zip(title,description,image,url,newid,content)
       tobic="Entertainment"
       context={
            'news':news,
            'tobic':tobic
        }
       return render(request,'pages/index.html',context)
   
         
def new(request,new_id):
       r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
         if(int(new_id)==c):
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           content.append(i['content'])
           newid.append(c)
           break
         c+=1
       news = zip(title,description,image,url,newid,content)

       context={
            'news':news,
       }
       return render(request,'pages/new.html',context)
   
def newBusiness (request,new_id):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=business&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
         if(int(new_id)==c):
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           break
         c+=1
       news = zip(title,description,image,url,newid,content)

       context={
            'news':news,
       }
       return render(request,'pages/new.html',context)
   
def newSport (request,new_id):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=sport&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
         if(int(new_id)==c):
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           break
         c+=1
       news = zip(title,description,image,url,newid,content)

       context={
            'news':news,
       }
       return render(request,'pages/new.html',context)
   
def newTechnology (request,new_id):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=technology&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
         if(int(new_id)==c):
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           break
         c+=1
       news = zip(title,description,image,url,newid,content)

       context={
            'news':news,
       }
       return render(request,'pages/new.html',context)
   
def newEntertainment (request,new_id):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=entertainment&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
         if(int(new_id)==c):
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           break
         c+=1
       news = zip(title,description,image,url,newid,content)

       context={
            'news':news,
       }
       return render(request,'pages/new.html',context)
   
def newSearch (request,new_id,name):
       SEARCH_NEWS = ('https://newsapi.org/v2/everything?apiKey=bbb83246743a4927bee52dcc7e7fb48e&q=')
       s=SEARCH_NEWS+str(name)
       r = requests.get(s)
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       newid=[]
       content=[]
       c=0
       for i in data:
         if(int(new_id)==c):
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
           newid.append(c)
           content.append(i['content'])
           break
         c+=1
       news = zip(title,description,image,url,newid,content)

       context={
            'news':news,
       }
       return render(request,'pages/new.html',context)