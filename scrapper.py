# Module naudojamas paraut kategorijos id is json failo

import json

# Opening the website 
# Naudosime bilietai.lt, nes top bilietu pardavimo plaforma, bet bus galima pridet daugiau

class Category:

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