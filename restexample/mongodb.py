class MongoDB(object):
    mongo = None

    @staticmethod
    def get_mongodb():
        if MongoDB.mongo is None:
            raise RuntimeError("Did not call set_mongodb before get_mongodb")
        return MongoDB.mongo

    @staticmethod
    def set_mongodb(mongodb):
        MongoDB.mongo = mongodb
