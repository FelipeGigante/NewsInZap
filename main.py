import requests
import bs4
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


#iniciando selenium, definindo navegador e inicializando objetos
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com")

#coletando as noticias e armazenando em um vetor 
url = 'https://ge.globo.com/'
request = requests.get(url)
text = []

pagehtml = bs4.BeautifulSoup(request.text, "html.parser")
list_news = pagehtml.find_all("a", class_="feed-post-link")


for news in list_news:
    print(news.text)
    print(news.get("href"))
    text.append(news)

#espera a página do whatsapp carregar
while len(driver.find_elements(By.ID, 'side')) < 1: 
    time.sleep(1)

#seta o número do whatsapp e a mensagem a ser enviada
link = f"https://web.whatsapp.com/send?phone=13991639366&text={text}"
driver.get(link)

#mesmo processo de carregamento
while len(driver.find_elements(By.ID, 'side')) < 1: 
    time.sleep(1)


if len(driver.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        
time.sleep(5)



