from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

storage = DBStorage() if (getenv("HBNB_TYPE_STORAGE") == "db") \
    else FileStorage()
storage = DBStorage()

storage.reload()