"""
Интерфейс взаимодействия с пользователем
на втором уровне - уровне корня выбранной базы данных (проекта)
список команд ограничен созданием модуля, просмотром списка, ....
"""

import cmd
import dbms
import os

class IBDShell(cmd.Cmd):
    def __init__(self, project):
        cmd.Cmd.__init__(self)
        print(project)
        name = project.name
        description = project.description
        self.prompt = f"{name}>>> "
        self.intro  = f"Добро пожаловать в БД {name}\nДля справки наберите 'help'"
        self.doc_header ="Доступные команды (для справки по конкретной команде наберите 'help _команда_')"

    def do_quit(self, arg):
        "выход в систему управления базами данных."
        return True
    
    def do_list(self, arg):
        "показать список модулей проекта"
        print("вывести список")