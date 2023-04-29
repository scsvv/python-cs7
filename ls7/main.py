from random import randint 

numbers_list = list()
list_len = randint(5, 6);
list_sum = 0 

for i in range(list_len):
    numbers_list.append(randint(0, 200))

print(numbers_list)
print(f"sum: {sum(numbers_list)}")

for number in numbers_list:
    if numbers_list.count(number) > 1: 
        continue    
    
    list_sum += number

print(f"Own sum equal: {list_sum}" )
# ДЗ СПИСОК ДОЛЖЕН СОДЕРЖАТЬ УНИКАЛЬНЫЕ ЗНАЧЕНИЯ
for i in range(list_len): 
    _value, _index = numbers_list[i], i
    for j in range(i + 1, list_len):
        if _value > numbers_list[j]:
            _value, _index = numbers_list[j], j
    else:
        numbers_list[i], numbers_list[_index] = numbers_list[_index], numbers_list[i]

print(numbers_list)

number_tuple = ("Nike", 13.2)

name, price = number_tuple
print(name, price)
