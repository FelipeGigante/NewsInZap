import requests
import bs4

url = 'https://ge.globo.com/'

request = requests.get(url)

pagehtml = bs4.BeautifulSoup(request.text, "html.parser")
list_news = pagehtml.find_all("a", class_="feed-post-link")


for news in list_news:
    print(news.text)
    print(news.get("href"))