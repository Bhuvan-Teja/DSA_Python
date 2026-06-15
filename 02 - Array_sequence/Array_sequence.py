import sys

class ArraySequence:
    def dynamic_array(self, size):
        # this method demostrates how python creates extra memory as the list size increases
        arr = []
        for i in range(size):
            arr.append(i)
            print(f"Size: {sys.getsizeof(arr):4d} bytes, Length: {len(arr):3d}")

array_sequence = ArraySequence()
array_sequence.dynamic_array(20)
