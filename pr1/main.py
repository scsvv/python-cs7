# Игра в города. Работа со строками и уникальными значениями. 

"""
    Для игры в города () - хранить города, названия должны быть уникальными, каждое новый город имеет первую букву екв. поледней превидущего  
"""

print("""
    It's a city game; 
    For exit write exit
""")

cities = set()
start_letter = None
players = ["", ""]
step = 1

while True: 
    step+=1
    if start_letter is None: 
        players[0] = input("Enter player 1 name: ")
        players[1] = input("Enter player 2 name: ")
        _data = input(f"{players[0]} enter city: ").lower()
        start_letter = _data[len(_data)-1]
        cities.add(_data)
        continue

    _data = input(f"{players[step%2]} enter city. Start from letter {start_letter}: ").lower()
    _data = _data.strip()

    if _data[0] == start_letter: 
        if _data in cities: 
            print(f"Game Over. Win player {players[(step-1)%2]}")
            break    
        start_letter = _data[len(_data)-1]
        cities.add(_data)
    elif _data[0] != start_letter: 
        print(f"Game Over. Win player {players[(step-1)%2]}")
        break
    if _data == "exit":
        break

print(cities)