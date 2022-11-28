from repositories.product_repository import Product_Repository

class Product_Service:    
   
    def __init__(self):
        pass

    def store_product(self, product):
        repository = Product_Repository()
        repository.register_product(product)

    def setTracking(self, id):
        repository = Product_Repository()
        repository.updateTracker(1,id)

    def delTracking(self, id):
        repository = Product_Repository()
        repository.updateTracker(0,id)
    
        