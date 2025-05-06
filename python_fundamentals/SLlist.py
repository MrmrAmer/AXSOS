class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        new_node = SLNode(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    
    def add_to_back(self, value):
        if self.head == None:
            return self.add_to_front(value)
        new_node = SLNode(value)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    
my_list = SList()
my_list.add_to_front("are").add_to_front("Linked Lists").add_to_back("Fun!").print_values()