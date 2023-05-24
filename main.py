class Todo:
    menu = {'1': 'Добавить дело', '2': 'Список всех дел', '3': 'Найти дело', '4': 'Выполнить дело',
            '5': 'Повторить дело', '6':'Выйти'}

    def __init__(self):
        self.todo_items = []

    def add_todo(self, items):

        self.todo_items.append(items)
        print("Задача успешно добавлена.")

    def list(self):
        print("список дел")
        for item in self.todo_items:
            print(str(item.counter) + ' . ' + item.name + " . " + format(item.is_done))
        print()

    def find(self, name_find):
        return ((item.counter, item.name) for item in self.todo_items if item.name.find(name_find) != -1)

    def run(self):

        while True:

            print("Меню:")
            for key, val in Todo.menu.items():
                print(key + '.' + val, end='\n')

            command = input("Введите цифру из меню:")

            # '1' :'Добавить дело'
            if command == '1':

                name_Todo = input("какое дело? ")  # запрашиваем у пользователя название задачи
                new_Todo = TodoItem(name_Todo)  #

                self.add_todo(new_Todo)

            # '2' :'Список всех дел'
            elif command == '2':
                self.list()

            # '3' :'Найти дело'
            elif command == '3':
                key_word = input("введите ключевое слово:")  # запрашиваю имя у пользователя
                find = self.find(key_word)
                for counter, val in find:
                    print(str(counter) + '.' + val)
            # '4' :'Выполнить дело'
            elif command == '4':

                number_todo = int(input("введите номер задачи"))

                for item in self.todo_items:  # ищем номер задачи
                    if item.counter == number_todo:
                        item.cheсk()
                        print("задача выполнена")
                        break
                else:
                    print("задача {number_todo} не найдена")

            # '5' :'Повторить дело'
            elif command == '5':
                number_todo = int(input("введите номер задачи для повторения:"))

                for item in self.todo_items:  # ищем номер задачи
                    if item.counter == number_todo:
                        item.uncheck()
                        print(f"задача {number_todo} успешно повторена")
                        break
                else:
                    print(f"задача {number_todo} не найдена")


            # '6' :'Выйти'
            elif command == '6':
                print("Программа завершена")
                break


class TodoItem:
    counter_do = 0

    def __init__(self, new_do):
        self.is_done = "не выполнено"
        self.name = new_do

        TodoItem.counter_do += 1
        self.counter = TodoItem.counter_do

    def cheсk(self):
        self.is_done = "выполнено"

    def uncheck(self):
        self.is_done = "не выполнено"


if __name__ == '__main__':
    todo = Todo()
    todo.run()