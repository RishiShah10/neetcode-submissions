class TimeMap:

    def __init__(self):
        self.myMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myMap[key].append((timestamp,value))

        

    def get(self, key: str, timestamp: int) -> str:
        values = self.myMap[key]
        if len(values) == 0:
            return ""
        l,r = 0, len(values) - 1
        while l <= r:
            m = ((l + r) // 2)
            print(l,r,m)
            time,val = values[m]
            if time == timestamp:
                return val
            elif time <= timestamp:
                l = m + 1
            else:
                r = m - 1
        if r < 0: return ""
        return values[r][1] 
        
