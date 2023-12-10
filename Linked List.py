from newnode import Node


class Linkedlist:
    def __init__(self):
        self.__first = None

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        self.__first = value

    @first.deleter
    def first(self):
        del self.__first

    def is_empty(self):
        if self.first is None:
            return "List is empty"
        return "List is not empty"

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.first

        if self.first is not None:
            self.first.prev = new_node

        self.first = new_node
        return "Data prepended to LinkedList"

    def append(self, data):
        new_node = Node(data)

        if self.first is None:
            self.first = new_node
            return

        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        tmp.next = new_node
        new_node.prev = tmp
        return "Data appended to LinkedList"

    def insert_after(self, target_data, data):
        if self.first is None:
            return "There is no target data in empty list"

        tmp = self.first

        while tmp is not None:
            if tmp.data == target_data:
                new_node = Node(data)
                new_node.next = tmp.next
                new_node.prev = tmp
                if tmp.next is not None:
                    tmp.next.prev = new_node
                tmp.next = new_node
                return "Data inserted after target data"
            tmp = tmp.next

        return f"Target data '{target_data}' not found in the list"

    def insert_before(self, target_data, data):
        if self.first is None:
            return "There is no target data in empty list"

        tmp = self.first
        while tmp is not None:
            if tmp.data == target_data:
                new_node = Node(data)
                new_node.next = tmp
                new_node.prev = tmp.prev
                if tmp.prev is not None:
                    tmp.prev.next = new_node
                else:
                    self.first = new_node
                tmp.prev = new_node
                return "Data inserted before target data"

            tmp = tmp.next

        return f"Target data '{target_data}' not found in the list"

    def delete(self, data):
        if self.first is None:
            return "There is no data to delete in empty list"

        tmp = self.first

        while tmp is not None:
            if tmp.data == data:
                if tmp.next is not None:
                    tmp.next.prev = tmp.prev
                if tmp.prev is not None:
                    tmp.prev.next = tmp.next
                if tmp == self.first:
                    self.first = tmp.next
                tmp.data = None
                tmp.prev = None
                tmp.next = None
                return f"Data {data} deleted"
            tmp = tmp.next
        return "Data not found"

    def display(self):
        if self.first is None:
            return "There is nothing to show"

        lst = []
        tmp = self.first
        while tmp:
            lst.append(tmp.data)
            tmp = tmp.next
        return lst


if __name__ == "__main__":
    dll = Linkedlist()
    print(dll.is_empty())
    dll.append(10)
    dll.append(90)
    dll.prepend(7)
    dll.insert_after(10, 88)
    dll.insert_before(90, 77)
    print(dll.delete(9))
    dll.delete(7)
    print(*dll.display())
    print(dll.is_empty())

