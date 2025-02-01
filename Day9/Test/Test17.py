#databaseclass
from abc import ABC, abstractmethod

class Idatabase(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def select(self):
        pass

class SQLdatabase(Idatabase):
    def insert(self):
        print("Inserting into SQL database")
    
    def delete(self):
        print("Deleting from SQL database")
    
    def update(self):
        print("Updating SQL database")
    
    def select(self):
        print("Selecting from SQL database")

class NoSQLdatabase(Idatabase):
    def insert(self):
        print("Inserting into NoSQL database")
    
    def delete(self):
        print("Deleting from NoSQL database")
    
    def update(self):
        print("Updating NoSQL database")
    
    def select(self):
        print("Selecting from NoSQL database")

sqldb = SQLdatabase()
sqldb.insert()
sqldb.delete()
sqldb.update()
sqldb.select()
nosqldb = NoSQLdatabase()
nosqldb.insert()
nosqldb.delete()
nosqldb.update()
nosqldb.select()