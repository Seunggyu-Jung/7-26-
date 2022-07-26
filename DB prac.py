from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.mvesofx.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'bob',
    'age':26
}

db.users.insert_one(doc)