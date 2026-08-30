class TimeMap:
    # keys: names
    # ["A", "b"]

    # values: mood 
    # ["happy", "sad"]

    # timestamp: number
    # ["1", "2"]

    # ask for timestamp
    # return all values before this timestamp that has the key 
    def __init__(self):
        self.keyStore = {} #initialize as defaultdict so it does not wrror if key is not present  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key,[])
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r-l)//2 
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1 #so that it will search only right half, return the largest timestamp
            else:
                r = m - 1
        return res
