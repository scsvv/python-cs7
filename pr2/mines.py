from random import randint
N, M, MINES, field = 9, 9, 9, list()

def field_print(_field):
    for _f in _field:
        str_f = ""
        for _fr in _f:
            str_f += f"{_fr} " 
        print(str_f)



for i in range(N):
    field.append([])
    for j in range(M):
        field[i].append('#')


while MINES > 0:
    x, y = randint(1, N - 2), randint(1, M - 2)

    if field[x][y] != "*":
        field[x][y] = "*"
        MINES -= 1
        if (x != 0 and y != 0) and (x < N-1) and (y < M-1):
            _x = x - 1
            while _x < x+2:
                _y = y - 1
                while _y < y+2:
                    if field[_x][_y] == "#":
                        field[_x][_y] = 1
                    elif field[_x][_y] != "*":
                        field[_x][_y] += 1
                    _y += 1
                _x += 1
    else: 
        continue



field_print(field)