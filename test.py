def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr))
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [11, 12, 22, 25, 34, 64, 90]
target = 22
print(binary_search(arr, target))
class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    
    def _hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
        
hash_table = HashTable()
hash_table.insert(12, "apple")
hash_table.insert(22, "banana")
hash_table.insert(32, "orange")
value = hash_table.search(22)
print(value)