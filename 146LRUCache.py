class linkedNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = dict()
        self.head = linkedNode(0, 0)
        self.tail = linkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        self._insert(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.size == self.capacity and key not in self.hashmap:
            # delete tail
            self._delete()
        if key not in self.hashmap:
            node = linkedNode(key, value)
            self.hashmap[key] = node
            self._insert(node)
            self.size += 1
        else:
            node = self.hashmap[key]
            node.val = value
            prev = node.prev
            next = node.next
            
            prev.next = next
            next.prev = prev
            self._insert(node)
        return None
            
    def _delete(self):
        # delete least visited element
        toDelete = self.tail.prev
        key = toDelete.key
        tmp = toDelete.prev
        tmp.next = self.tail
        self.tail.prev = tmp
        del self.hashmap[key]
        self.size -= 1
        
    def _insert(self, node):
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        tmp.prev = node
        node.prev = self.head
   
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
print(lRUCache.get(2))
print(lRUCache.put(2, 6))
print(lRUCache.get(1))
print(lRUCache.put(1, 5))
print(lRUCache.put(1, 2))
print(lRUCache.get(1))
print(lRUCache.get(2))
# [null,-1,null,-1,null,null,2,6]

