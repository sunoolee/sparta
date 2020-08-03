from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

docs = list(db.movies.find({'star' : '9.40'}))
print(docs)

for doc in docs:
    print(doc['title'])




# target_movie = db.movies.find_one({'title' : '월-E'})
# target_star = (target_movie['star'])
#
#
# movies = list(db.movies.find({'star': target_star}))
#
# for movie in movies:
#     print(movie['title'])
#     db.movies.update_many({'star': target_star}, {'$set': {'star': '0'}})
#     print(movie['star'])