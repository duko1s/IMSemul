class BaseEntity:
    def __init__(self, id):
        self.id = id

class Node(BaseEntity):
    def __init__(self, id, name, parent_id=None):
        super().__init__(id)
        self.name = name
        self.parent_id = parent_id

    def display_info(self):
        print("ID:", self.id)
        print("Name:", self.name)
        if self.parent_id:
            print("Parent ID:", self.parent_id)

class Leaf(BaseEntity):
    def __init__(self, id, value):
        super().__init__(id)
        self.value = value

    def display_info(self):
        print("ID:", self.id)
        print("Value:", self.value)

# Пример использования
node1 = Node("1", "Root", parent_id=None)
leaf1 = Leaf("1-1", "Leaf 1")
leaf2 = Leaf("1-2", "Leaf 2")
node2 = Node("2", "Child", parent_id="1")

node1.display_info()
leaf1.display_info()
leaf2.display_info()
node2.display_info()