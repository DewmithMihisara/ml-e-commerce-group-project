class Product:

    # Product class initialization
    def __init__(self, name, price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # get product details
    def get_details(self):
        return f"Product : {self.name} , Price : {self.price} , Quantity : {self.quantity}"
    
    # update product price
    def update_price(self, new_price):
        self.prce = new_price
    
    #update product quantity
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity