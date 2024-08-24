animal = "ceBolla MarIna"
print(animal.capitalize())  # Cebolla marina
print(animal.upper())  # CEBOLLA MARINA
print(animal.lower())  # cebolla marina
print(animal.title())  # Cebolla Marina
print(animal.strip().capitalize())  # Cebolla marina
print(animal.swapcase())  # CEbOLLA mARiNA
print(animal.casefold())  # cebolla marina
print(animal.count("a"))  # 4
print(animal.find("a"))  # 3
print(animal.rfind("a"))  # 12
print(animal.index("a"))  # 3
print(animal.rindex("a"))  # 12
print(animal.replace("a", "o"))  # ceBollo Mornin
print(animal.split(" "))  # ['ceBolla', 'MarIna']
print("Bo" in animal)  # True
print("Bo" not in animal)  # False
