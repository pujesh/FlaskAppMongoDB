import mongoengine as db

class Test(db.Document):
    name = db.StringField()
    reason = db.StringField()
    meta = {
        'collection' : 'test_collection'
    }