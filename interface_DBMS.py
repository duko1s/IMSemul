"""
Интерфейс взаимодействия с пользователем
на самом верхнем уровне ИБД
список команд ограничен созданием корня БД, просмотром списка, архивирование и восстановление, выбор БД для работы.
При выборе БД запускается интерфейс выбранной БД
"""

import cmd
import dbms
import shutil
import os
from interface_DB import IBDShell

class DBMSShell(cmd.Cmd):
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
        "выбор базы данных (проекта): обязательно указать номер выбираемого проекта (БД)"
        roots = dbms.Roots()
        if len(roots) == 0:
            print("Проектов (баз данных) нет, нечего выбирать!")
        elif arg.isdigit():
            index = int(arg)
            if 1 <= index <= len(roots):
                roots.select(index)
            else:
                print(f"ВВедите индекс от 1 до {len(roots)}")
        else:
            print(f"ВВедите индекс от 1 до {len(roots)}, только число!")

    def do_unselect(self, arg):
        "снять выделение активного проекта: без аргументов"
        roots = dbms.Roots()
        roots.current = None
        roots.save()

    def do_backup(self, arg):
        'создать бэкап баз данных: указать имя архива без расширения'
        if arg:
            output_filename = arg
            dir_name = dbms.Roots.db_path_name
            shutil.make_archive(output_filename, 'zip', dir_name)
        else:
            print("укажите имя архива!")

    def do_restore(self, arg):
        'востановить базы данных: указать имя архива'
        if arg:
            try:
                shutil.unpack_archive(arg, dbms.Roots.db_path_name)
            except:
                print("убедитесь в правильности имени архива!")
    
    def do_list_backup(self, arg):
        'показать список архивов: без аргументов'
        for file_name in os.listdir('.'):
            if file_name.endswith('.zip'):
                print(file_name)

    def do_use(self, arg):
        "Переход в базу данных: предварительно выбрать базу данных командой select"
        roots = dbms.Roots()
        if roots.current:
            IBDShell(roots.use()).cmdloop()
        else:
            print("Необходимо сначала выбрать базу данных")


    def do_quit(self, arg):
        'Выход из программы'
        print('До свидания!!')
        return True

if __name__ == '__main__':
    IBDShell().cmdloop()