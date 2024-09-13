class Warrior():
    def __init__(self, name, power, endurence, hair_color):
        self.name = name
        self.power = power
        self.endurence = endurence
        self.hair_color = hair_color

    def sleeep(self):
        print(f'{self.name} is sleeping')
        self.endurence +=2

    def eat(self):
        print(f'{self.name} is eating')
        self.power+=1

    def attack(self):
        print(f'{self.name} is attacking')
        self.endurence -=6

    def walk(self):
        print(f'{self.name} is walking')
        self.endurence -=1
    def info(self):
        print(f'имя воина {self.name}, \n'
              f' сила воина {self.power}, \n'
              f'выносливость воина {self.endurence}, \n'
              f'цвет волос воина {self.hair_color}')