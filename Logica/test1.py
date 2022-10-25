from time import sleep

class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.print_info()

    def print_info(self):
        print(f'''Имя: {self.name}\nЗдоровье: {self.health}''')

    def strike(self, enemy):
        print(f'Удар! {self.name} атакует {enemy.name} с силой {self.power}, используя {self.weapon}\n')

        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health -= self.power
            enemy.armor = 0

        print(f'{enemy.name} покачнулся\nКласс его брони упал до {enemy.armor}, а уровень здоровья упал до {enemy.health}')


richard = Hero('Ричард', 50, 25, 20, 'меч')
helen = Hero('Хелен', 100, 5, 5, 'лук')

while True:
    richard.strike(helen)
    helen.strike(richard)
    if richard.health < 0:
        print(f'{richard.name} погиб...')
        break
    elif helen.health < 0:
        print(f'{helen.name}  погиб...')
        break
    sleep(1)