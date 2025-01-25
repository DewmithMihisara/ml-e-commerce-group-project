
from product import Product

print("Product Controller")

product = None

isContinue = True
while isContinue:
    print("\na. Create a product object")
    print("b. Update the price of the product")

    choice =input("\nEnter your choice: ")

    if(choice == 'a'):
        name = input("Enter the name of the product: ")
        price = int(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity of the product: "))
        product = Product(name, price, quantity)
        print(product.get_details())

    elif(choice == 'b'):
        if product is not None:
            new_price = int(input("Enter the new price of the product: "))
            product.update_price(new_price)
            print(product.get_details())
        else:
            print("Product not created")

    else:
        print("Invalid choice")

    isContinue = input("Do you want to continue? (y/n): ") == 'y'
