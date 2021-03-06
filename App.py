from flask import Flask, render_template
from newsapi.newsapi_client import NewsApiClient
import urllib.parse
import json



app = Flask(__name__)


@app.route('/js/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')

@app.route('/.well-known/assetlinks.json', methods=['GET'])
def alj():
    return app.send_static_file('./assetlinks.json')

@app.route('/updata', methods=['GET'])
def up():
    newsapi = NewsApiClient(api_key="56f7ee8f6b4143269d9d2ac534374cbb")
    
    topheadlines = newsapi.get_top_headlines(country="in")
    for i in range(len(topheadlines['articles'])):
        if topheadlines['articles'][i]['content'] is not None:
            topheadlines['articles'][i]['content']=topheadlines['articles'][i]['content'][0:201] 
    with open("home.json", "w") as outfile:  
        json.dump(topheadlines['articles'], outfile)
    
    topwsj = newsapi.get_everything(domains="wsj.com")
    for i in range(len(topwsj['articles'])):
        if topwsj['articles'][i]['content'] is not None:
            topwsj['articles'][i]['content']=topwsj['articles'][i]['content'][0:201]
    with open("wsj.json", "w") as outfile:  
        json.dump(topwsj['articles'], outfile)

    toptechc = newsapi.get_top_headlines(sources="techcrunch")
    for i in range(len(toptechc['articles'])):
        if toptechc['articles'][i]['content'] is not None:
            toptechc['articles'][i]['content']=toptechc['articles'][i]['content'][0:201]
    with open("techc.json", "w") as outfile:  
        json.dump(toptechc['articles'], outfile)
    
    topgoogle = newsapi.get_top_headlines(sources="google-news-in")
    for i in range(len(topgoogle['articles'])):
        if topgoogle['articles'][i]['content'] is not None:
            topgoogle['articles'][i]['content']=topgoogle['articles'][i]['content'][0:201]
    with open("google.json", "w") as outfile:  
        json.dump(topgoogle['articles'], outfile)

    return("done")

@app.route('/')
def bbc():
    with open('home.json') as json_file: 
        data = json.load(json_file) 

    articles = data
    blog="blog"
    desc = []
    news = []
    img = []
    source = []
    link = []
    time = []
    cont = []
    lin = []
    parlink = []

    for i in range(len(articles)):
        lin.append("/".join([blog,articles[i]['url'].rsplit('/', 1)[-1]]))
        var = articles[i]['url'].rsplit('/', 1)[-1]
        var1 = "/".join(["https://trueornaw.herokuapp.com",blog,var])
        q = urllib.parse.quote(var1)
        parlink.append(var1)
        myarticles = articles[i]
        source.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
        time.append(myarticles['publishedAt'])

    mylist = zip(source, news, desc, cont, img, link,time,lin,parlink)

    return render_template('home.html', context=mylist)

@app.route('/wsj')
def wsj():
    with open('wsj.json') as json_file: 
        data = json.load(json_file) 

    articles = data
    wsj = "wsj"
    desc = []
    news = []
    img = []
    source = []
    link = []
    time = []
    cont = []
    lin = []
    parlink = []

    for i in range(len(articles)):
        var = articles[i]['url'].rsplit('/', 1)[-1]
        var1 = "/".join([wsj,var])
        lin.append(var1)
        query = "/".join(["https://trueornaw.herokuapp.com",var1])
        q = urllib.parse.quote(query)
        parlink.append(q)
        myarticles = articles[i]
        source.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
        time.append(myarticles['publishedAt'])

    mylist = zip(source, news, desc, cont, img, link,time,lin,parlink)

    return render_template('home.html', context=mylist)

@app.route('/techcrunch')
def tech():
    with open('techc.json') as json_file: 
        data = json.load(json_file) 

    articles = data
    desc = []
    news = []
    img = []
    source = []
    link = []
    time = []
    cont = []
    lin = []
    parlink = []

    for i in range(len(articles)):
        var = articles[i]['url'].rsplit('/', 1)[-1]
        var1 = "/".join(["techcrunch",var])
        lin.append(var1)
        query = "/".join(["https://trueornaw.herokuapp.com",var1])
        q = urllib.parse.quote(query)
        parlink.append(q)
        myarticles = articles[i]
        source.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
        time.append(myarticles['publishedAt'])

    mylist = zip(source, news, desc, cont, img, link, time, lin,parlink)

    return render_template('home.html', context=mylist)

@app.route('/google/<string:news>')
def techpost(news):
    with open('google.json') as json_file: 
        data = json.load(json_file) 

    articles = data
    desc = []
    news = []
    img = []
    source = []
    link = []
    time = []
    cont = []
    lin = []
    parlink = []

    for i in range(len(articles)):
        var = articles[i]['url'].rsplit('/', 1)[-1]
        var1 = "/".join(["google",var])
        lin.append(var1)
        query = "/".join(["https://trueornaw.herokuapp.com",var1])
        q = urllib.parse.quote(query)
        parlink.append(q)
        if f"{news}" in lin:
            myarticles = articles[i]
            source.append(myarticles['author'])
            news.append(myarticles['title'])
            desc.append(myarticles['description'])
            cont.append(myarticles['content'])
            img.append(myarticles['urlToImage'])
            link.append(myarticles['url'])
            time.append(myarticles['publishedAt'])

    mylist = zip(source, news, desc, cont, img, link, time, lin,parlink)
           
    return render_template('index.html', context=mylist)

@app.route('/google')
def google():
    with open('google.json') as json_file: 
        data = json.load(json_file) 

    articles = data
    desc = []
    news = []
    img = []
    source = []
    link = []
    time = []
    cont = []
    lin = []
    parlink = []

    for i in range(len(articles)):
        var = articles[i]['url'].rsplit('/', 1)[-1]
        var1 = "/".join(["google",var])
        lin.append(var1)
        query = "/".join(["https://trueornaw.herokuapp.com",var1])
        q = urllib.parse.quote(query)
        parlink.append(q)
        myarticles = articles[i]
        source.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
        time.append(myarticles['publishedAt'])

    mylist = zip(source, news, desc, cont, img, link,time, lin,parlink)

    return render_template('index.html', context=mylist)

@app.route('/<string:country>/<string:name>')
def name(country,name):
    newsapi = NewsApiClient(api_key="56f7ee8f6b4143269d9d2ac534374cbb")
    topheadlines = newsapi.get_top_headlines(country=f"{country}",category=f"{name}")

    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    source = []
    link = []
    time = []
    cont = []
    lin = []
    parlink = []

    for i in range(len(articles)):
        var = articles[i]['url'].rsplit('/', 1)[-1]
        var1 = "/".join([f"{country}", f"{name}",var])
        lin.append(var1)
        query = "/".join(["https://trueornaw.herokuapp.com",var1])
        q = urllib.parse.quote(query)
        parlink.append(q)
        myarticles = articles[i]
        source.append(myarticles['author'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
        time.append(myarticles['publishedAt'])

    mylist = zip(source, news, desc, cont, img, link,time, lin,parlink)
    
    return render_template('index.html', context=mylist)    


@app.route('/<string:country>/<string:name>/<string:post>')
def post(country,name,post):
    newsapi = NewsApiClient(api_key="56f7ee8f6b4143269d9d2ac534374cbb")
    topheadlines = newsapi.get_everything(country=f"{country}",category=f"{name}")

    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    source = []
    link = []
    time = []
    cont = []
    lin = []
    parlink = []
    for i in range(len(articles)):
        lin = articles[i]['url'].rsplit('/', 1)[-1]
        var = articles[i]['url'].rsplit('/', 1)[-1]
        var1 = "/".join([f"{country}", f"{name}",var])
        query = "/".join(["https://trueornaw.herokuapp.com",var1])
        q = urllib.parse.quote(query)
        parlink.append(q)
        if f"{post}" in lin:
    
            myarticles = articles[i]
            source.append(myarticles['author'])
            news.append(myarticles['title'])
            desc.append(myarticles['description'])
            cont.append(myarticles['content'])
            img.append(myarticles['urlToImage'])
            link.append(myarticles['url'])
            time.append(myarticles['publishedAt'])

    mylist = zip(source, news, desc, cont, img, link, time, lin,parlink)
    return render_template('blog.html', context=mylist)

@app.route('/blog/<string:post>')
def bpost(post):
    with open('home.json') as json_file: 
        data = json.load(json_file) 

    articles = data
    desc = []
    news = []
    img = []
    source = []
    link = []
    time = []
    cont = []
    lin = []
    parlink = []
    for i in range(len(articles)):
        lin = articles[i]['url'].rsplit('/', 1)[-1]
        query = "/".join(["https://trueornaw.herokuapp.com","blog",lin])
        q = urllib.parse.quote(query)
        parlink.append(q)
        if f"{post}" in lin:
    
            myarticles = articles[i]
            source.append(myarticles['author'])
            news.append(myarticles['title'])
            desc.append(myarticles['description'])
            cont.append(myarticles['content'])
            img.append(myarticles['urlToImage'])
            link.append(myarticles['url'])
            time.append(myarticles['publishedAt'])

    mylist = zip(source, news, desc, cont, img, link, time, lin,parlink)
    return render_template('blog.html', context=mylist)


if __name__ == "__main__":
    app.run()