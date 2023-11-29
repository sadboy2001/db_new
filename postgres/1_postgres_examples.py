import psycopg2
from helper.helper import TABLE_NAME, PgDbConfig
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Create connection to BD
connection = psycopg2.connect(**PgDbConfig().asdict())

# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor object
cursor = connection.cursor()

create_table_stmt = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL
);
"""

cursor.execute(create_table_stmt)

cursor.execute(f"SELECT * FROM {TABLE_NAME};")
# Fetch the results
results = cursor.fetchall()
if results:
    for row in results:
        print(row)
else:
    print(f'Table {TABLE_NAME} is empty!')

connection.commit()

cursor.close()
connection.close()
