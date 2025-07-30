class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Hashmap:
    def __init__(self):
        self.hashtable = [None] * 10

    def insert(self, key):
        hashvalue = key % 10
        node = Node(key)
        if self.hashtable[hashvalue] == None:
            self.hashtable[hashvalue] = node
        else:
            current_linkedlist = self.hashtable[hashvalue]
            self.hashtable[hashvalue] = self.traverse_insert(node, current_linkedlist)

    def traverse_insert(self, node, current_linkedlist):
        previous = current_linkedlist
        forward = current_linkedlist.next
        head = current_linkedlist
        current = current_linkedlist

        if node.key < head.key:
            node.next = head
            return node

        while current.next is not None:
            current = current.next
        if node.key > current.key:
            current.next = node
            return head

        while node.key > previous.key and node.key < forward.key:
            previous = previous.next
            forward = forward.next

        previous.next = node
        node.next = forward
        return head

    def remove(self, key):
        hashvalue = key % 10
        if self.hashtable[hashvalue] is None:
            print("cannot delete something which doesnt exist")
        elif self.hashtable[hashvalue].next is None:
            self.hashtable[hashvalue] = None
        else:
            current_linkedlist = self.hashtable[hashvalue]
            self.hashtable[hashvalue] = self.deletion_by_traversal(
                key, current_linkedlist
            )

    def deletion_by_traversal(self, key, current_linkedlist):
        head = current_linkedlist
        previous = current_linkedlist
        forward = current_linkedlist.next
        if key == head.key:
            head = head.next
            return head

        while key > forward.key:
            previous = previous.next
            forward = forward.next
        if key == forward.key:
            previous.next = forward.next
        return head

    def display(self):
        for linkedlist in self.hashtable:
            if linkedlist is None:
                print(linkedlist)
                continue
            current = linkedlist

            while current.next is not None:
                print(f"{current.key} -> ", end="")
                current = current.next
            print(current.key, end=" -> None")
            print()


h = Hashmap()
h.insert(10)
h.insert(11)
h.insert(12)
h.insert(14)
h.insert(15)
h.insert(16)
h.insert(17)
h.insert(18)
h.insert(19)
h.insert(22)
h.insert(24)
h.insert(25)
h.insert(26)
h.insert(27)
h.insert(28)
h.insert(29)
h.insert(35)
h.insert(45)
h.insert(55)
h.insert(65)
h.insert(75)
h.display()
h.remove(15)
print()
print("New Hashtable after deleting 15 ")
print()
h.display()

h.remove(55)
print()
print("New Hashtable after deleting 55")
print()
h.display()

h.remove(75)
print()
print(" New Hashtable after deleting 75")
print()
h.display()
h.remove(11)
print()
print("New Hashtable after deleting 11")
print()
print(h.display())
h.remove(22)
print()
print("New Hashtable after deleting 22")
print()
print(h.display())
