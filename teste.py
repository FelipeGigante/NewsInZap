from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://flipboard.com/@flipboardbr/edi-o-do-dia-vonp8btnz")

# Inicialize as listas
news_title_list = []
news_body_list = []

# Iterar de 1 a 4 (inclusive)
for i in range(1, 5):
    try:
        # Esperar até que o título da notícia esteja presente na página
        news_title_xpath = f"//*[@id='content']/div/div/div/div[2]/main/ul/li[{i}]/div/article/div/h3/a"
        news_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, news_title_xpath)))
        
        # Esperar até que o corpo da notícia esteja presente na página
        news_body_xpath = f"//*[@id='content']/div/div/div/div[2]/main/ul/li[{i}]/div/article/div/p/a"
        news_body = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, news_body_xpath)))
        
        # Adicionar os textos do título e corpo às listas
        news_title_list.append(news_title)
        news_body_list.append(news_body)
        
        # Imprimir o título e corpo da notícia
        print("Título:", news_title_list[i])
        print("Corpo:", news_body_list[i])
    
    except Exception as e:
        print(f"Erro ao encontrar notícia {i}: {e}")

# Imprimir as listas de títulos e corpos das notícias
print(news_title_list)
print(news_body_list)
