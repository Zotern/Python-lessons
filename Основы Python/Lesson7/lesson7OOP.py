import random
import sys
import os

# TODO Игровой движок - создание  лотерейных билетов, за выбор следующего бочонка
# за определение победителя


class Card:
    def __init__(self):
        self.numbers_on_card = []

        for i in range(1, 90):
            self.random_number = random.randrange(1, 90)
            for j in range(0, 15):
                if self.random_number not in self.numbers_on_card:
                    self.numbers_on_card.append(self.random_number)
            if len(self.numbers_on_card) == 15:
                break

        self.numbers_on_card = sorted(self.numbers_on_card)

    def show(self, name_of_card):
        if name_of_card == 'Карточка компьютера':
            print('----{}---\n'.format(name_of_card),
                  self.print_card(self.numbers_on_card[0:5]), '\n',
                  self.print_card(self.numbers_on_card[5:10]), '\n',
                  self.print_card(self.numbers_on_card[10:16]), '\n'
                  '--------------------------')
        elif name_of_card == 'Ваша карточка':
            print('-------{}------\n'.format(name_of_card),
                  self.print_card(self.numbers_on_card[0:5]), '\n',
                  self.print_card(self.numbers_on_card[5:10]), '\n',
                  self.print_card(self.numbers_on_card[10:16]), '\n'
                  '--------------------------')

    @staticmethod
    def print_card(line_of_cards):
        """
        """
        for _ in range(4):
            i = random.randint(0, 10)
            for _ in range(1):
                line_of_cards.insert(i, ' ')

        for i in range(len(line_of_cards), 10):
            string = ' '
            return string.join(map(str, line_of_cards))


class Keg:
    def __init__(self):
        self.random_keg = random.randrange(1, 90)

    def show_keg(self):
        print(self.random_keg)


class Bag(Keg):
    def __init__(self):
        super().__init__()
        self.kegs_in_bag = [x for x in range(1, 91)]

    def remove_keg(self, random_keg):
        if random_keg in self.kegs_in_bag:
            self.kegs_in_bag.remove(random_keg)


class Player(Card):
    def __init__(self):
        super().__init__()

    @staticmethod
    def cross_out(command, keg, card):
        if command == 'y':
            if keg in card:
                index = card.index(keg)
                card[index] = '-'
            elif keg not in card:
                print('Вы проиграли!')
                sys.exit()
        elif command == 'n':
            if keg in card:
                print('Вы проиграли!')
                sys.exit()
            else:
                pass
        elif command == 'q':
            print('До свидания!')
            sys.exit()

    @staticmethod
    def check_of_win(card):
        for _ in card:
            if card.count('-') == 15:
                print("You win!")
                sys.exit()


class Computer(Card):
    def __init__(self):
        super().__init__()

    @staticmethod
    def cross_out_com(keg, card):
        if keg in card:
            index = card.index(keg)
            card[index] = '-'
            return card

    @staticmethod
    def check_of_win(card):
        for _ in card:
            if card.count('-') == 15:
                print("Computer win!")
                sys.exit()


class Game(Player, Computer, Bag):
    def __init__(self):
        super(Player, self).__init__()
        super(Computer, self).__init__()
        super(Bag, self).__init__()
        player = Player()
        computer = Computer()
        bag = Bag()

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            keg = Keg()
            if keg.random_keg in bag.kegs_in_bag:
                bag.remove_keg(keg.random_keg)
                print('Новый бочонок - {} (осталось {})'.format(keg.random_keg, len(bag.kegs_in_bag)))
                player.show('Ваша карточка')
                computer.show('Карточка компьютера')
                computer.cross_out_com(keg.random_keg, computer.numbers_on_card)
                commands = input('Зачеркнуть цифру? (y/n) - ')
                player.cross_out(commands, keg.random_keg, player.numbers_on_card)
                player.check_of_win(player.numbers_on_card)
                computer.check_of_win(computer.numbers_on_card)
                os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    game = Game()
