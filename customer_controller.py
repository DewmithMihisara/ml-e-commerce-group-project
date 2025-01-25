from customer import Customer

continue_loop = True

while(continue_loop) : 
    print ("Let's create a customer ! :)")

    customer_name = input("Enter customer Name : ")
    customer_address = input("Enter customer address : ")
    customer_contact = input("Enter customer contact : ")

    # Create the customer 
    customer = Customer(customer_name , customer_address , customer_contact)
    print("Customer Created ! ")
    print(customer.get_details())

    continue_forward = input("Continue to add ? (if yes enter y otherwise n) : ")

    if continue_forward == "n" : 
        continue_loop = False

