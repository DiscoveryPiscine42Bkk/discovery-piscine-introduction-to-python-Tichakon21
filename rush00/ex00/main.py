# main.py

tasks = []

def add_task():
    name = input("ชื่องาน: ")
    category = input("ประเภทงาน (พืช/สัตว์): ").lower()
    tasks.append({"name": name, "category": category})
    print("✅ เพิ่มงานเรียบร้อยแล้ว\n")

def show_tasks():
    if not tasks:
        print("ยังไม่มีงานในระบบ\n")
        return
    print("📋 รายการงานทั้งหมด:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} ({task['category']})")
    print()

def delete_task():
    show_tasks()
    try:
        task_num = int(input("กรอกหมายเลขงานที่ต้องการลบ: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"🗑 ลบงาน '{removed['name']}' เรียบร้อย\n")
        else:
            print("❌ หมายเลขงานไม่ถูกต้อง\n")
    except ValueError:
        print("❌ กรุณากรอกตัวเลขเท่านั้น\n")

def summarize_tasks():
    summary = {}
    for task in tasks:
        cat = task["category"]
        summary[cat] = summary.get(cat, 0) + 1
    print("📊 สรุปจำนวนงานในแต่ละประเภท:")
    for cat, count in summary.items():
        print(f"- {cat}: {count} งาน")
    print()

def main_menu():
    while True:
        print("🧑‍🌾 เมนูจัดการงานฟาร์ม:")
        print("1. เพิ่มงานในฟาร์ม")
        print("2. แสดงรายการงานทั้งหมด")
        print("3. ลบงาน")
        print("4. สรุปจํานวนงานในแต่ละประเภท")
        print("5. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            summarize_tasks()
        elif choice == "5":
            print("👋 ออกจากโปรแกรมแล้ว")
            break
        else:
            print("❌ เลือกไม่ถูกต้อง กรุณาลองใหม่\n")

if __name__ == "__main__":
    main_menu()
