import sys


class Node(object):
    """Class to represent a node of a LinkedList.

    Attributes:
        data (Optional[str]):
            Contains the data of the Node object.
            Default to None if not specified.
        previous (Optional[str]):
            Represents the pointer to the previous node.
            Default to None if not specified.
        next (Optional[str]):
            Represents the pointer to the next node.
            Default to None if not specified.

    Methods:
        __repr__: Overrides __repr__ dunder method.
        Returns the data(str) contained in the Node object.
    """

    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList(object):
    """Class to represent a LinkedList of Node objects.

    Attributes:
        head (str):
            Specifies the head of the LinkedList.
            Initialized as None.
        size (str):
            Specifies the size of a LinkedList.
            Initialized as 0.

    Methods:
        __len__: Overrides __len__ dunder method.
        Returns the size of the LinkedList.
        __repr__: Overrides __repr__ dunder method.
        Returns the data(str) contained in the Node object.
        find: Finds the first occurrence of a key in the list.
        Returns a Node object.
    """
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
        """
        Finds the first occurrence of key argument in the list.
        Takes O(n) time.

        Args:
            key(str): The key to search in the list.

        Returns:
            First Node object with data equals to key.
            If no occurence found, returns None.
        """
        current_node = self.head
        while current_node:
            if key == current_node.data:
                return current_node
            current_node = current_node.next
        return None


class SingleLinkedList(LinkedList):
    """SubClass of LinkedList. Represents a SingleLinkedList of Node objects.

    Attributes:
        head (str):
            Inherited from LinkedList.
        size (str):
            Inherited from LinkedList.

    Methods:
        prepend: Adds Node objects at the beginning of the LinkedList.
        append: Adds Node objects at the end of the LinkedList.
        reverse: Reverses the LinkedList in place and returns it.
        remove: Remove the first occurence in the list.
        insert_at: Insert Node at specific position in LinkedList.
        insert_after: Insert Node after the first occurence of `key` found.
    """
    def __init__(self):
        if sys.version_info[0] < 3:
            super(SingleLinkedList, self).__init__()
        else:
            super().__init__()

    def prepend(self, *args):
        """
        Adds Node objects at the beginning of the LinkedList.
        Takes O(1) time for each node.

        Args:
            *args: Variable length argument list of data.
        """
        for data in args:
            self.head = Node(data=data, next=self.head)
            self.size += 1

    def append(self, *args):
        """
        Adds Node objects at the end of the LinkedList.
        Takes O(n) time for each node.

        Args:
            *args: Variable length argument list of data.
        """
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
        """
        Reverses the list of Nodes in place.
        Takes O(n) time.

        Returns:
            The list itself.
        """
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
        Removes the first occurrence of `key` in the list.
        Takes O(n) time.

        Args:
            key (str): The key to find the Node for removal.

        Raises:
            Exception: If no Node with `key` data found in the list.
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
        else:
            raise Exception("Node with data: %s not present in the list" % key)

    def insert_after(self, data, key):
        """
        Inserts new Node with `data` after the first occurence of `key`.
        Takes O(n) time.

        Args:
            data (str): The content of the node to be inserted.
            key (str): The key to search the Node with the correpsonding data.

        Raises:
            Exception: If no Node with `key` found.
        """
        found = self.find(key)
        if found:
            found.next = Node(data, next=found.next)
            self.size += 1
            return
        raise Exception("Node with data: %s not present in the list" % key)

    def insert_at(self, data, pos):
        """
        Inserts new Node with `data` at position `pos`.
        Takes O(1) time if position is <= 0 or >= list_size.
        For all other cases takes O(n) time.

        Args:
            data (str): The content of the node to be inserted.
            pos (int): The position in the list that the new Node
            will be inserted. First Node of the list has position 0.
        """
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
    """SubClass of LinkedList. Represents a DoubleLinkedList of Node objects.

    Attributes:
        head (str):
            Inherited from LinkedList.
        size (str):
            Inherited from LinkedList.

    Methods:
        prepend: Adds Node objects at the beginning of the LinkedList.
        append: Adds Node objects at the end of the LinkedList.
        reverse: Reverses the LinkedList in place and returns it.
        remove_node: Remove a Node from the list.
        remove: Remove the first occurence in the list.
        insert_at: Insert Node at specific position in LinkedList.
        insert_after: Insert Node after the first occurence of `key` found.
    """
    def __init__(self):
        if sys.version_info[0] < 3:
            super(DoubleLinkedList, self).__init__()
        else:
            super().__init__()

    def prepend(self, *args):
        """
        Adds Node objects at the beginning of the LinkedList.
        Takes O(1) time for each node.

        Args:
            *args: Variable length argument list of data.
        """
        for data in args:
            new_head = Node(data=data, next=self.head)
            if self.head:
                self.head.previous = new_head
            self.head = new_head
            self.size += 1

    def append(self, *args):
        """
        Adds Node objects at the end of the LinkedList.
        Takes O(n) time for each node.

        Args:
            *args: Variable length argument list of data.
        """
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
        """
        Reverses the list of Nodes in place.
        Takes O(n) time.

        Returns:
            The list itself.
        """
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
        """
        Unlink the Node `node` from the list.
        Takes O(1) time.

        Args:
            node (Node): The node to be removed.

        Raises:
            TypeError: If node param is not a Node object.
        """
        if not isinstance(node, Node):
            raise TypeError("`node` param should be <Node> and is a <%s>"
                            % type(node).__name__)
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
        """
        Removes the first occurrence of `key` in the list.
        Takes O(n) time.

        Args:
            key (str): The key to find the Node for removal.

        Raises:
            Exception: If no Node with `key` data found in the list.
        """
        found = self.find(key)
        if found:
            self.remove_node(found)
            return
        raise Exception("Node with data: %s not present in the list" % key)

    def insert_after(self, data, key):
        """
        Inserts new Node with `data` after the first occurence of `key`.
        Takes O(n) time.

        Args:
            data (str): The content of the node to be inserted.
            key (str): The key to search the Node with the correpsonding data.

        Raises:
            Exception: If no Node with `key` found.
        """
        found = self.find(key)
        if found:
            found.next = Node(data, previous=found, next=found.next)
            self.size += 1
            return
        raise Exception("Node with data: %s not present in the list" % key)

    def insert_at(self, data, pos):
        """
        Inserts new Node with `data` at position `pos`.
        Takes O(1) time if position is <= 0 or >= list_size.
        For all other cases takes O(n) time.

        Args:
            data (str): The content of the node to be inserted.
            pos (int): The position in the list that the new Node
            will be inserted. First Node of the list has position 0.
        """
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
