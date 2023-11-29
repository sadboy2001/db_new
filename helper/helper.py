from dataclasses import dataclass, asdict

DATABASE_NAME = 'test_database'
TABLE_NAME = 'persons'


@dataclass
class MyDbConfig:
    host: str = 'localhost'
    port: str = '3306'
    user: str = 'mysql_user'
    password: str = 'mysql_password'
    database: str = DATABASE_NAME

    def asdict(self) -> dict:
        return asdict(self)

    def db_url(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'


@dataclass
class PgDbConfig:
    host: str = 'localhost'
    port: str = '5432'
    user: str = 'postgres'
    password: str = 'postgres'
    database: str = DATABASE_NAME

    def asdict(self) -> dict:
        return asdict(self)

    def db_url(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'


def select_from_table(cursor):
    cursor.execute(f'SELECT * FROM {TABLE_NAME};')
    results = cursor.fetchall()

    print(f"\033[92m---> All rows from table '{TABLE_NAME}':\033[0m")
    for row in results:
        print(f'\033[94m{row}\033[0m')
