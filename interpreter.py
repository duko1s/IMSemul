"""
Интерпретатор языка запросов к Иерархической Базе данных
Состоит из двух разделов:
DDL - язык определения структуры данных
DML - язык манипуляции с данными
"""

class Interpreter:
    def __init__(self, root):
        self.root = root

    def execute(self, command):
        if command == 'add_node':
            name = input("Введите имя узла: ")
            parent = input("Укажите родителя (если есть): ")
            node = Node(name, parent)
            self.root.add_child(node)
        elif command == 'get_node':
            name = input("Введите имя узла: ")
            print(self.get_node(name))
        elif command == 'update_node':
            name = input("Введите имя узла: ")
            equipment_data = {
                'fuel_capacity': input("Ёмкость топлива: "),
                'max_speed': input("Максимальная скорость: ")
            }
            self.update_node(name, equipment_data)
        elif command == 'delete_node':
            name = input("Введите имя узла: ")
            self.delete_node(name)
        elif command == 'search_nodes':
            criteria = input("Введите критерии поиска: ")
            results = self.search_nodes(criteria)
            for result in results:
                print(result)

    # Реализация методов для выполнения операций над узлами
    def get_node(self, name):
        return self.root.get_child_by_name(name).equipment_data

    def update_node(self, name, data):
        node = self.root.get_child_by_name(name)
        node.equipment_data.update(data)

    def delete_node(self, name):
        node = self.root.get_child_by_name(name)
        self.root.children.remove(node)

    def search_nodes(self, criteria):
        results = []
        for node in self.root.children:
            if self.matches_criteria(node, criteria):
                results.append(node)
        return results

    def matches_criteria(self, node, criteria):
        # Пример реализации поиска по критериям
        equipment_data = node.equipment_data
        max_speed = equipment_data['max_speed']
        return max_speed > int(criteria)

# Создание корневого узла
root = Node("Root")

# Инициализация интерпретатора
interpreter = Interpreter(root)

while True:
    command = input("Введите команду: ")
    interpreter.execute(command)
