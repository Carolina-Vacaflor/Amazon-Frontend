from flask import Flask, render_template, redirect, request, url_for
import products_scraper
from services.product_service import Product_Service

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    return(render_template('home.html'))

@app.route("/results", methods = ['GET', 'POST'])
def results():
    search = request.form.get("search")
    print(search)
    final_list = products_scraper.get_products(search)    
    print(final_list[0].title)
    return render_template('index.html', search = search, final_list = final_list)

@app.route('/track/<string:result_id>', methods = ['GET', 'POST'])
def track(result_id):
    return render_template('form.html')
    # product_service = Product_Service()
    # product_service.setTracking(result_id)
    # return redirect(url_for('tracking'))

@app.route('/tracking', methods = ['GET', 'POST'])
def tracking():
    return render_template('form.html')