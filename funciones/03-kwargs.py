def get_product(**kwargs):
    print(kwargs)  # {'name': 'Laptop', 'price': 1000, 'brand': 'Dell'}
    print(kwargs["name"])  # Laptop


get_product(name="Laptop", price=1000, brand="Dell")
