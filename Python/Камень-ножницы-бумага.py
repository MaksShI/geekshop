import time


while True:
    player_1 = str(input("Игрок 1 , введите словами (камень-ножницы-бумага), или quit чтобы выйти:  "))
    print("Передайте контроль другому игроку!")
    time.sleep(5)
    player_2 = str(input("Игрок 2 , введите словами (камень-ножницы-бумага), или quit чтобы выйти:  "))
    player_1 = player_1.lower()
    player_2 = player_2.lower()
    if player_1 == "ножницы" and player_2 == "бумага":
        print("Победил Игрок 1")
    elif player_2 == "ножницы" and player_1 == "бумага":
        print("Победил Игрок 2")
    elif player_1 == "камень" and player_2 == "бумага":
        print("Победил Игрок 2")
    elif player_2 == "камень" and player_1 == "бумага":
        print("Победил Игрок 1")
    elif player_1 == "камень" and player_2 == "ножницы":
        print("Победил Игрок 1")
    elif player_2 == "камень" and player_1 == "ножницы":
        print("Победил Игрок 2")
    elif player_2 == "quit" or player_1 == "quit":
        break
    else:
        print("Ничья!")