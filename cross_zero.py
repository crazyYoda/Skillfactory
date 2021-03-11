ef begin():      # функция начальной заставки
    print("           CROSS & ZERO  ")
    print("            это война   ")
    print()
    print("   Ходы выполняются по координатам")
    print("в формате X Y, где Х-строка; Y-столбец")

def game_field():     # рисуем игровое поле
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        print(f"  {i} | {' | '.join(row)} | ")
        print("  --------------- ")
    print()

def input_cords():      #получение и обработка координат хода
    while True:
        cords = input().split()
        
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or  0 > y or  y > 2 :
            print(" Координаты вне диапазона! ")
            continue
        
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue
        
        return x, y
        
        
def check_win():     #функция проверки выигрышных комбинаций
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Игра окончена. Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Игра окончена. Выиграл 0!!!")
            return True
    return False



begin()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    game_field()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    
    x, y = input_cords()
    
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    
    if check_win():
        break
    
    if count == 9:
        game_field()
        print(" Игра окончена. Ничья!")
        break

    © 2021 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Docs

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About


