# OB01_1

### 1_2 Класс Contact:
Представляет отдельный контакт с полями: имя (name), телефон (phone), и email (email).
  - Метод info() выводит информацию о контакте в формате: "имя: {имя} - телефон: {телефон} - email: {email}".
- Класс Book_contact:
Хранит список контактов в виде пустого списка book, который можно пополнять объектами класса Contact.
  - Методы:
    - add_contact(name, phone, email): добавляет новый контакт в книгу контактов, создавая объект класса Contact и добавляя его в список.
    - del_contact(name): удаляет контакт из книги по имени. Если найден контакт с заданным именем, он удаляется из списка, и выводится сообщение об успешном удалении.
    - search_contact(name): ищет контакт по имени и выводит информацию о нем с помощью метода info().
    - show_all(): выводит информацию обо всех контактах в книге.
    - 
Пример использования:

Создается объект книги контактов book.
Добавляются три контакта: Вася, Петя и Коля.
Метод show_all() выводит информацию обо всех контактах (Вася, Петя, Коля).
Метод search_contact('Вася') ищет и выводит информацию о Васе.
Метод del_contact('Петя') удаляет Петра из книги контактов.
После удаления, вызов show_all() выводит оставшихся контактов (Вася и Коля).
Таким образом, это базовый пример контактной книги с добавлением, удалением, поиском и отображением всех контактов.


### 1_3 Класс Account:

При инициализации создается объект счета с уникальным id и начальным балансом, который равен 0.
В конструкторе отображается сообщение о создании счета и выводится информация о балансе через метод info().

Методы класса:
- add_balance(self, amount): увеличивает баланс на указанную сумму и выводит обновленную информацию о балансе.
- withdraw(self, amount): уменьшает баланс на указанную сумму, если достаточно средств, и сообщает об успешном списании или недостатке средств.
- info(self): выводит текущий баланс счета.
- 
Основная логика программы:
Пользователю задается вопрос, хочет ли он создать счет. Если ответ положительный, создается объект класса Account с уникальным идентификатором (случайное число от 1000 до 9999) и начальным балансом 0. Если ответ отрицательный, программа завершает работу с сообщением "До свидания".
Меню действий:

После создания счета запускается цикл, который отображает меню с выбором действия:
Пополнить счет: Пользователь вводит сумму, и баланс увеличивается на эту сумму.
Снять деньги со счета: Пользователь вводит сумму, которую хочет снять, и если на счете достаточно средств, баланс уменьшается на эту сумму.
Посмотреть баланс: Отображает текущий баланс счета.
Выход: Завершает работу программы.
Обработка ввода:

Программа запрашивает действие у пользователя в виде числа (1–4) и выполняет соответствующее действие.
Если пользователь вводит неправильное число, программа выводит сообщение о недопустимом действии.
Таким образом, этот код имитирует взаимодействие с банковским счетом: можно создать счет, пополнять баланс, снимать деньги и проверять состояние счета.

### 1_4 Класс Task:

Класс представляет собой шаблон для создания задач.
- У каждой задачи есть 4 свойства: name (название), description (описание), deadline (дедлайн), и status (статус выполнения).

При создании задачи статус автоматически устанавливается как False, то есть задача не выполнена.
- Метод done() изменяет статус задачи на True (выполнено).
- Метод info() выводит информацию о задаче: её название, описание, дедлайн и статус.

- Список list1:

Это список, в который добавляются все созданные задачи.
Бесконечный цикл while True:

Программа работает в бесконечном цикле, предлагая пользователю выбрать одно из четырёх действий: добавить задачу, изменить статус задачи, вывести список задач или выйти из программы.
Добавление задачи (опция 1):

Пользователю предлагается ввести название, описание и дедлайн задачи.
После этого создаётся новый объект класса Task и добавляется в список list1.
Изменение статуса задачи (опция 2):

Пользователь вводит название задачи, статус которой нужно изменить.
Программа находит задачу в списке и вызывает метод done(), изменяющий её статус на выполненную.
Вывод списка задач (опция 3):

Программа выводит информацию обо всех задачах в списке, используя метод info() каждого объекта.
Выход из программы (опция 4):

Если пользователь выбирает этот пункт, программа завершает работу.
Обработка неверного выбора:

Если пользователь выбирает номер, не соответствующий ни одному из действий, программа выводит сообщение об ошибке.
Таким образом, программа предоставляет простой способ управления задачами в текстовом режиме.

 
