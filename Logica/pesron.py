from time import sleep

class Hero():
    def __init__(self, name, health, armor, power):
        self.name = name
        self.health = health #число
        self.armor = armor #рядок
        self.power = power

    def print_info(self):
        print('Рівень здоров\'я:', self.health)
        print('Клас броні:', self.armor, '\n')


class Warrior(Hero):
    def hello(self):
        print(f'Привет! Меня зовут {self.name}!')

    def attack(self, other):
        print(f'{self.name} атакует {other.name} c силой {self.power}')
        other.print_info()
        if other.armor <= 0:
            other.health -= self.power
        else:
            other.armor -= self.power


class Magican(Hero):
    def hello(self):
        print(f'Привет! Меня зовут {self.name}!')

    def attack(self, other):
        print(f'{self.name} атакует {other.name} c силой {self.power}')
        other.print_info()
        if other.armor <= 0:
            other.health -= self.power
        else:
            other.armor -= self.power


warrior = Warrior('Richard the Lion heart', 80, 20, 15)
magican = Magican('Gandulf Grey', 50, 0, 30)

warrior.hello()
magican.hello()

while True:
    warrior.attack(magican)
    if magican.health <= 0:
        print(f'{magican.name} погиб')
        break
    sleep(1)

    magican.attack(warrior)
    if warrior.health <= 0:
        print(f'{warrior.name} погиб')
        break
    sleep(1)

print('Game over!')