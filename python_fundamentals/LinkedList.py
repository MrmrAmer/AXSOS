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
    
    def remove_from_front(self):
        removed_value = self.head.value
        self.head = self.head.next
        return print(removed_value)
    
    def remove_from_back(self):
        runner = self.head
        while (runner.next.next != None):
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return print(removed_value)

my_list = SList()
my_list2 = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").add_to_back("fun222!").print_values()
my_list2.add_to_back("Hmmm").print_values()

my_list.remove_from_front()
my_list.remove_from_back()

my_list.print_values()
