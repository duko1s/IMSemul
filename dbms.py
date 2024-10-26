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
    
# путь и имя папки где будет хранится данные
db_path_name = 'ibd_content'
db_path = Path(db_path_name)
# файл ядро СУБД ИБД
root_core_name = '.core_ibd_mgmnt.json'
root_core = db_path / root_core_name

class Roots():
    def __init__(self):
        self.load_roots()

    def load_roots(self):
        self.roots = []
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

class Root():
    """
    Корень ИБД. Это папка которая будет содержать файлы с записями 
    и атрибутами, а так же вложенные папки с предками.
    """
    def __init__(self, name, description='', start_date=None, path=None):
        if not db_path.exists():
            db_path.mkdir()
        if path is None:
            path = db_path / name
            if not path.exists():
                path.mkdir()
            else:
                raise "база с таким именем существует!"
        self.path = Path(path)
        self.name = name
        self.description = description
        if start_date:
            self.start_date = datetime.datetime.fromisoformat(start_date)
        else:
            self.start_date = datetime.datetime.now()
        
    def __str__(self):
        return f"{self.name} | {self.start_date} | {self.path}"
    
    def to_dict(self):
        return self.__dict__


