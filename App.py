from flask import Flask, render_template
from newsapi.newsapi_client import NewsApiClient
import urllib.parse



app = Flask(__name__)



@app.route('/bbc1')
def Index():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        myarticles = articles[i]


        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])



    mylist = zip(news, desc, img)


    return render_template('bbc1.html', context = mylist)

@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')

@app.route('/')
def bbc():
    newsapi = NewsApiClient(api_key="56f7ee8f6b4143269d9d2ac534374cbb")
    topheadlines = newsapi.get_top_headlines(country="in")

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
        lin.append(articles[i]['url'].rsplit('/', 1)[-1])
        query = "/".join(["https://trueornaw.herokuapp.com",articles[i]['url'].rsplit('/', 1)[-1]])
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

@app.route('/wsj')
def wsj():
    newsapi = NewsApiClient(api_key="56f7ee8f6b4143269d9d2ac534374cbb")
    topheadlines = newsapi.get_everything(domains="wsj.com")

    articles = topheadlines['articles']
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
    newsapi = NewsApiClient(api_key="56f7ee8f6b4143269d9d2ac534374cbb")
    topheadlines = newsapi.get_top_headlines(sources="techcrunch")

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
    newsapi = NewsApiClient(api_key="56f7ee8f6b4143269d9d2ac534374cbb")
    topheadlines = newsapi.get_top_headlines(sources="google-news-in")

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
    newsapi = NewsApiClient(api_key="56f7ee8f6b4143269d9d2ac534374cbb")
    topheadlines = newsapi.get_top_headlines(sources="google-news-in")

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

if __name__ == "__main__":
    app.run()