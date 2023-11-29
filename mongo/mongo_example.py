import pymongo

from helper import MongoConfig, print_green, print_blue

# connect to the MongoDB server
client = pymongo.MongoClient(MongoConfig().db_url())

# create a new database and collection
db = client['test_database']
collection = db['persons']


# insert a document into the collection
document = {'name': 'Alice', 'age': '20', 'email': 'something@something.com'}
document_2 = {'name': 'Bob', 'age': '30', 'email': 'bob@something.com'}
result = collection.insert_one(document)
print(result.inserted_id)
collection.insert_one(document_2)


# query the collection for all documents
documents = collection.find()
for document in documents:
    # print(document['_id'], document['name'], document['age'])
    print(document)


print_green('=== Search results 1 === ')
# query the collection for documents that match a specific condition
documents = collection.find({'name': 'Alice'})
for document in documents:
    print_blue(document)


print_green('=== Search results 2 === ')
documents = collection.find({'email': 'bob@something.com'})
for document in documents:
    print(document['_id'], document['name'], document.get('age'), document.get('email'))
