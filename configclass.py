class Config(object):
    MONGODB_SETTINGS = {
        'db' : 'test',
        'host' : 'localhost',
        'port' : 27017
    }

class ProductionConfig(object):
    MONGODB_SETTINGS = {
        'db' : <production_db>,
        'host' : <production_host>,
        'port' : <production_port>
    }