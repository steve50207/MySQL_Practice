import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='zxc12345',
                                    database='demo')

cursor = connection.cursor()

# 解除安全更新模式（safe update mode),開啟批次更新
cursor.execute("SET SQL_SAFE_UPDATES = 0;")


# 插入資料至branch表格,manager_id需要等employee表格建立後再更新(foreign key關聯)
cursor.execute("INSERT INTO branch VALUES(1, '研發', NULL);")
cursor.execute("INSERT INTO branch VALUES(2, '行政', NULL);")
cursor.execute("INSERT INTO branch VALUES(3, '資訊', NULL);")


# 插入資料至employee表格
cursor.execute("INSERT INTO employee VALUES(206, '小黃', '1998-10-08', 'F', 50000, 1, NULL);")
cursor.execute("INSERT INTO employee VALUES(207, '小綠', '1985-09-16', 'M', 29000, 2, 206);")
cursor.execute("INSERT INTO employee VALUES(208, '小黑', '2000-12-19', 'M', 35000, 3, 206);")
cursor.execute("INSERT INTO employee VALUES(209, '小白', '1997-01-22', 'F', 39000, 3, 207);")
cursor.execute("INSERT INTO employee VALUES(210, '小蘭', '1925-11-10', 'F', 84000, 1, 207);")


# 新增branch表格資料,manager_id需要等employee表格建立後再更新(foreign key關聯)
cursor.execute("UPDATE branch SET manager_id=206 WHERE branch_id=1;")
cursor.execute("UPDATE branch SET manager_id=207 WHERE branch_id=2;")
cursor.execute("UPDATE branch SET manager_id=208 WHERE branch_id=3;")


# 插入資料至client表格
cursor.execute("INSERT INTO client VALUES(400, '阿狗', 254354335);")
cursor.execute("INSERT INTO client VALUES(401, '阿貓', 25633899);")
cursor.execute("INSERT INTO client VALUES(402, '旺來', 45354345);")
cursor.execute("INSERT INTO client VALUES(403, '露西', 54354365);")
cursor.execute("INSERT INTO client VALUES(404, '艾瑞克', 18783783);")


# 插入資料至works_with表格
cursor.execute("INSERT INTO works_with VALUES(206, 400, 70000);")
cursor.execute("INSERT INTO works_with VALUES(207, 401, 24000);")
cursor.execute("INSERT INTO works_with VALUES(208, 400, 9800);")
cursor.execute("INSERT INTO works_with VALUES(208, 403, 24000);")
cursor.execute("INSERT INTO works_with VALUES(210, 404, 87940);")


# 查詢表格資料
print("取得employee表格資料")
records = cursor.execute("SELECT * FROM employee;")
records = cursor.fetchall()
for r in records:
    print(r)
    
    
print("取得branch表格資料")
records = cursor.execute("SELECT * FROM branch;")
records = cursor.fetchall()
for r in records:
    print(r)


print("取得client表格資料")
records = cursor.execute("SELECT * FROM client;")
records = cursor.fetchall()
for r in records:
    print(r)


print("取得works_with表格資料")
records = cursor.execute("SELECT * FROM works_with;")
records = cursor.fetchall()
for r in records:
    print(r)


# 中斷資料庫連線
cursor.close()
connection.commit() # 更動資料內容需要輸入commit()指令才會生效
connection.close()