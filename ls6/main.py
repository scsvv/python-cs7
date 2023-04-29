# Sviatoslav, ONPU, 45, 46, 47, 48
goods = list()

goods = [
            ["Air 22", 125.0], 
            ["Puma Ferrari Shoes", 123.8], 
            ["Puma Shorts", 156.9], 
            ["Puma T-Shirt", 45.7]
            ] # список
print(goods)

goods.append(["Nike Red Bull Suite", 456.9])
goods.append(["Nike McLaren Suite", 456.9])
goods.append(["Nike Alfa Romeo Suite", 456.9])


# goods.append(["Air 23", 500.0])
goods.insert(0, ["Air 23", 500.0])
print(goods)


order = ("Svitoslav", "Odesa, Kanatnaya 34, 6", [0, 3]) # кортеж

print(f"👾 Name: {order[0]}")
print(f"📍 Address: {order[1]}")
print(f"📋 list of orders: ")
for good in order[2]:
    print(f"\t• {goods[good]} ")


