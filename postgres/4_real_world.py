import psycopg2.extras
from helper.helper import TABLE_NAME, PgDbConfig
from dataclasses import dataclass
from pydantic import BaseModel
from mongo.helper import print_blue, print_green


class Person(BaseModel):
    name: str
    age: int


@dataclass
class Person2:
    id: int
    name: str
    age: int

    # @classmethod
    # def from_row(cls, values: dict):
    #     values = {k: v for k, v in values.items() if k != 'id'}
    #     return cls(**values)


insert_stmt = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s);'
data = [
    ('Sofia', 22),
    ('Alex', 28)
]

with psycopg2.connect(**PgDbConfig().asdict()) as conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curr:
        curr.executemany(insert_stmt, data)

        # READ (SELECT...)
        curr.execute(f'SELECT * FROM {TABLE_NAME};')
        results = curr.fetchall()

        persons = [Person.parse_obj(row) for row in results]
        print_blue('From pydantic -->')
        print_blue(persons)

        print_green('From dataclass -->')
        persons = [Person2(**row) for row in results]
        print_green(persons)
