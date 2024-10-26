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

from interface import showMenu
from dbms import Root, Roots

if __name__ == "__main__":
    # отобразить диалог с пользователем с меню:
    # - отобразить имеющиеся корни
    # - создать корень
    # - выбрать нужный корень
    # если ИБД пуста создать первоначальную структуру: 
    # папку с контентом и json файл с метаинформацией
    

    
    # Считываю базы и так как структура пустая , то создаю пустую базу 
    # и вывожу содержимое
    roots = Roots()
    roots.list()
    print("++++++++++++++++++++++++++++++++++++++++")
    # добавляю две базы
    roots.add_root(Root("Апполон1"))
    roots.add_root(Root("Национальная библиотека"))
    roots.list()
    # Снова считываю базы т.к. структура уже создана то заполняю структуру
    # и добавляю еще одну базу и вывожу 
    roots = Roots()
    roots.add_root(Root("VAZ2106", "детали для автомобиля ВАЗ 2106"))
    print("++++++++++++++++++++++++++++++++++++++++")
    roots.list()