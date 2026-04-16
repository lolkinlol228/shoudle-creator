import sqlite3

conn = sqlite3.connect(r'C:\Users\user\Desktop\project\schedule.db')
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(schedules);")
columns = cursor.fetchall()
print("Колонки таблицы schedules:")
for col in columns:
    print(col)

conn.close()
