"""
Интерфейс взаимодействия с пользователем
на соответствующем уровне ИБД
список команд зависит от уровня
"""

import cmd
import dbms

class IBDShell(cmd.Cmd):
    intro = 'Эмулятор первой базы данных IMS  введите help или ? чтобы открыть лист команд.\n'
    prompt = '>>> '
    def do_list(self, arg):
        'отобразить список баз данных'
        roots = dbms.Roots()
        roots.list()

    def do_add(self, arg):
        'добавить базу данных: обязательно указать имя и необязательно описание'
        roots = dbms.Roots()
        try:
            roots.add(dbms.Project(arg))
        except NameError as e:
            print(e)
        else:
            print(f"Добавлен новый проект {arg}")

    def do_select(self, arg):
        "выбор базы данных (проекта)"
        roots = dbms.Roots()
        if len(roots) == 0:
            print("Проектов (баз данных) нет, нечего выбирать!")
            return None
        if arg.isdigit():
            index = int(arg)
            if index >= len(roots):
                return roots.select(int(arg))
            else:
                print(f"ВВедите индекс от 1 до {len(roots)}")
                return None
        else:
            print(f"ВВедите индекс от 1 до {len(roots)}, только числовой символ!")
            return None

    def do_save(self, arg):
        'сохранить базу данных'
        print('сохраняет базу данных')

    def do_quit(self, arg):
        'Выход из программы'
        print('До свидания!!')
        return True

if __name__ == '__main__':
    IBDShell().cmdloop()