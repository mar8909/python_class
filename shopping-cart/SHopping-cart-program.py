# products&prices


products = []
prices = []
total = 0

while True:
    product = input("Enter the product that would you like to add to the cart: Milk / Sugar / Bread (q to quit) ")

    if product.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the ${product}  "))
        products.append(product)
        prices.append(price)

print(" **** Your cart is **** ")
for product in products:
    print(product)

for price in prices:

    total += price

print(f"The total of your cart is $ {total} ")









