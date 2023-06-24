class Node: 
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList: 
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else: 
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
    

    def display(self):
        current_node = self.head
        str_node = f""
        while current_node:
            str_node += f" {current_node.data} <--->"
            current_node = current_node.next
        str_node += " END"
        return str_node
    
dll = DoublyLinkedList()
dll.append(1)
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(5)
dll.append(23)
dll.append(34)
dll.append(34)
dll.append(5)
print(dll.display())