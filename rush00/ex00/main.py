# Smart Farm Task Organizer

tasks = []

def add_task():
    print("📌 ป้อนชื่องาน:", end=" ")
    name = input()
    print("📅 ป้อนวันที่ (dd/mm/yyyy):", end=" ")
    date = input()
    print("🐄 ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ):", end=" ")
    category = input()

    task = {
        "name": name,
        "date": date,
        "category": category
    }
    tasks.append(task)
    print("✅ เพิ่มงานสำเร็จ\n")

def show_tasks():
    if not tasks:
        print("\n📋 ไม่มีงานในระบบ\n")
        return
    print("\n📋 รายการงานทั้งหมด:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['date']} – {task['name']} ({task['category']})")
    print()

def delete_task():
    
    if not tasks:
        print("\n🗑 ไม่มีงานให้ลบ\n")
        return

    show_tasks()
    name = input("🗑 ลำดับงานที่ต้องการลบ: ").strip()

    found = False
    for task in tasks:
        if task["name"] == name:
            tasks.remove(task)
            print(f"✅ ลบงาน: {name} แล้ว\n")
            found = True
            break

    if not found:
        print(f"⚠️ ไม่พบงานชื่อ: {name}\n")

def summarize_tasks():
    if not tasks:
        print("\n📊 ยังไม่มีงานในระบบ\n")
        return
    summary = {}
    for task in tasks:
        cat = task['category']
        summary[cat] = summary.get(cat, 0) + 1
    print("\n📊 สรุปงานตามประเภท:")
    for cat, count in summary.items():
        print(f"- {cat}: {count} งาน")
    print()

def main_menu():
    while True:
        print("====== Smart Farm Task Organizer ======")
        print("1. เพิ่มงานในฟาร์ม")
        print("2. แสดงรายการงานทั้งหมด")
        print("3. ลบงาน")
        print("4. สรุปจำนวนนงานในแต่ละประเภท")
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
            print("👋 ลาก่อน ขอบคุณที่ใช้โปรแกรม Smart Farm!")
            break
        else:
            print("⚠️ กรุณาเลือกเมนูที่ถูกต้อง (1-5)\n")

if __name__ == "__main__":
    main_menu()