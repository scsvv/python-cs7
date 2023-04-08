num = input("Enter day: ")
days = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")

try: 
    num = int(num)
except: 
    print("Err 1: Invalid data in field (1 - 7)")
    exit()

if num <= 0 or num >=8:
    print(f"Err 2: Data should be in 1 - 7, not {num}")
elif num <=5: 
    print(f"{days[num-1]}: Будний день")
else: 
    print(f"{days[num-1]}: Выходной")