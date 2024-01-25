import pymongo
import random
from time import time
t = time()
print(time() - t)

client = pymongo.MongoClient('mongodb://localhost', 27017)

print('resetting everything')
client.test.test.delete_many({})

if client.test.test.find_one({}) is None:
    print('creating stuff because test has nothing in it')

    t = time()
    client.test.test.insert_many({
        'path': random.random(),
        'views': random.randint(1, 3)
    } for i in range(10000))
    print(time() - t)


print(client.test.test.count_documents({}))

t = time()
x = client.test.test.find({'views': 1})
print(time() - t)

t = time()
y = x.limit(5)
print(time() - t)

for document in y:
    print(document)
