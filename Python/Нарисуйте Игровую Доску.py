def hy_wins(Game_State):
    for i in range(0, len(Game_State)):
        if Game_State[i][0] == Game_State[i][1] == Game_State[i][2]:
            print("end")
            print("Player " + str(Game_State[i][1]) + " has won the game")
        else:
            pass


def floor(game, a):
    print(' ___ ' * a)
    while k != a:
        for i in range(0, a):
            if game[0][i] == 1:
                print(' |' + 'x' + '| ')
            else:
                print(' ___ ' * a)
                print(' | | ' * a)

a = int(input('Введите число полей по x^x: '))
k = 0
while a > k:
    k += 1
    print(' ___ ' * a)
    print(' | | ' * a)
print(' ___ ' * a)

game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

while True:
    fis_p = int(input('Введите кординаты x: '))
    p = int(input('Введите кординаты y: '))
    if game[fis_p][p] == 0:
        game[fis_p][p] = 1
    else:
        pass

    floor(game, a)
    Top_H = game[0]
    Mid_H = game[1]
    Bot_H = game[2]
    Left_V = game[0][0], game[1][0], game[2][0]
    Mid_V = game[0][1], game[1][1], game[2][1]
    Right_V = game[0][2], game[1][2], game[2][2]
    Neg_Diag = game[0][0], game[1][1], game[2][2]
    Pos_Diag = game[2][0], game[1][1], game[0][2]

    Game_State = [Top_H, Mid_H, Bot_H, Left_V, Mid_V, Right_V, Neg_Diag, Pos_Diag]
    hy_wins(Game_State)
    sec_p = int(input('Введите кординаты 0: '))
    k = int(input('Введите кординаты y: '))
    if game[fis_p][p] == 0:
        game[fis_p][p] = 2
    else:
        pass

    floor(game, a)
    Top_H = game[0]
    Mid_H = game[1]
    Bot_H = game[2]
    Left_V = game[0][0], game[1][0], game[2][0]
    Mid_V = game[0][1], game[1][1], game[2][1]
    Right_V = game[0][2], game[1][2], game[2][2]
    Neg_Diag = game[0][0], game[1][1], game[2][2]
    Pos_Diag = game[2][0], game[1][1], game[0][2]

    Game_State = [Top_H, Mid_H, Bot_H, Left_V, Mid_V, Right_V, Neg_Diag, Pos_Diag]
    hy_wins(Game_State)
