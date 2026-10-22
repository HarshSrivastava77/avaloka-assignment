class Node:
    def __init__(self, key, value):
        self.key = key  # keep key so we can delete it from dict later
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # fake head and tail, so no empty-list checks
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

    def add_node(self, node):
        # front = most recently used
        first = self.head.next

        node.next = first
        node.prev = self.head

        self.head.next = node
        first.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)

        return node.value

    def put(self, key, value):
        if self.capacity <= 0:
            return

        # key already exists: update it, no removal
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove_node(node)
            self.add_node(node)
            return

        if len(self.cache) == self.capacity:
            # full, remove the oldest node (just before tail)
            old_node = self.tail.prev
            self.remove_node(old_node)
            del self.cache[old_node.key]

        node = Node(key, value)
        self.cache[key] = node
        self.add_node(node)


c = LRUCache(2)

c.put(1, 1)
c.put(2, 2)
print(c.get(1))  # 1

c.put(3, 3)
print(c.get(2))  # -1

c.put(1, 10)
print(c.get(1))  # 10
print(c.get(3))  # 3

c.put(4, 4)
print(c.get(1))  # -1
print(c.get(4))  # 4

z = LRUCache(0)
z.put(1, 1)
print(z.get(1))  # -1
