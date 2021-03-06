from doubly_linked_list import DoublyLinkedList
import sys
# sys.path.append('../doubly_linked_list')
sys.path.insert(
    1, '/home/apetsi/Documents/Projects/lambda/Data-Structures/doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
        # temp = self.storage.head
        # count = 0
        # while temp is not None:
        #     count = count + 1
        #     temp = temp.next
        # return count
