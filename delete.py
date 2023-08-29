import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='zxc12345',
                                    database='demo')

cursor = connection.cursor()


# 刪除Employee小綠資料
print("刪除Employee小綠資料")
cursor.execute("DELETE FROM employee WHERE name='小綠';")

print("取得employee表格資料")
cursor.execute("SELECT * FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)

print("取得branch表格資料")
cursor.execute("SELECT * FROM branch;")
records = cursor.fetchall()
for r in records:
    print(r)

print("取得works_with表格資料")
cursor.execute("SELECT * FROM works_with;")
records = cursor.fetchall()
for r in records:
    print(r)


# 刪除表格資料
cursor.execute("DELETE FROM employee;")
cursor.execute("DELETE FROM branch;")
cursor.execute("DELETE FROM client;")
cursor.execute("DELETE FROM works_with;")


# 刪除資料庫
cursor.execute("DROP DATABASE demo;")


# 中斷資料庫連線
cursor.close()
connection.close()