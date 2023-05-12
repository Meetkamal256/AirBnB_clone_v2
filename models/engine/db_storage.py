#!/usr/bin/python3
"""
database engine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """database engine"""
    
    __engine = None
    __session = None
    
    def __init__(self):
        """init"""
        
        url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB"),
        )
        self.__engine = create_engine(url, pool_pre_ping=True, echo=False)
    
    def all(self, cls=None):
        """Query the database session to retrieve all objects depending on the class name"""
        
        # Import the necessary classes for querying from the database
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        
        # Create an empty dictionary to store the retrieved objects
        objects = {}
    
        if cls is None:
            # If no class is specified, retrieve objects from all classes
            classes = [State, City, User, Place, Review, Amenity]
            
            for class_ in classes:
                # Query the session for all objects of the class
                objects_list = self.__session.query(class_).all()
                
                for obj in objects_list:
                    # Generate a key using the class name and object ID
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    # Store the object in the dictionary using the key
                    objects[key] = obj
        
        else:
            # If a class is specified, retrieve objects from that class only
            objects_list = self.__session.query(cls).all()
            
            for obj in objects_list:
                # Generate a key using the class name and object ID
                key = f"{obj.__class__.__name__}.{obj.id}"
                # add the object in the dictionary using the key
                objects[key] = obj
        
        # Return the dictionary containing the retrieved objects
        return objects
    
    def new(self, obj):
        """UPDATE!!!"""
        self.__session.add(obj)
    
    def save(self):
        """UPDATE!!!"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """UPDATE!!!"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """UPDATE!!!"""
        from models.base_model import Base
        
        Base.metadata.create_all(self.__engine)
        
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        
        self.__session = scoped_session(session)()
    
    def close(self):
        """method on the private session attribute"""
        self.__session.close()
