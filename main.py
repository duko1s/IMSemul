"""
Эмулятор иерархической базы данных.
В иерархической базе данных имеется родитель и предки.
Уровень вложенности неограничен, но по мере роста уровней вложенности 
усложняется поддержка связей между уровнями, накапливается избыточность, что
будет продемонстрировано в этом проекте.
Каждый уровень имеет свою структуру данных. создание каждого уровня жестко 
запрограммирована, так же как и связь с предком.
Реализовано ИБД на примере проекта Апполон как историческая признательность
первой базе данных, когда не было понятий файловая система, файл, папка.
А были только диски, цилиндр, головка и сектор.

По такой же архитектуре, возможно воссоздать и другие первые исторические ИБД:
Детали автомобильной отрасли
Библиотека и архив
Телефонный справочник
"""

from interface_DBMS import DBMSShell
from dbms import Project, Roots

if __name__ == "__main__":
    DBMSShell().cmdloop()