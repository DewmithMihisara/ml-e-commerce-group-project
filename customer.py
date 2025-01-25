class Customer:
    
    # Customer class initialization
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact

    #get customer details
    def get_details(self):
        return f"name :{self.name}, age : {self.address}, contact : {self.contact}"