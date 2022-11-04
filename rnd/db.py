from tinydb import TinyDB, Query

db = TinyDB("db.json")

query = Query()
# db.insert({"id": 0, "type": "text", "content": "this is a clippy!", "date": 202211011222})
# db.insert({"id": 1, "type": "image", "content": "this is an image", "date": 202211011224})
# db.insert({"id": 2, "type": "url", "content": "htts://google.com", "date": 202211011226})
# db.truncate()

result = db.search((query.id < 2) & (query.type == "image"))

print(result)