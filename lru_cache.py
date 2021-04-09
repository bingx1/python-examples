#Lru Cache implemented using python's built-in OrderedDict
# OrderedDict stores the order keys were added to the dictionary


class LruCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.price_table = {}
    
 
    def lookup(self, isbn):
        if isbn not in self.price_table:
            return -1
        # Key is popped so that we can re-insert the (key,value) to the back of the queue
        price = self.price_table.pop(isbn)
        self.price_table[isbn] = price


    def insert(self, isbn, price):
        if isbn in self.price_table:
            price = self.price_table.pop(isbn) # Pop even when the item is present so we can update the order of the queue
        elif len(self.price_table == self.capacity):
            self.price_table.popitem(last=False)
        self.price_table[isbn] = price
    
    def erase(self, isbn):
        return self.price_table.pop(isbn, None) is not None
