goods = dict()
K = int(input("Enter quantity of goods: "))
for i in range(K):
    key = input("Enter product name: ")
    value = input("Enter product quantity on stack: ")
    goods[key] = value
print(goods)