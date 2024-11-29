"""
Система управления иерархической базой данных
1. создание корня
2. удаление корня
3. просмотр информации о всех корнях
"""
import datetime
import os
from pathlib import Path
import json

# функция сериализации сложных типов данных в строки  json
def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    elif isinstance(o, Path):
        return os.fspath(o)
    
"""
Множество корней ИБД  решающих одну и ту же задачу хранения и 
управления одними типами данных.
В нашем случае проект - модуль - деталь
"""
class Roots():
    # путь и имя папки где будет хранится данные
    db_path_name = 'ibd'
    db_path = Path(db_path_name)
    # файл ядро СУБД ИБД
    root_core_name = '_meta.json'
    root_core = db_path / root_core_name
        
    def __init__(self):
        self.projects = []
        self.load()
        self.current = None
    
    def __len__(self):
        return len(self.projects)
    
    # загрузить структуру с диска
    def load(self):
        if self.root_core.exists():
            with open(self.root_core, 'r') as f:
                projects = json.load(f)
            for project in projects:
                self.projects.append(Project(**project))
        else:
            os.mkdir(self.db_path_name)
            self.save()
    
    # сохранить структуру на диск
    def save(self):
        result = []
        for item in self.projects:
            result.append(item.to_dict())
        j_dump = json.dumps(result, indent=2, default=default)
        # print(j_dump)
        with open(self.root_core, 'w') as f:
            f.write(j_dump)
    
    # добавить новую базу данных - проект
    def add(self, project):
        self.projects.append(project)
        self.save()
    
    # отобразить список баз данных 
    def list(self):
        if not self.projects:
            print("ИБД нет! создайте хотя бы одну базу!")
        for index, root in enumerate(self.projects):
            print(f"{index + 1}{'*' if root.current else ''}. {root}")

    # выбрать имеющуюся базу данных
    def select(self, index=None):
        if index is None or index == 0:
            os.chdir(self.db_path)
            self.current = None
        if 1 <= index <= len(self.projects):
            self.current = index - 1
            root = self.projects[index - 1]
            os.chdir(root.path)
        return root
    
"""
    Корень ИБД. Это папка которая будет содержать определнную иерархическую базу
    данных (по сути большая область последовательности байтов на первых дискам
    IBM - где еще только зарождается понятие файловой системы).
    Имя проекта это и есть корень: его характеризует имя, описание, 
    время начала проекта и служебная информация - путь хранения информации и 
    связь с дочерними объектами - модулями проекта.
"""
class Project():
    META = '_meta.json'
    db_path = Roots.db_path
    def __init__(self, name, description='', start_date=None,
                 path=None, modules = [], current=None):
        if not self.db_path.exists():
            self.db_path.mkdir()
        if path is None:
            path = self.db_path / name
            if not path.exists():
                path.mkdir()
            else:
                raise NameError("Проект с таким именем существует! Имена проектов должны быть уникальны! Дайтье другое имя.")
        self.path = Path(path)
        self.name = name
        self.description = description
        if start_date:
            self.start_date = datetime.datetime.fromisoformat(start_date)
        else:
            self.start_date = datetime.datetime.now()
        self.modules = modules
        self.current = current
        
    def __str__(self):
        return f"{self.name} | {self.start_date} | {self.path}"
    
    def to_dict(self):
        return self.__dict__
    
    
    def load(self):
        meta = self.path / self.META
        if meta:
            with open(meta, 'r') as f:
                modules = json.load(f)
            for module in modules:
                self.modules.append(Module(**module))

    def save(self):
        result = []
        meta = self.path / self.META
        for item in self.modules:
            result.append(item.to_dict())
        j_dump = json.dumps(result, indent=2, default=default)
        # print(j_dump)
        with open(meta, 'w') as f:
            f.write(j_dump)

    # добавить модуль космического коробля
    def add(self, module):
        self.modules.append(module)
        self.save()


    def list(self):
        if not self.modules:
            print("Модулей нет!")
        for module in self.modules:
            print(module)

    def select(self, index):
        if self.current is not None:
            #os.chdir(db_path)
            self.current = None
        if 0 <= index < len(self.modules):
            self.current = index
            module = self.modules[index]
            #os.chdir(root.path)
        return module

    

"""
Модуль имеет такие характеристики как название, описание назначения, 
масса, габариты, 
картинка внешнего вида (общий макет).
Общий макет в те далекие времена не могли еще хранить в виде файлов
хранилась структурная информацяи где взять альбом с рисунками и чертежами, в виде
стелаж-полка-папка.
Так же мы храним служебную информацию, откуда считать метаинформацию по каждым
экземплярам модулей, в нашем случае папка в файловой системе.
"""
class Module():
    META = '_meta.json'
    def __init__(self, name, description="", path=None, 
                 ):
        self.name = name
        self.description = description
        if path is None:
            current_root = Path(".")
            self.path = current_root / name
        else:
            self.path = path
        
    # Добавить модуль
    def add(self, child):
        self.children.append(child)

    def load(self):
        if root_core.exists():
            with open(root_core, 'r') as f:
                roots = json.load(f)
            for root in roots:
                self.roots.append(Root(**root))

    def save(self):
        result = []
        for item in self.roots:
            result.append(item.to_dict())
        j_dump = json.dumps(result, indent=2, default=default)
        # print(j_dump)
        with open(root_core, 'w') as f:
            f.write(j_dump)

    def add_root(self, root):
        self.roots.append(root)
        self.save()

    def list(self):
        if not self.roots:
            print("ИБД нет! создайте хоть одну базу!")
        for root in self.roots:
            print(root)

    def select(self, index):
        if self.current is not None:
            #os.chdir(db_path)
            self.current = None
        if 0 <= index < len(self.roots):
            self.current = index
            root = self.roots[index]
            #os.chdir(root.path)
        return root

    # Добавление методов для работы с оборудованием
    def get_equipment_data(self):
        return self.equipment_data

    def set_equipment_data(self, data):
        self.equipment_data = data



    