from order import Order
from product import Product
from customer import Customer

#Create products
product1 = Product("Laptop", 11000, 5)
product2 = Product("Mouse", 3000, 10)

#create customer
customer1 = Customer("Theekshana Buddhika","Rajgama Junction Rajgama","94763918511")

#create order
order1 = Order(customer1)
order1.add_product(product1)
order1.add_product(product2)

#calculate and print total
total = order1.calculate_total()

#Output: order Total
print(f"Order Total : Rs{total}")

#generate and print order summary
print(order1.generate_summary())