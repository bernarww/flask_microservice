from pymongo import MongoClient

host = '192.168.1.123'
port = 27017
database_name = 'mydatabase'

client = MongoClient(f'mongodb://{host}:{port}/{database_name}')
db = client[database_name]

first_collection = db['first_collection']
data = {'first_key': 'first_value'}
first_result = first_collection.delete_many({})
first_collection.insert_one(data)