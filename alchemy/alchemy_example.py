from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

from helper.helper import TABLE_NAME, PgDbConfig


# Create a SQLAlchemy engine object
engine = create_engine(PgDbConfig().db_url())

# # Create a base class for declarative models
Base = declarative_base()


# Define the model for the "persons" table
class PersonsTable(Base):
    __tablename__ = TABLE_NAME

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)


# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a new record
session = Session()
new_record = PersonsTable(name="John Snow", age=30)
session.add(new_record)
session.commit()

# Create several records
session = Session()
many_records = [
    PersonsTable(name="Kate", age=20),
    PersonsTable(name="Mike", age=30),
    PersonsTable(name="Anton", age=40),
]
session.add_all(many_records)
session.commit()

# Query all the records
query = session.query(PersonsTable)
results = query.all()
for row in results:
    print(row.id, row.name, row.age)

# Query the records with predicate
query = session.query(PersonsTable).filter(PersonsTable.age > 25)
results = query.all()
print('-> Query with predicate: age > 25')
for row in results:
    print(row.id, row.name, row.age)

# Query the records with predicate
query = session.query(PersonsTable).filter(
    PersonsTable.age > 25,
    PersonsTable.name.startswith('A')
)
results = query.all()
print('-> Query with predicate: age > 25 and name start with "A"')
for row in results:
    print(row.id, row.name, row.age)

# Close the session
session.close()
