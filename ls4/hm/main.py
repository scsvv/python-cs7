hour = input()

try: 
    hour = int(hour)
except: 
    print(f"Error 1: Invalid data. {hour} is {type(hour)} not int")
    exit()

if hour < 0 or hour >= 24: 
    print(f"Error 2: Invalid data. {hour} isn't work interval: (0 - 23)")
elif hour == 23 or hour < 5: 
    print(f" Night: {hour} hour")
elif hour >= 5 and hour < 12:
    print(f" Morning: {hour} hour")
elif hour >= 12 and hour < 18:
    print(f" Day: {hour} hour")
elif hour >= 18 and hour < 23:
    print(f" Evening: {hour} hour")
else: 
    print("Error: unknown error")

