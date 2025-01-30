import heapq  # นำเข้า heapq

class ProductRanking:
    def __init__(self, k):
        self.k = k
        self.products = []  # Min Heap เก็บ k สินค้าขายดีที่สุด
    
    def update_sales(self, product_id, sales):
        # ถ้ายังไม่มีสินค้าครบ k อันดับ
        if len(self.products) < self.k:
            heapq.heappush(self.products, (sales, product_id))
        else:
            # ถ้ามียอดขายมากกว่าค่าต่ำสุด (สินค้าหมดจาก k อันดับ)
            if sales > self.products[0][0]:
                heapq.heapreplace(self.products, (sales, product_id))
    
    def get_top_k(self):
        # เรียงลำดับจากมากไปหาน้อย
        return sorted(self.products, key=lambda x: x[0], reverse=True)

# ตัวอย่างการใช้งาน
ranking = ProductRanking(3)  # เก็บ 3 อันดับสินค้าขายดี
ranking.update_sales("สินค้า A", 100)
ranking.update_sales("สินค้า B", 150)
ranking.update_sales("สินค้า C", 80)
ranking.update_sales("สินค้า D", 200)

# แสดงผลอันดับสินค้าขายดี
top_k = ranking.get_top_k()
for sales, product_id in top_k:
    print(f"สินค้า: {product_id}, ยอดขาย: {sales}")
