class MyHashMap:

    def __init__(self):
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        if contains(self.hash_map, key): # 딕셔너리가 키를 갖고 있는지 확인하는 contains 함수
            return self.hash_map[key]
        return -1

    def remove(self, key: int) -> None:
        if contains(self.hash_map, key):
            delitem(self.hash_map, key)
        return -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)