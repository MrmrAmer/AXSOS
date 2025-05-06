class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
        prev = None
        current = head
 
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


    def removeNthFromEnd(self, head, n):
        start = ListNode(0)
        start.next = head
        first = start
        second = start
 
        for _ in range(n + 1):
            first = first.next
 
        while first:
            first = first.next
            second = second.next
 
        second.next = second.next.next
 
        return start.next