x = input("x = ")
y = 10 

try: 
    x = int(x)
    print("All is good")
except:
    x = 0
    print("All is going bad")

print(x+y)