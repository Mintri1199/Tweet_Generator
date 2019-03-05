#!python

from linked_list import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0       # O(1) search for size

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored.
        Run time O(1) since it is performing one task and returning one thing
        """

        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n) since the program have to traverse the entire hash table where n is the number of keys"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) same with keys function but where n is the number of value"""
        list_of_values = []         # O(n)
        for bucket in self.buckets:
            for key, value in bucket.items():
                list_of_values.append(value)
        return list_of_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) same with keys function but where n is the number of items?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) because the function has to traverse through buckets and count the items"""
        self.size = 0
        for bucket in self.buckets:
            self.size += bucket.length()
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(n) will be the worst case since the program is going through hash table looking for
        a nonexistence item. The best case if O(1) if the desired value is the first node in a bucket"""
        bucket = self.buckets[self._bucket_index(key)]      # Get the bucket of using the key hash code to get bucket

        current_node = bucket.head  # Set the current node to the head of the current bucket
        while current_node is not None:
            if current_node.data[0] == key:     # Check if the key match
                return True
            current_node = current_node.next    # Reassign the current node to the next

        return False    # Return after go through the bucket

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(1) is the best case if the desired value is in the first node of the bucket.
        O(n) will be the worst case since the program has to traverse through all the items in the buckets to find it
        or finding nothing. """
        bucket = self.buckets[self._bucket_index(key)]
        entry = bucket.find(lambda key_value: key_value[0] == key)

        if entry is not None:
            return entry[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """
        Insert or update the given key with its associated value.
        TODO: Running time: O(1) if the desired node is the first node of a bucket.
        O(n) is the worst case since the program has to traverse through all the items in the buckets.
        """

        bucket = self.buckets[self._bucket_index(key)]

        entry = bucket.find(lambda key_value: key_value[0] == key)
        # Check out the entry that was returned

        if entry:   # Does the entry exist?
            current_node = bucket.head
            while current_node is not None:
                if current_node.data[0] == key:
                    current_node.data = (key, value)
                    break
                current_node = current_node.next
        else:   # The entry does not exist
            bucket.append((key, value))
            self.size += 1

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(1) if the desired node is the first node of a bucket.
        O(n) is the worst case since the program has to traverse through all the items in the buckets.
        """
        bucket = self.buckets[self._bucket_index(key)]

        key_value = bucket.find(lambda item: item[0] == key)
        print(key_value)
        if key_value == None :
            raise KeyError('Key not found: {}'.format(key))
        else:
            bucket.delete(key_value)
            self.size -= 1

        # use linkedlist.find() to get the value the match the key
        


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
