from flask import Flask, render_template, flash, request
from bs4 import BeautifulSoup
from wtforms import Form, TextAreaField, validators, StringField, SubmitField
import requests



app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    return(render_template('home.html'))


@app.route("/form", methods = ['GET', 'POST'])
def home2():
    search = request.form.get("search")
    return(render_template('form.html', search = search))  


@app.route("/results", methods = ['GET', 'POST'])
def get_info():
    example_list1 = [('Wireless Mouse, E-YOOSO Computer Mouse 18 Months Battery Life Cordless Mouse, 5-Level 2400 DPI, 6 Button Ergo Wireless Mice, 2.4G Portable USB Wireless Mouse for Laptop, Mac, Chromebook, PC, Windows', '4.5 out of 5 stars', '4,189', '$10.99', 'https://m.media-amazon.com/images/I/51EWovYcRYS.AC_UY218_.jpg'), ('Wireless Gaming Mouse- USB Cordless PC Computer Mice with LED Blue Backlit, Ergonomic Silent Gamer Laptop Mouse with 7 Silent Click Buttons, 5 Adjustable DPI Plug & Play for PC, Windows, Mac', '4.5 out of 5 stars', '603', '$15.99',
        'https://m.media-amazon.com/images/I/61lF-CvIfDL._AC_UY218_.jpg'), ('Wireless Mouse, TECKNET Pro 2.4G Ergonomic Wireless Optical Mouse with USB Nano Receiver for Laptop,PC,Computer,Chromebook,Notebook,6 Buttons,24 Months Battery Life, 2600 DPI, 5 Adjustment Levels', '4.5 out of 5 stars', '48,424', '$11.99', 'https://m.media-amazon.com/images/I/61Xl9zQcfBL._AC_UY218_.jpg')]
    headers = {
        'authority': 'scrapeme.live',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
    search = request.form.get("search")
    url = 'https://www.amazon.com/s?k='+search.strip()
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    print(soup)
    first_list = list()

    for post in soup.find_all("div", {"class":"a-section"}):
        title = post.find("span", {"class": "a-size-medium a-color-base a-text-normal"})
        rate = post.find("span", {"class": "a-icon-alt"})
        review = post.find("span", {"class": "a-size-base s-underline-text"})
        price = post.find("span", {"class": "a-offscreen"})
        img = post.find("img", {"class": "s-image"})
        if (img is not None):
            img_link = img['src']
        if (title is not None) and (rate is not None) and (review is not None) and (price is not None) and (img_link is not None):
            first_list.append((title.text, rate.text, review.text, price.text, img_link))

    final_list = list()
    for item in first_list:
        if item not in final_list:
            final_list.append(item)

    if(len(final_list) == 0):
        final_list = example_list1
    
    return render_template('index.html', search = search, final_list = final_list)