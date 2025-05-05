from entities.librarian import Librarian

class LibrarianService:
    def __init__(self):
        self.librarians = {}

    def add_librarian(self, name:str, age:int, gender:str):
        new_librarian = Librarian(name, age,gender)
        self.librarians[new_librarian._id] = new_librarian
        return new_librarian
    
    def get_librarian(self, librarian_id:str):
        return self.librarians.get(librarian_id, None)
    
    def remove_librarian(self, librarian_id:str):
        if librarian_id in self.librarians:
            del self.librarians[librarian_id]
            return True
        return False
    
    def list_librarians(self):
        return list(self.librarians.values())
    
    