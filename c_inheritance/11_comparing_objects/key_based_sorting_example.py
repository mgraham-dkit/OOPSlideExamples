from Product import Product

def calc_profit(product):
    return product.calc_profit()

products = []
prod1 = Product("Product 1", 5, 10)
prod2 = Product("Product 2", 3, 10)
prod3 = Product("Product 3", 10, 11)
products.append(prod1)
products.append(prod2)
products.append(prod3)

print(products)
products.sort(key=calc_profit)
print(products)
