import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='zxc12345',
                                    database='demo')

cursor = connection.cursor()


# 取得所有員工資料
print("取得所有員工資料")
cursor.execute("SELECT * FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得所有客戶資料
print("取得所有客戶資料")
cursor.execute("SELECT * FROM client;")
records = cursor.fetchall()
for r in records:
    print(r)


# 按薪水低到高取得員工資料
print("按薪水低到高取得員工資料")
cursor.execute("SELECT * FROM employee ORDER BY salary ASC;")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得薪水前3高的員工
print("取得薪水前3高的員工")
cursor.execute("SELECT * FROM employee ORDER BY salary DESC LIMIT 3;")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得所有員工的名子 
print("取得所有員工的名子")
cursor.execute("SELECT name FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)
    
  
# 取得不重複的部門id
print("取得不重複的部門id")
cursor.execute("SELECT DISTINCT branch_id FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得所有員工人數
print("取得所有員工人數")
cursor.execute("SELECT COUNT(*) FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得有主管的員工人數
print("取得有主管的員工人數")
cursor.execute("SELECT COUNT(sup_id) FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)
    
    
# 取得所有出生於 1970-01-01 之後的女性員工人數
print("取得所有出生於 1970-01-01 之後的女性員工人數")
cursor.execute("SELECT COUNT(*) FROM employee WHERE birth_date > '1970-01-01' AND sex = 'F';")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得所有員工的平均薪水
print("取得所有員工的平均薪水")
cursor.execute("SELECT AVG(salary) FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)
    
    
# 取得所有員工薪水的總和
print("取得所有員工薪水的總和")
cursor.execute("SELECT SUM(salary) FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得薪水最高的員工
print("取得薪水最高的員工")
cursor.execute("SELECT MAX(salary) FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得薪水最低的員工
print("取得薪水最低的員工")
cursor.execute("SELECT MIN(salary) FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得電話號碼尾數是335的客戶
print("取得電話號碼尾數是335的客戶")
cursor.execute("SELECT * FROM client WHERE phone LIKE '%335';")
records = cursor.fetchall()
for r in records:
    print(r)
    
    
# 取得電話號碼開頭是256的客戶
print("取得電話號碼開頭是256的客戶")
cursor.execute("SELECT * FROM client WHERE phone LIKE '256%';")
records = cursor.fetchall()
for r in records:
    print(r)
    
    
# 取得電話號碼中間是354的客戶
print("取得電話號碼中間是354的客戶")
cursor.execute("SELECT * FROM client WHERE phone LIKE '%354%';")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得姓艾的客戶
print("取得姓艾的客戶")
cursor.execute("SELECT * FROM client WHERE client_name LIKE '艾%';")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得生日在12月的員工
print("取得生日在12月的員工")
cursor.execute("SELECT * FROM employee WHERE birth_date LIKE '____-12-__';")
records = cursor.fetchall()
for r in records:
    print(r)


# 取得生日在9月的員工
print("取得生日在9月的員工")
cursor.execute("SELECT * FROM employee WHERE birth_date LIKE '____-09-__';")
records = cursor.fetchall()
for r in records:
    print(r)


# 員工名子 union 客戶名子
print("員工名子 union 客戶名子")
cursor.execute("SELECT name FROM employee UNION SELECT client_name FROM client;")
records = cursor.fetchall()
for r in records:
    print(r)


# 員工id union 客戶id
print("員工id union 客戶id")
cursor.execute("SELECT emp_id FROM employee UNION SELECT client_id FROM client;")
records = cursor.fetchall()
for r in records:
    print(r)


# 員工薪水 union 銷售金額
print("員工薪水 union 銷售金額")
cursor.execute("SELECT salary FROM employee UNION SELECT total_sales FROM works_with;")
records = cursor.fetchall()
for r in records:
    print(r)


# 將employee表格與branch表格合併後,搜尋所有部門經理資訊
print("取得employee表格與branch表格合併後所有部門經理資訊")
cursor.execute("SELECT * FROM employee JOIN branch ON emp_id = manager_id;")
records = cursor.fetchall()
for r in records:
    print(r)
    
    
# 同上,但只顯示員工id,員工名稱,部門名稱
print("同上,但只顯示員工id,員工名稱,部門名稱")
cursor.execute("SELECT emp_id, name, branch_name FROM employee JOIN branch ON emp_id = manager_id;")
records = cursor.fetchall()
for r in records:
    print(r)


# 同上,但改用表格.欄位設定
print("同上,但改用表格.欄位設定")
cursor.execute("SELECT employee.emp_id, employee.name, branch.branch_name FROM employee JOIN branch ON employee.emp_id = branch.manager_id;")
records = cursor.fetchall()
for r in records:
    print(r)
    
    
# 同上,但是將JOIN改成LEFT JOIN
print("同上,但是將JOIN改成LEFT JOIN")
cursor.execute("SELECT employee.emp_id, employee.name, branch.branch_name FROM employee LEFT JOIN branch ON employee.emp_id = branch.manager_id;")
records = cursor.fetchall()
for r in records:
    print(r)
    
    
# 同上,但是將JOIN改成RIGHT JOIN
print("同上,但是將JOIN改成RIGHT JOIN")
cursor.execute("SELECT employee.emp_id, employee.name, branch.branch_name FROM employee RIGHT JOIN branch ON employee.emp_id = branch.manager_id;")
records = cursor.fetchall()
for r in records:
    print(r)


# 找出研發部門的經理名稱
print("找出研發部門的經理名稱")
cursor.execute("SELECT name FROM employee WHERE emp_id=(SELECT manager_id FROM branch WHERE branch_name='研發');")
records = cursor.fetchall()
for r in records:
    print(r)

# 找出單一客戶銷售金額超過50000的員工名稱
print("找出單一客戶銷售金額超過50000的員工名稱")
cursor.execute("SELECT name FROM employee WHERE emp_id IN (SELECT emp_id FROM works_with WHERE total_sales >50000);")
records = cursor.fetchall()
for r in records:
    print(r)


# 中斷資料庫連線
cursor.close()
connection.close()