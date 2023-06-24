# Represents the individual members in the LinkedList
class Node:
    def __init__(self, data=None, next=None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)
    
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr.prev:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        '''To wipe out if the list already exists and make one with new data values.'''
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self, index):
        ''' Removes the value from the index. The indexing starts from 0'''
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        ''' Insert the value at the given index. Indexing starts from 0.'''
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break

            itr = itr.next

    # There is an error in remove_by_value method
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr:
            if itr.data == data:
                itr.prev = itr.next
                break
            itr = itr.next

if __name__=="__main__":
    ll = LinkedList()
    ll.insert_values(['Apple', 'Banana', 'Cat', 'Dog'])
    ll.print()
    ll.insert_at(0, 'firstApple')
    ll.insert_at(2, 'Oranges')
    ll.print_forward()
    ll.print_backward()