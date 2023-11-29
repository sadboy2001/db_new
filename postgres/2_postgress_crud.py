import psycopg2
from helper.helper import TABLE_NAME, PgDbConfig, select_from_table

connection = psycopg2.connect(**PgDbConfig().asdict())
cursor = connection.cursor()

# # CREATE (INSERT...)
insert_stmt = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s);'
data = [
    ('Sofia', 22),
    ('Alex', 28)
]

cursor.execute(insert_stmt, ('Alice', 20))
cursor.execute(insert_stmt, ('Bob', 30))
# connection.commit()


# with psycopg2.connect(**PgDbConfig().asdict()) as conn:
#     with conn.cursor() as curr:
#         curr.executemany(insert_stmt, data)


# READ (SELECT...)
cursor.execute(f'SELECT * FROM {TABLE_NAME};')
results = cursor.fetchall()

for row in results:
    print(row)

# UPDATE (UPDATE...)

update_stmt = f'UPDATE {TABLE_NAME} set age=%s WHERE name=%s'
cursor.execute(update_stmt, (100, 'Bob'))

select_from_table(cursor)

# DELETE (DELETE...)
cursor.execute(f'DELETE FROM {TABLE_NAME} where name=%s', ('Alice',))
select_from_table(cursor)
# connection.commit()

cursor.close()
connection.close()
