class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


    def info(self):
        print(f'имя: {self.name} - телефон: {self.phone} - email: {self.email}')


class Book_contact():
    def __init__(self):
        self.book = []

    def add_contact(self, name, phone, email):
        self.book.append(Contact(name, phone, email))

    def del_contact(self, name):
        for i in self.book:
            if i.name == name:
                self.book.remove(i)
                print(f'{name} удален из книги контактов')

    def search_contact(self, name):
        for i in self.book:
            if i.name == name:
                print('Информация о контакте:')
                print(i.info())

    def show_all(self):
        for i in self.book:
            print(i.info())


book = Book_contact()
book.add_contact('Вася', '123456789', 'a@a.com')
book.add_contact('Петя', '987654321', 'b@b.com')
book.add_contact('Коля', '555555555', 'c@c.com')

book.show_all() # Вася, Петя, Коля

book.search_contact('Вася') # Вася - телефон: 123456789 - email: a@a.com

book.del_contact('Петя')
book.show_all() # Вася, Коля