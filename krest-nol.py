field = [[" "] * 3 for i in range(3)]


def space():
    print(f"  0 1 2")
    print(f"0 {field[0][0]} {field[0][1]} {field[0][2]}")
    print(f"1 {field[1][0]} {field[1][1]} {field[1][2]}")
    print(f"2 {field[2][0]} {field[2][1]} {field[2][2]}")


def ask():
    while True:
        dots = input("Введите координаты, где первое число - это вертикаль, а вторая - горизонталь").split()
        if len(dots) != 2:
            print("Координаты введены неверно!")
            continue
        x, y = dots
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне поля!")
            continue

        if field[x][y] != " ":
            print("Эта клетка занята!!!")
            continue
        return x, y





def Game():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for check in win:
        num = []

        for c in check:
            num.append(field[c[0]][c[1]])
        if num == ["X", "X", "X"]:
            print("Выйграли Крестики!")
            return True
        if num == ["O", "O", "O"]:
            print("Выйграли Нолики!")
            return True
    return False

turn = 0
while True:
    turn += 1
    space()
    if turn % 2 == 1:
        print(f"Ход крестиков")
    else:
        print(f"Ход ноликов")
    x, y = ask()

    if turn % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"
    if Game():
        break
    if turn == 9:
        print("Ничья")
        break
