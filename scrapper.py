# Module naudojamas paraut kategorijos id is json failo
from selenium import webdriver
import webdriver_manager.chrome as ChromeDriverManager
from bs4 import BeautifulSoup as bs
import json

class CategoryData:

    def __init__(self, failas, kategorija):
        self.failas = failas
        self.kategorija = kategorija

    def get_category(self):
        with open(self.failas, 'r') as f:
            data = json.load(f)
        for i in data['categories']:
            if i['title'] == self.kategorija:
                category_id = i['id']
                url = f'https://www.bilietai.lt/lit/renginiai/visi/category:{category_id}/status:insales/country:14/order:date,asc'
                return url
        else:
            return 0   

    def get_a_tags(self):
        driver = webdriver.Chrome()
        driver.get(self.get_category())
        soup = bs(driver.page_source, 'html.parser')
        results = soup.find_all('a', {'class': 'event_short event'})
        print(map(lambda x: x.get_text(), results))
        return results

    def get_hrefs(self):
        hrefs = [a_tag.get('href') for a_tag in self.results]
        return hrefs

    def get_titles(self):
        titles = [a_tag.get('event_short_title') for a_tag in self.results]
        return titles   

    def ticket_prices(self):
        prices = []
        
        for i in self.get_a_tags():
            driver = webdriver.Chrome()
            driver.get(self.get_category())
            soup = bs(driver.page_source, 'html.parser')
            results = soup.find_all('span', {'class': 'event_short_price_text'}).text
            prices.append(results)
        
        return prices

data = CategoryData('kategorijos.json', 'sportas')
print(data.get_a_tags())
print(data.get_hrefs())
print(data.ticket_prices())