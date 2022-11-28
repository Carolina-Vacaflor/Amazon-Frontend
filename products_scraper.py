import requests, random
from bs4 import BeautifulSoup
from models.product import Product
from services.product_service import Product_Service

def get_products(search):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
        ]
    random_user_agent = random.choice(user_agents)
    headers = {
        'authority': 'scrapeme.live',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': random_user_agent,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
    url = 'https://www.amazon.com/s?k='+search.strip()
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    first_list = list()

    for post in soup.find_all("div", {"class":"a-section"}):
        title = post.find("span", {"class": "a-size-medium a-color-base a-text-normal"})
        rate = post.find("span", {"class": "a-icon-alt"})
        review = post.find("span", {"class": "a-size-base s-underline-text"})
        price = post.find("span", {"class": "a-offscreen"})
        img = post.find("img", {"class": "s-image"})
        link = post.find("a", {"class": "a-link-normal s-no-outline"})
        if (link is not None):
            product_link = "https://www.amazon.com"+str(link['href'])
        if (img is not None):
            img_link = img['src']
        if (title is not None) and (rate is not None) and (review is not None) and (price is not None) and (img_link is not None) and (product_link is not None):
            product = Product(product_link, title.text, rate.text, review.text, price.text, img_link)
            first_list.append(product)

    final_list = list()
    id_list = list()
    product_service = Product_Service()

    for item in first_list:
        if item.id not in id_list:
            id_list.append(item.id)
            final_list.append(item)
            product_service.store_product(item)

    if(len(final_list) == 0):
        error_product = Product('There was an issue trying to load the page.','We are very sorry for the inconvenince.','Please try to reload the page.',':(','https://content.spiceworksstatic.com/service.community/p/cms_microsite_attachments/0000002161/59668faa/attached_file/sad-computer.png','https://content.spiceworksstatic.com/service.community/p/cms_microsite_attachments/0000002161/59668faa/attached_file/sad-computer.png')
        final_list.append(error_product)
    


    return final_list