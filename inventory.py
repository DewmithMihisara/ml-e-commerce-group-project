<<<<<<< HEAD
from product import Product

class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product
    
    def remove_product(self, product_name , quantity):
        if product_name in self.products:
            if self.products[product_name].quantity >= quantity:
                self.products[product_name].quantity -= quantity
            else:
                print(f"Insufficeint stock for {product_name}")
        else:
            print(f"product : ' {product_name} ' is not available in inventory")
            
    def check_status(self, product_name):
        if product_name in self.products:
            return self.products[product_name].quantity
        else:
            return
=======
# Inventory Management

# 1. Track product stock level
# 2. Update stock after order fulfilment
>>>>>>> 55d017c5165cc9f949821a3ad026330d12a7d735
