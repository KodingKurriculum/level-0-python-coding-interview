from plumbum import cli

class HeapSort(cli.Application):

    _list = [8, 100, 99, 5, 15, 15, 25, 5, 10, 35, 36, 101, 88]

    def main(self):
        if list is None or len(self._list) is 0:
            print("List should have at least one element")
            return 1
        else:
            sorted_list = self.sort(self._list)
            print(sorted_list)

    def sort(self, heap):
        length = len(heap)-1

        # Walk backwards from the parent of end of the array
        parent = int(length / 2)
        for i in range(parent, -1, -1):
            self.create_max_heap(heap, i, length)

        # Every time we decrement, we're logically reducing the heap space, leaving the last element (the largest)
        for j in range(length, 0, -1):
            # Swap the first and last element, then create a max heap
            heap[0], heap[j] = heap[j], heap[0]
            self.create_max_heap(heap, 0, j)
        return heap


    def create_max_heap(self, heap, parent, size):
        left = parent*2 + 1
        right = parent*2 + 2
        largest = parent

        if right < size and heap[right]>heap[parent]:
            largest = right

        if left < size and heap[left]>heap[largest]:
            largest = left

        if parent != largest:
            # Swap parent with the largest child
            heap[parent], heap[largest] = heap[largest], heap[parent]
            # Run heap function on parent
            self.create_max_heap(heap, largest, size)
        return heap