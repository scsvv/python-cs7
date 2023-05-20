# Упопрядоченные list tuple set -> deque array queue stack (0-N) 
# Неоупорядоченные 

prices = {
    "apple": 19, 
    "orange": 23, 
    "banana": 21, 
    "paper": 21, 
}

print( prices["orange"] )

f = dict()
g : set = {1, 2, 3, 4} 

student : dict = {
    "fullname": "", 
    "grade": 0, 
    "subjects": {
        "math": [], 
        "ukrainian": [], 
        "physic": [], 

    }
}

student["exam"] = "10"

print(student)

# Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение. Например: 