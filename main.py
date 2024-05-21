import requests
import requests
import bs4
import dotenv
import os

#protegendo os dados da API
dotenv.load_dotenv(dotenv.find_dotenv())


def get_page_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Falha ao acessar o site. Status code: {response.status_code}")
        return None

def consume_evolution_api(api_key, url, data):
    headers = {
        'apikey': api_key,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  
        return response.json() 
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return None


def main():
    api_key = os.getenv("api_key")
    url = os.getenv("url")
    
    url_news = 'https://ge.globo.com/'
    page_html = get_page_html(url_news)

   
    if page_html:
        pagehtml = bs4.BeautifulSoup(page_html, "html.parser")

        
        list_news = pagehtml.find_all("a", class_="feed-post-link")
        news_list = []

        for news in list_news[:5]:  
            title = news.text.strip()  
            link = news.get("href")  
            news_list.append({'title': title, 'link': link})

        number = os.getenv("number")
        message_body = "As 5 principais notícias de hoje:\n\n"
        for news in news_list:
            message_body += f"Título: {news['title']}\nLink: {news['link']}\n\n"

        print(message_body)
    else:
        print("Não foi possível obter o conteúdo da página.")


    data = {
        "number": f"{number}",
        "textMessage": {
            "text": f"{message_body}"
    }
    }

    response = consume_evolution_api(api_key, url, data)
    if response:
        print("Resposta da API:", response)
    else:
        print("Não foi possível obter uma resposta da API.")

if __name__ == "__main__":
    main()
