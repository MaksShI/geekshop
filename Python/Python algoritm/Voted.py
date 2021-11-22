voted = {}


def check_voter(name):

    if voted.get(name):
        print('Выгнать егo!!')
    else:
        voted[name] = True
        print('Допустить к голосованию.')


check_voter('Ivan')
check_voter('Ivan')
check_voter('Sania')
