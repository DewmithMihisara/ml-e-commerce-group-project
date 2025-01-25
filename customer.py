class Customer:
    
    # Customer class initialization
    def __init__(self, name, address, contact):
        self.name = name
        self.age = address
        self.contact = contact

    #get customer details
    def get_details(self):
        return f"name :{self.name}, age : {self.age}, contact : {self.contact}"