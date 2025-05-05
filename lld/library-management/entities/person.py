from uuid import uuid4
from datetime import datetime

class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        self._id = str(uuid4())  # Unique ID for each person
        self._created_at = datetime.now()  # Record creation time
        self._updated_at = self._created_at  # Initially same as creation time

    def rename(self, new_name: str):
        """
        Renames the person and updates the last modified timestamp.
        """
        self.name = new_name
        self._updated_at = datetime.now()
        
    def __repr__(self):
        return f"Person(ID={self._id}, Name={self.name}, Age={self.age}, Gender={self.gender}, CreatedAt={self._created_at}, UpdatedAt={self._updated_at})"
