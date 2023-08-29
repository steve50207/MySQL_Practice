import mysql.connector

# 建立資料庫連線
connection = mysql.connector.connect(host="localhost",
                                     port="3306",
                                     user="root",
                                     password="zxc12345")
cursor = connection.cursor()


# 創建資料庫
cursor.execute("CREATE DATABASE demo;")


# 選擇資料庫
cursor.execute("USE demo;")


# 取得所有資料庫名稱
print("取得所有資料庫名稱")
cursor.execute("SHOW DATABASES;")
records = cursor.fetchall()
for r in records:
    print(r)


# 建立employee表格
cursor.execute("CREATE TABLE employee(emp_id INT , name VARCHAR(20), birth_date DATE, sex VARCHAR(1), salary INT, branch_id  INT, sup_id INT, PRIMARY KEY(emp_id));")

# 建立branch表格
cursor.execute("CREATE TABLE branch(branch_id INT, branch_name VARCHAR(20), manager_id INT, PRIMARY KEY(branch_id), FOREIGN KEY(manager_id) REFERENCES employee(emp_id) ON DELETE SET NULL);")

# employee表格補上Foreign Key設定
cursor.execute("ALTER TABLE employee ADD FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL;")
cursor.execute("ALTER TABLE employee ADD FOREIGN KEY(sup_id) REFERENCES employee(emp_id) ON DELETE SET NULL;")


# 建立client表格
cursor.execute("CREATE TABLE client(client_id INT, client_name VARCHAR(20), phone INT, PRIMARY KEY(client_id));")


# 建立works_with表格
cursor.execute("CREATE TABLE works_with(emp_id INT, client_id INT, total_sales INT,	PRIMARY KEY(emp_id,client_id), FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE, FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE);") 


# 取得所有表格名稱
print("取得所有表格名稱")
cursor.execute("SHOW TABLES;")
records = cursor.fetchall()
for r in records:
    print(r)


# 查詢表格欄位資訊
print("取得employee表格欄位資訊")
records = cursor.execute("DESCRIBE employee;")
records = cursor.fetchall()
for r in records:
    print(r)

print("取得branch表格欄位資訊")
records = cursor.execute("DESCRIBE branch;")
records = cursor.fetchall()
for r in records:
    print(r)

print("取得client表格欄位資訊")
records = cursor.execute("DESCRIBE client;")
records = cursor.fetchall()
for r in records:
    print(r)

print("取得works_with表格欄位資訊")
records = cursor.execute("DESCRIBE works_with;")
records = cursor.fetchall()
for r in records:
    print(r)

# 中斷資料庫連線
cursor.close()
connection.close()
