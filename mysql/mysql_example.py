import mysql.connector
from helper.helper import MyDbConfig, TABLE_NAME, select_from_table

# establish a connection
conn = mysql.connector.connect(**MyDbConfig().asdict())

# create a table
cursor = conn.cursor()
cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INT PRIMARY KEY, name VARCHAR(255), age INT)')
cursor.execute(f'DELETE FROM {TABLE_NAME}')

# insert some data
data = [
    (1, 'Alice', 30),
    (2, 'Bob', 35),
    (3, 'Charlie', 25),
]
cursor.executemany(f'INSERT INTO {TABLE_NAME} (id, name, age) VALUES (%s, %s, %s)', data)
conn.commit()

# query the data
cursor.execute(f'SELECT * FROM {TABLE_NAME}')
results = cursor.fetchall()

# print the results
for row in results:
    print(row)

update_stmt = f'UPDATE {TABLE_NAME} set age=%s WHERE name=%s'
cursor.execute(update_stmt, (100, 'Bob'))
select_from_table(cursor)

# DELETE (DELETE...)
cursor.execute(f'DELETE FROM {TABLE_NAME} where name=%s', ('Alice',))
select_from_table(cursor)

cursor.close()
# close the connection
conn.close()
