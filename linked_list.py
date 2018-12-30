import sys


class Node(object):
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        current_node = self.head
        list = []
        while current_node:
            list.append(repr(current_node))
            current_node = current_node.next
        return "[" + ", ".join(list) + "]"

    def find(self, key):
        current_node = self.head
        while current_node:
            if key == current_node.data:
                return current_node
            current_node = current_node.next
        return None


class SingleLinkedList(LinkedList):
    def __init__(self):
        if sys.version_info[0] < 3:
            super(SingleLinkedList, self).__init__()
        else:
            super().__init__()

    def prepend(self, *args):
        for data in args:
            self.head = Node(data=data, next=self.head)
            self.size += 1

    def append(self, *args):
        for data in args:
            if not self.head:
                self.head = Node(data=data, next=self.head)
                self.size += 1
                continue
            if self.head and not self.head.next:
                self.head.next = Node(data=data)
                self.size += 1
                continue
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data=data)
            self.size += 1

    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
        return self

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        current_node = self.head
        previous = None
        found = False
        while current_node:
            if current_node.data != key:
                previous = current_node
                current_node = current_node.next
            else:
                found = True
                break
        # Unlink it from the list
        if previous is None:
            self.head = current_node.next
        elif current_node:
            previous.next = current_node.next
            current_node.next = None
        if found:
            self.size -= 1

    def insert_after(self, data, key):
        found = self.find(key)
        if found:
            found.next = Node(data, next=found.next)
            self.size += 1
            return
        raise Exception("Node with data: %s not present in the list" % key)

    def insert_at(self, data, pos):
        counter = 0
        current_node = self.head
        if pos <= 0:
            self.prepend(data)
            return
        if pos > self.size-1:
            self.append(data)
            return
        previous_node = None
        while current_node:
            if pos == counter:
                new_node = Node(
                        data=data,
                        next=current_node
                        )
                previous_node.next = new_node
                self.size += 1
                return
            previous_node = current_node
            current_node = current_node.next
            counter += 1


class DoubleLinkedList(LinkedList):
    def __init__(self):
        if sys.version_info[0] < 3:
            super(DoubleLinkedList, self).__init__()
        else:
            super().__init__()

    def prepend(self, *args):
        for data in args:
            new_head = Node(data=data, next=self.head)
            if self.head:
                self.head.previous = new_head
            self.head = new_head
            self.size += 1

    def append(self, *args):
        for data in args:
            if not self.head:
                self.head = Node(data=data, next=self.head)
                self.size += 1
                continue
            if self.head and not self.head.next:
                self.head.next = Node(data=data, previous=self.head)
                self.size += 1
                continue
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data=data, previous=current_node)
            self.size += 1

    def reverse(self):
        current_node = self.head
        previous_node = None
        while current_node:
            previous_node = current_node.previous
            current_node.previous = current_node.next
            current_node.next = previous_node
            current_node = current_node.previous
        self.head = previous_node.previous
        return self

    def remove_node(self, node):
        if not isinstance(node, Node):
            raise Exception("2nd param should be a Node object")
        if node.previous:
            node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous
        if node is self.head:
            self.head = node.next
        node.previous = None
        node.next = None
        self.size -= 1

    def remove(self, key):
        found = self.find(key)
        if found:
            self.remove_node(found)
            return
        raise Exception("Node with data: %s not present in the list" % key)

    def insert_after(self, data, key):
        found = self.find(key)
        if found:
            found.next = Node(data, previous=found, next=found.next)
            self.size += 1
            return
        raise Exception("Node with data: %s not present in the list" % key)

    def insert_at(self, data, pos):
        counter = 0
        current_node = self.head
        if pos <= 0:
            self.prepend(data)
            return
        if pos > self.size-1:
            self.append(data)
            return
        while current_node:
            if pos == counter:
                new_node = Node(
                        data=data,
                        previous=current_node.previous,
                        next=current_node
                        )
                current_node.previous.next = new_node
                self.size += 1
                return
            current_node = current_node.next
            counter += 1


if __name__ == '__main__':
    print("-----------------------TEST DoubleLinkedList----------------------")
    dlist = DoubleLinkedList()
    data = ("4", "5", "6")
    dlist.append(*data)
    data2 = ("3", "2", "1")
    dlist.prepend(*data2)
    dlist.append("last")
    dlist.prepend("first")
    print("------------------------------NORMAL ORDER------------------------")
    print("list_size: %s, data: %s" % (len(dlist), dlist))
    print("-------------------------REVERSE ORDER----------------------------")
    print("list_size: %s, data: %s" % (len(dlist), dlist.reverse()))
    print("--------------------------REMOVE OF NODE 3----------------------")
    node_3 = dlist.find("3")
    dlist.remove_node(node_3)
    print("list_size: %s, data: %s" % (len(dlist), dlist.reverse()))
    print("--------------------REMOVE OF NODE WITH DATA '4'------------------")
    dlist.remove("4")
    print("list_size: %s, data: %s" % (len(dlist), dlist))
    print("-----INSERT NODE WITH DATA 'after_2' AFTER NODE WITH DATA '2'-----")
    dlist.insert_after("after_2", "2")
    print("list_size: %s, data: %s" % (len(dlist), dlist))
    print("------------INSERT NODE WITH DATA 'at_0' at position 0------------")
    dlist.insert_at("at_0", 0)
    print("list_size: %s, data: %s" % (len(dlist), dlist))
    # print(dlist.find("at_0").next.previous)
    print("------------INSERT NODE WITH DATA 'at_1' at position 1------------")
    dlist.insert_at("at_1", 1)
    print("list_size: %s, data: %s" % (len(dlist), dlist))

    print("-----------------------TEST SingleLinkedList----------------------")
    slist = SingleLinkedList()
    data = ("4", "5", "6")
    slist.append(*data)
    data2 = ("3", "2", "1")
    slist.prepend(*data2)
    slist.append("last")
    slist.prepend("first")
    print("------------------------------NORMAL ORDER------------------------")
    print("list_size: %s, data: %s" % (len(slist), slist))
    print("-------------------------REVERSE ORDER----------------------------")
    print("list_size: %s, data: %s" % (len(slist), slist.reverse()))
    print("--------------------REMOVE OF NODE WITH DATA '4'------------------")
    slist.remove("4")
    print("list_size: %s, data: %s" % (len(slist), slist))
    print("-----INSERT NODE WITH DATA 'after_2' AFTER NODE WITH DATA '2'-----")
    slist.insert_after("after_2", "2")
    print("list_size: %s, data: %s" % (len(slist), slist))
    print("------------INSERT NODE WITH DATA 'at_0' at position 0------------")
    slist.insert_at("at_0", 0)
    print("list_size: %s, data: %s" % (len(slist), slist))
    print("------------INSERT NODE WITH DATA 'at_1' at position 1------------")
    slist.insert_at("at_1", 1)
    print("list_size: %s, data: %s" % (len(slist), slist))
