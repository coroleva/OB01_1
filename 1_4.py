class Task:
    def __init__(self, name,description, deadline, status):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = False

    def done(self):
        self.status = True

    def info(self):
        print(f'Задача: {self.name} *** Описание: {self.description} ***Дедлайн: {self.deadline} *** Статус: {self.status}')

list1 = []

while True:
    print('1. Добавить задачу')
    print('2. Изменить статус задачи')
    print('3. Вывести список задач')
    print('4. Выход')
    choice = int(input('Выберите действие: '))

    if choice == 1:
        name = input('Название задачи: ')
        description = input('Описание задачи: ')
        deadline = input('Дедлайн задачи: ')
        task = Task(name, description, deadline, False)
        list1.append(task)

    elif choice == 2:
        name = input('Название задачи: ')
        for task in list1:
            if task.name == name:
                task.done()

    elif choice == 3:
        for task in list1:
            task.info()

    elif choice == 4:
        break
    else:
        print('Такого действия нет')
