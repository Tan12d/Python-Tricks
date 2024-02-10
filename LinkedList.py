class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, new_node):
        if self.head:
            last_node = self.head
            while last_node.next!=None:
                last_node = last_node.next
            last_node.next=new_node
        
        else:
            self.head=new_node
    
    def display(self):
        temp_node = self.head
        while temp_node != None:
            print(temp_node.data, end=" -> ")
            temp_node = temp_node.next
        print('Null')

if __name__ =='__main__':
    linked_list = LinkedList()

    # linked_list.insert(Node(1))
    # linked_list.insert(Node(2))
    # linked_list.insert(Node(3))
    # linked_list.insert(Node(4))

    for i in range(0,5):
        linked_list.insert(Node(int(input())))

    linked_list.display()