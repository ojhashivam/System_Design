class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.counter = {}
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.counter[key] += 1
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.counter[key] += 1
            self.cache.pop(key)
            self.cache[key] = value

        else:
            if len(self.cache) < self.size:
                self.counter[key] = 1
                self.cache[key] = value

            else:
                least_recent = min(self.counter.values())
                for i in self.cache:
                    if self.counter[i] == least_recent:
                        self.cache.pop(i)
                        self.counter.pop(i)
                        break

                self.counter[key] = 1
                self.cache[key] = value
