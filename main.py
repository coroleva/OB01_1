class Warrior():
    def __init__(self, name, power, endurence, hair_color):
        self.name = name
        self.power = power
        self.endurence = endurence
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} is sleeping')
        self.endurence +=2
        self.info(self.endurence)

    def eat(self):
        print(f'{self.name} is eating')
        self.power+=1
        self.info(self.power)

    def attack(self):
        print(f'{self.name} is attacking')
        self.endurence -=6
        self.info(self.endurence)

    def walk(self):
        print(f'{self.name} is walking')
        self.endurence -=1
        self.info(self.endurence)

    def info(self,sign):
        if sign == self.name:
            print(f'имя воина {sign}')
        if sign == self.power:
            print(f'сила воина {sign}')
        if sign == self.endurence:
            print(f'выносливость воина {sign}')
        if sign == self.hair_color:
            print(f'цвет волос воина {sign}')


war1 = Warrior('Степа', 10, 10, 'black')

war1.sleep()
war1.eat()
war1.attack()
war1.walk()



