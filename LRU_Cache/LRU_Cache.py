class LRUCache:
    def __init__(self, capacity: int):
        self.size=capacity
        self.d={}
        self.c=0
        

    def get(self, key: int) -> int:
        if key in self.d:
            v=self.d[key]
            self.d.pop(key)
            self.d[key]=v
            return v
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
            self.d[key]=value

        elif self.c==self.size:
            self.d.pop(next(iter(self.d)))
            self.d[key]=value
        
        else:
            self.d[key]=value
            self.c+=1
                    


# LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
