import random
import sys
import os
'''

def random_number_of_keg_from_bag():
    """Генерируется рандомное число от 1 до 90,
       обозначающее бочонок из мешка"""
    return random.randint(1, 90)


def numbers_on_cards():
    """Генеируется список из 15 рандомных чисел от 1 до 90
       Возвращает отсортированный список.
       Обозначает карточку.
    """
    numbers_on_card = []
    for i in range(1, 16):
        random_number = random_number_of_keg_from_bag()
        if random_number in numbers_on_card:
            numbers_on_card.append(random_number_of_keg_from_bag())
        elif random_number not in numbers_on_card:
            numbers_on_card.append(random_number)
    return sorted(numbers_on_card)


def line_of_card(line):
    """Выполняет встроенную функцию 4 раза
       line - список из 5 цифр
       Возвращает список с вставленными в него ' ' в рандоном порядке
    """
    def insert_blank(line_with_blank):
        """Вставляет ' ' в список с рандомным индексом от 0 до 10"""
        i = random.randint(0, 10)
        for _ in range(1):
            line_with_blank.insert(i, ' ')
        return line_with_blank

    for _ in range(4):
        insert_blank(line)
    return line


def print_card(line_of_cards):
    """Объединяет список с помощью ' ' и возвращает строку
       line_of_cards - список с ' ' внутри
    """
    for i in range(len(line_of_cards), 10):
        string = ' '
        return string.join(map(str, line_of_cards))


def check_of_com_win(card):
    """Функция проверяет не победил ли компьютер"""
    for _ in card:
        if card.count('-') == 5:
            print('Computer win!')
            print('--Карточка компьютера---\n',
                  print_card(first_line_com), '\n',
                  print_card(second_line_com), '\n',
                  print_card(third_line_com), '\n'
                  '--------------------------')
            sys.exit()


def check_of_player_win(card):
    """Функция проверяет не победил ли игрок"""
    for _ in card:
        if card.count('-') == 5:
            print('You win!')
            print('------Ваша карточка-----\n',
                  print_card(first_line_player), '\n',
                  print_card(second_line_player), '\n',
                  print_card(third_line_player), '\n'
                  '--------------------------')
            sys.exit()


def cross_out(line, random_keg):
    index = line.index(random_keg)
    line[index] = '-'


def game():
    """Игра"""
    try:
        random_keg = random_number_of_keg_from_bag()
        if random_keg in kegs_in_bag:
            kegs_in_bag.remove(random_keg)
            print('Новый бочонок - {} (осталось {})'.format(random_keg, len(kegs_in_bag)))
            print('------Ваша карточка-----\n',
                  print_card(first_line_player), '\n',
                  print_card(second_line_player), '\n',
                  print_card(third_line_player), '\n'
                  '--------------------------')
            print('--Карточка компьютера---\n',
                  print_card(first_line_com), '\n',
                  print_card(second_line_com), '\n',
                  print_card(third_line_com), '\n'
                  '--------------------------')

            if random_keg in first_line_com:
                cross_out(first_line_com, random_keg)
            elif random_keg in second_line_com:
                cross_out(second_line_com, random_keg)
            elif random_keg in third_line_com:
                cross_out(third_line_com, random_keg)
            elif random_keg not in kegs_in_card_com:
                pass
            commands = input('Зачеркнуть цифру? (y/n) - ')
            if commands == 'y':
                if random_keg in first_line_player:
                    cross_out(first_line_player, random_keg)
                elif random_keg in second_line_player:
                    cross_out(second_line_player, random_keg)
                elif random_keg in third_line_player:
                    cross_out(third_line_player, random_keg)
                elif random_keg not in first_line_player or random_keg not in second_line_player \
                        or random_keg not in third_line_player:
                    print('Вы проиграли!')
                    sys.exit()
            elif commands == 'n':
                if random_keg in first_line_player or random_keg in second_line_player \
                        or random_keg in third_line_player:
                    print('Вы проиграли!')
                    sys.exit()
                else:
                    pass
            elif commands == 'q':
                print('До свидания!')
                sys.exit()
            check_of_player_win(first_line_player)
            check_of_player_win(second_line_player)
            check_of_player_win(third_line_player)
            check_of_com_win(first_line_com)
            check_of_com_win(second_line_com)
            check_of_com_win(third_line_com)
        elif random_keg not in kegs_in_bag:
            pass
        os.system('cls' if os.name == 'nt' else 'clear')
    except ValueError:
        print('Бочонок уже доставали')


def main(command):
    """Меню игры
       Принимает две команды.
    """
    if command.lower() == 'y'.lower():
        game()
    elif command.lower() == 'n'.lower():
        print('До свидания!')
        sys.exit()
    else:
        print('Команда неизвестна, попробуйте ещё раз')
        second_chance = input('Начать игру? Y/N - ')
        main(second_chance)


kegs_in_bag = [x for x in range(1, 91)]

kegs_in_card = numbers_on_cards()

one_line = print_card(line_of_card(kegs_in_card[0:5]))

kegs_in_card_com = numbers_on_cards()

first_line_player = line_of_card((kegs_in_card[0:5]))
second_line_player = line_of_card(kegs_in_card[5:10])
third_line_player = line_of_card(kegs_in_card[10:16])

first_line_com = line_of_card((kegs_in_card_com[0:5]))
second_line_com = line_of_card(kegs_in_card_com[5:10])
third_line_com = line_of_card(kegs_in_card_com[10:16])

try:
    start_game = input('Начать игру? Y/N - ')
    while True:
        main(start_game)
except KeyboardInterrupt:
    print('You exit')
'''