import sys
# sys.path.append('../doubly_linked_list')
sys.path.insert(
    1, '/home/apetsi/Documents/Projects/lambda/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add to tail
        self.size += 1
        return self.storage.add_to_tail(value)
        

    def dequeue(self):
        # remove from front
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_from_head()
        pass


    def len(self):
        return self.size
