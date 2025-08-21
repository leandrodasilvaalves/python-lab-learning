import pymongo

INSERT = False
DROP = False


def line():
    print("".ljust(65, "."))


myclient = pymongo.MongoClient("mongodb://root:passw0rd@localhost:27017/")

print(myclient.list_database_names())

db = myclient["myhouse"]
print(db.list_collection_names())

collection = db["people"]

lele = {"name": "Lele", "address": "Parnamirim"}

if INSERT:
    result = collection.insert_one(lele)
    print(result.inserted_id)

    family = [
        {"name": "Meire", "address": "Parnamirim"},
        {"name": "Isa", "address": "Parnamirim"},
        {"name": "Leo", "address": "Parnamirim"},
    ]

    result = collection.insert_many(family)
    print(result.inserted_ids)


person = collection.find_one()
print(person)

line()
for person in collection.find():
    print(person)

# retornando campos selecionados
line()
for person in collection.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(person)

line()
for person in collection.find({}, {"address": 0}):
    print(person)

line()
query= {"name": "Leo"}
doc = collection.find(query)
for person in doc:
    print(person)

line()
query ={"name": {"$gt": "L"}}
doc = collection.find(query)
for person in doc:
    print(person)

line()
query = {"name": {"$regex": "^[iI]"}}
doc = collection.find(query)
for person in doc:
    print(person)

line()
doc = collection.find().sort('name')
for person in doc:
    print(person)

line()
doc = collection.find().sort('name',-1)
for person in doc:
    print(person)

line()
query = {"name": "Leandro"}
collection.delete_one(query)
doc = collection.find()
for person in doc:
    print(person)

if DROP:
    line()
    query = {"address": "Parnamirim"}
    collection.delete_many(query)
    doc = collection.find()
    for person in doc:
        print(person)

    collection.drop()

    collection.insert_one(lele)


line()
query = {"name": "Lele"}
new_values = {"$set":{"address": "Cajupiranga, Parnamirim"}}

collection.update_one(query, new_values)
doc = collection.find_one(query)
print(doc)

line()
query = {'address': 'Parnamirim'}
collection.update_many(query, new_values)
doc = collection.find()
for person in doc:
    print(person)

line()
for person in collection.find().limit(2):
    print(person)