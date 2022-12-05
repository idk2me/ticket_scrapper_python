import selenium 
from selenium import webdriver
import webdriver_manager.chrome as ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import json


# Opening the website 
# Naudosime bilietai.lt, nes top bilietu pardavimo plaforma, bet bus galima pridet daugiau
f = open('kategorijos.json')
id = json.load(f)
# print(id)

muziejai_id = id['categories'][0]['id']
teatras_id = id['categories'][1]['id']
koncertai_id = id['categories'][2]['id']
sportas_id = id['categories'][3]['id']
festivaliai_id = id['categories'][4]['id']
kinas_id = id['categories'][5]['id']
kita_id = id['categories'][6]['id']

url = f'https://www.bilietai.lt/lit/renginiai/visi/category:{int(festivaliai_id)}/status:insales/order:date,asc'

driver = webdriver.Chrome()
driver.get(url)

# HTML parser
soup = bs(driver.page_source, 'html.parser')
results = soup.find_all('a', {'class': 'event_short event'})
print(results[0])

item = results[0]
atag = item['a']
description = atag

print(description)
print(atag.get('href'))

driver.quit()