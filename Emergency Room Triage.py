import heapq  # นำเข้า heapq สำหรับใช้งาน heap

class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority  # ระดับความรุนแรง 1-5 (1 = ฉุกเฉินมาก)
    
    def __lt__(self, other):
        # เปรียบเทียบความรุนแรง โดยที่ค่าความรุนแรงต่ำ (priority ต่ำ) จะมีความสำคัญมากกว่า
        return self.priority < other.priority

class ERQueue:
    def __init__(self):
        self.queue = []  # Min Heap เพื่อให้ผู้ป่วยที่มี priority ต่ำ (อาการหนัก) ได้รับการรักษาก่อน
    
    def add_patient(self, patient):
        heapq.heappush(self.queue, patient)  # ใช้ heapq เพื่อเพิ่มผู้ป่วยในลำดับที่ถูกต้อง
    
    def treat_next_patient(self):
        if self.queue:
            return heapq.heappop(self.queue)  # ลบผู้ป่วยที่มี priority ต่ำสุด (อาการหนัก)
        return None

# ตัวอย่างการใช้งาน
er = ERQueue()
er.add_patient(Patient("คนไข้ A", 1))  # หัวใจวาย
er.add_patient(Patient("คนไข้ B", 3))  # ปวดท้อง
er.add_patient(Patient("คนไข้ C", 2))  # กระดูกหัก

# ทดสอบการรักษาผู้ป่วย
next_patient = er.treat_next_patient()
if next_patient:
    print(f"รักษาผู้ป่วย: {next_patient.name}, Priority: {next_patient.priority}")
else:
    print("ไม่มีผู้ป่วยในคิว")

next_patient = er.treat_next_patient()
if next_patient:
    print(f"รักษาผู้ป่วย: {next_patient.name}, Priority: {next_patient.priority}")
else:
    print("ไม่มีผู้ป่วยในคิว")

next_patient = er.treat_next_patient()
if next_patient:
    print(f"รักษาผู้ป่วย: {next_patient.name}, Priority: {next_patient.priority}")
else:
    print("ไม่มีผู้ป่วยในคิว")
