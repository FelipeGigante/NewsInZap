from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://flipboard.com/@flipboardbr/edi-o-do-dia-vonp8btnz")


news_body_list = []
news_title_list = []
i = 0

while i < 6:
    i += 1
    news_title = driver.find_element_by_xpath("//*[@id='content']/div/div/div/div[2]/main/ul/li[{}]/div/article/div/h3/a".format(i))
    news_body = driver.find_elements(By.XPATH, "//*[@id='content']/div/div/div/div[2]/main/ul/li[{}]/div/article/div/p/a".format(i))
    news_title_list.append(news_title)
    news_body_list.append(news_body)    
    print(news_title)
    print(news_body)


#news_list = driver.find_elements(By.XPATH, "//*[@id='content']/div/div/div/div[2]/main/ul")
#news_data = []

# Percorrer os itens da lista <ul>
#for news_item in news_list:
#    news_data.append(news_item.text)

# Imprimir os dados das notícias
#for news in news_data:
#    print(news)


driver.quit()
