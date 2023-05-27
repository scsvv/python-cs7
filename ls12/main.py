class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)
    

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        

    def printf(self) -> str:
        node = self.head
        link_str = ""
        while node:
            link_str += f"{node} -> "
            node = node.next
        else: 
            link_str += f"END"
        
        return link_str

    def get(self, index):
        i = 0
        node = self.head

        while i <= index:
            if i == index:
                return node.data
            elif node.next:
                i += 1
                node = node.next
        else:
            return None
    
    def len(self):
        length = 0
        node = self.head

        while node.next: 
            length += 1
            node = node.next
        else: 
            length += 1

        return length

linklist = LinkedList()
linklist.append(1)
linklist.append(10)
linklist.append(1)
linklist.append(1)
linklist.append(1)
linklist.append(1)
linklist.append(1)
linklist.append(1)
linklist.append(1)
linklist.append(1)
linklist.append(1)
linklist.append(1)
linklist.append(3)
linklist.append(1)
linklist.append(1)
linklist.append(1)
linklist.append(5)

print(linklist.printf())
print(linklist.get(1))
print(linklist.get(16))
print(linklist.len())