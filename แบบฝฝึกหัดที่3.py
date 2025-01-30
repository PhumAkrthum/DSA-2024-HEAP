def is_max_heap(arr):
    """ ตรวจสอบว่า arr เป็น Max Heap หรือไม่ """
    n = len(arr)
    
    for i in range(n):  # วนลูปเช็คทุกตำแหน่ง
        left = 2 * i + 1   # ตำแหน่งลูกซ้าย
        right = 2 * i + 2  # ตำแหน่งลูกขวา

        # ถ้ามีลูกซ้าย และค่าของลูกซ้ายมากกว่าพ่อ → ไม่ใช่ Max Heap
        if left < n and arr[left] > arr[i]:
            return False
        
        # ถ้ามีลูกขวา และค่าของลูกขวามากกว่าพ่อ → ไม่ใช่ Max Heap
        if right < n and arr[right] > arr[i]:
            return False

    return True  # ถ้าผ่านทุกเงื่อนไข แสดงว่าเป็น Max Heap



arr1 = [9, 7, 8, 3, 6, 5, 4]  #  จะเป็น Max Heap
arr2 = [10, 15, 8, 7, 6, 5, 4]  #  ไม่เป็น Max Heapเพราะตรงที่ (15 > 10)
arr3 = [8, 4, 7, 3, 2, 5, 6, 1]  #  เป็น Max Heap 

print(is_max_heap(arr1))  
print(is_max_heap(arr2)) 
print(is_max_heap(arr3))  
