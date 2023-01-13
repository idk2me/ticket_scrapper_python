import scrapper as sc

data = sc.Category('kategorijos.json', 'sportas')

if(data != 0):
    driver = webdriver.Chrome()
    driver.get(data.get_category())

    soup = bs(driver.page_source, 'html.parser')

    

    # Getting all the links
    def get_hrefs(html):
        """
        Extracts all 'href' attributes from 'a' tags with the 'event_short event' class.
        """
        # Parse the HTML using BeautifulSoup
        soup = bs(html, 'html.parser')
        
        
        # Find all 'a' tags with the 'event_short event' class
        a_tags = soup.find_all('a', {'class': 'event_short event'})
        
        # Extract the 'href' attribute from each 'a' tag
        hrefs = [a_tag.get('href') for a_tag in a_tags]
        
        # Return the list of 'href' attributes
        return hrefs

    # scroll down page by 1000 pixels 
    driver.execute_script("window.scrollBy(0, 1000)")
    print(get_hrefs(driver.page_source))
    print(len(get_hrefs(driver.page_source)))

    driver.quit()
else:
    print("Su visa derama pagarba, Jūs esate idiotas")
