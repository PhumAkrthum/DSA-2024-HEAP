class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
        
    def left_child(self, i):
        return 2 * i + 1  
        
    def right_child(self, i):
        return 2 * i + 2
        
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, key):
        """ แทรกค่าใหม่ลงใน Heap """
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, i):
        """ ปรับโครงสร้าง Heap เมื่่อเพิ่มค่าใหม่ """
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)

    def print_heap(self):
        """ แสดงค่าใน Heap """
        print("Max Heap:", self.heap)


# สร้าง Max Heap และแทรกค่าที่กำหนด
heap = MaxHeap()
values = [5, 3, 8, 1, 2, 7, 6, 4]

for value in values:
    heap.insert(value)

heap.print_heap()

