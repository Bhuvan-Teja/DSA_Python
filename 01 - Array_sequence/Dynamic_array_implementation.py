class dynamic_array():
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._array = self.make_array(self._capacity)

    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]
    
    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = value
        self._size += 1

    def _resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def make_array(self, capacity):
        return [None] * capacity

arr = dynamic_array()
arr.append(1)
print("Value is ",len(arr))
print("capacity is ", arr._capacity)
arr.append(2)
print("Value is ",len(arr))
print("capacity is ", arr._capacity)
arr.append(3)
print("Value is ",len(arr))
print("capacity is ", arr._capacity)
arr.append(4)
print("Value is ",len(arr))
print("capacity is ", arr._capacity)
arr.append(5)
print("Value is ",len(arr))
print("capacity is ", arr._capacity)
print(arr[0])
print(arr[1])