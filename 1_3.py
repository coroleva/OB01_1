import random


class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        print(f'Счет создан. Ваш ID: {self.id}')
        self.info()
    def add_balance(self, amount):
        self.balance += amount
        print('Баланс пополнен')
        self.info()
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print('Списание проведено')
        else:
            print('Недостаточно средств')
        self.info()
    def info(self):
        print(f'Ваш баланс: {self.balance}')


question = input('Вы хотите создать счет? ').lower()
if question == 'да':
    a = Account(random.randint(1000, 9999), 0)
else:
    print('До свидания')


while True:
    print('1. Пополнить счет')
    print('2. Снять деньги со счета')
    print('3. Посмотреть баланс')
    print('4. Выход')
    choice = int(input('Выберите действие: '))

    if choice == 1:
        amount = int(input('Сколько вы хотите пополнить? '))
        a.add_balance(amount)
    elif choice == 2:
        amount = int(input('Сколько вы хотите снять? '))
        a.withdraw(amount)
    elif choice == 3:
        a.info()
    elif choice == 4:
        break
    else:
        print('Такого действия нет')