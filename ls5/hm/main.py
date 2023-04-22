# Cycles

N, S = 1000, 0 
for i in range(1, N+1): 
    if i%3 == 0 or i%5 == 0 or i%7 == 0: 
        S += i 

print(S)
