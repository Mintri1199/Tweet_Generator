class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""

        counter = 0
        # TODO: Loop through all nodes and count one for each
        node = self.head
        while node is not None:
            counter += 1
            node = node.next

        return counter

    def get_length_recursive(self, node):
        """
            This function count the number of node in a linked list recursively
            Note: this function is work by assuming the linked list is a singly linked list.
            thus it won't utilized the tail
        """
        if not node:   # Base case
            return 0
        else:
            return 1 + self.get_length_recursive(node.next)     # Call the function again with the next node

    def recursive_wrapper(self):
        """This function wrap the get_length_recursive function"""
        return self.get_length_recursive(self.head)

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""

        # TODO: Create new node to hold given item
        new_node = Node(item)
        current_head = self.head
        current_tail = self.tail
        # TODO: Append node after tail, if it exists
        if not self.is_empty():             # Does the linked list have stuffs?
            if self.tail:                       # Does the tail exist?
                current_tail.next = new_node
                self.tail = new_node
            else:                           # The tail is None and the list is not empty (the list only have one item)
                current_head.next = new_node
                self.tail = new_node
        else:                               # The list is empty
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        new_node = Node(item)
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        if self.head:                       # Does the head exist?
            current_head_node = self.head
            self.head = new_node
            new_node.next = current_head_node
        else:
            self.append(new_node.data)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node:                     # Use a while loop since we can't get the index of the list
            if quality(node.data):      # If the current node's data is the quality return it
                return node.data
            else:
                node = node.next        # If not then go to next

        return None                     # Went through the list an found nothing

    def insert_node_after(self, data, indexed_node, next_node):
        """This is a helper function for inserting node after a specific index"""
        new_node = Node(data)

        if next_node is None:    # Checking whether the current node is the tail
            indexed_node.next = new_node
            self.tail = new_node

        else:
            indexed_node.next = new_node
            new_node.next = next_node

    def begin_insert_after(self, data, index):
        """This function finds the specific node to insert a new node after it"""
        index = int(index)
        size = self.recursive_wrapper() - 1
        if index < 0:  # Is the index less than the linked list?
            raise IndexError(print("The index does not exist"))

        if index > size:  # Is the index bigger than the linked list?
            raise IndexError(print("The index does not exist"))

        current_node = self.head
        counter = 0                                           # The counter we going to use to find a specific node

        while current_node is not None and counter != index:  # This while loop will get the index node we need
            counter += 1
            current_node = current_node.next

        self.insert_node_after(data, current_node, current_node.next)

    def insert_before(self, data, indexed_node, previous_node):
        """This function add the new node to before a specific node"""
        new_node = Node(data)

        if previous_node is None:       # Checking if the indexed node is the head
            self.head = new_node
            new_node.next = indexed_node

        else:
            previous_node.next = new_node
            new_node.next = indexed_node

    def begin_insert_before(self, data, index):
        """This function finds the specific node to insert a new node before it"""
        index = int(index)
        size = self.recursive_wrapper() - 1
        if index < 0:
            raise IndexError("Invalid Index")
        if index > size:
            raise IndexError("Invalid Index")
        previous_node = None                    # Remove this when implemented previous attribute
        current_node = self.head
        counter = 0

        while current_node is not None and counter != index:
            counter += 1
            previous_node = current_node
            current_node = current_node.next

        self.insert_before(data, current_node, previous_node)

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""

        current_node = self.head
        previous_node = None
        found = False
        while current_node:
            if self.head.data == item:              # If the head is the target node
                if self.head.next is not None:      # If the head points to a node
                    self.head = self.head.next      # Reassign the head
                    found = True
                    break
                else:
                    self.head = None                # The list only have one node
                    self.tail = None
                    found = True
                    break

            elif current_node.data == item:         # found the target node and the node is not the head
                if current_node == self.tail:       # Is the tail the targeted node?
                    previous_node.next = None
                    self.tail = previous_node
                    found = True
                    break
                else:                               # The targeted node points to something
                    previous_node.next = current_node.next
                    found = True
                    break
            else:                                   # Not the target node
                previous_node = current_node
                current_node = current_node.next

        if not found:
            raise ValueError(print(""))


def test_recursive_count():
    ll = LinkedList()
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))
    print("length: {}".format(ll.recursive_wrapper()))


def test_insert_after():
    ll = LinkedList()
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))
    ll.begin_insert_after("D", 2)
    print(ll)
    print(ll.head)
    print(ll.tail)

    # ll.begin_insert_after("Fail", 4)
    # print(ll)

    # ll.begin_insert_after("Fail Again", -1)
    # print(ll)


def test_insert_before():
    ll = LinkedList()
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))
    ll.begin_insert_before("1", 2)
    print(ll)
    print(ll.head)
    print(ll.tail)

    # ll.begin_insert_before("Fail", 4)
    # print(ll)
    # ll.begin_insert_before("Fail Again", -1)
    # print(ll)


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_insert_before()

