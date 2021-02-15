from pymongo import MongoClient
from post import post

#insert data in collections
def insert(collection):
    posts.insert_many(collection)

#delete data in collections
def delete(id):
    posts.delete_one(id)

#update data in collections
def update(id,value_update):
    posts.update_one(id,value_update)

#find document using find_one()
def find():
    for i in posts.find():
        print(i)

#show all data with value
def sort(value):
    sort_value = posts.find().sort(value)
    
    for i in sort_value:
        print(i)


#making conection with MongoClient
client = MongoClient('localhost',27017)

#create datase
db = client.blog
# db = client['test_database'] - format dictionary

#create collections
posts = db.posts
# collection = db['test_collection'] - format dictionary


insert(post)
find()
print('----------------')

update({'id':1}, {'$set': {'author' : 'gabriel'}})
find()
print('----------------')

delete({'id' : 2})
find()
posts.delete_many({})