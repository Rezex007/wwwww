import csv
import json
import os

CSV_FILE = "data.csv"       # ชื่อไฟล์ CSV ของคุณ
OUTPUT_DIR = "public/data"   # โฟลเดอร์เก็บข้อมูลย่อย

os.makedirs(OUTPUT_DIR, exist_ok=True)

# สมมติชื่อคอลัมน์ username ให้ปรับตามหัวตารางจริงของคุณ
USERNAME_COL = "username"

buckets = {}
print("กำลังอ่านและจัดหมวดหมู่ข้อมูล...")

with open(CSV_FILE, mode="r", encoding="utf-8-sig", errors="ignore") as f:
    reader = csv.DictReader(f)
    for row in reader:
        u = row.get(USERNAME_COL, "").strip()
        if not u:
            continue
        
        # ใช้ 2 ตัวอักษรแรก (ตัวพิมพ์เล็ก) เป็นชื่อไฟล์ เช่น "oh.json", "ad.json"
        prefix = u[:2].lower()
        if not prefix.isalnum():
            prefix = "other"
            
        if prefix not in buckets:
            buckets[prefix] = []
        buckets[prefix].append(row)

print(f"กำลังเซฟไฟล์ทั้งหมด {len(buckets)} ไฟล์...")
for prefix, data in buckets.items():
    with open(os.path.join(OUTPUT_DIR, f"{prefix}.json"), "w", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False)

print("แบ่งไฟล์เสร็จสมบูรณ์!")