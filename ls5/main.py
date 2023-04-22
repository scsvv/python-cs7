from random import randint
"""
N = int(input("Enter number: "))
K = int(input("Enter number: "))  
for i in range(N+1):
    print(i)

for i in range(N, K-1, -1):
    print(i)
counter = 0
while counter < 1000:
    print(counter)
    counter+=1 
"""
MINES_COUNT = 10
field = ""
for i in range(9):
    for j in range(9):
        field += "#"
    field+="\n"

print(field)



