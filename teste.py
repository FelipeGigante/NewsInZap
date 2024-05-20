from selenium import webdriver
driver_path = "C:\\Users\\5150s\\AppData\\Local\\Programs\\Python\\Python38\\chromedriver.exe"
brave_path = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
browser = webdriver.Chrome(executable_path=driver_path, options=option)
browser.get("https://www.google.es")