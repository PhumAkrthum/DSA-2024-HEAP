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

    def extract_max(self):
        """ ลบค่าสูงสุดออกจาก Heap """
        if len(self.heap) == 0:
            return None  # ถ้า Heap ว่างเปล่า
        
        max_val = self.heap[0]  # เก็บค่ามากสุด
        self.heap[0] = self.heap[-1]  # นำค่าล่าสุดมาแทน root
        self.heap.pop()  # ลบค่าล่าสุดออก
        
        if len(self.heap) > 0:
            self._sift_down(0)  # ปรับ heap ใหม่
        
        return max_val

    def _sift_down(self, i):
        """ ปรับโครงสร้าง Heap เมื่อลบค่าออก """
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
            
        if i != max_index:
            self.swap(i, max_index)
            self._sift_down(max_index)

    def print_heap(self):
        """ แสดงค่าใน Heap """
        print("Max Heap:", self.heap)


# สร้าง Max Heap และแทรกค่าที่กำหนด
heap = MaxHeap()
values = [5, 3, 8, 1, 2, 7, 6, 4]

for value in values:
    heap.insert(value)

heap.print_heap()  # แสดงค่าเริ่มต้นของ Heap

# ลบค่าสูงสุด 3 ครั้ง
for i in range(3):
    removed = heap.extract_max()
    print(f"ลบค่าสูงสุดออก: {removed}")
    heap.print_heap()
