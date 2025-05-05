from entities.item import Item


class Magazine(Item):
    def __init__(self, title: str, issue_number: int, publisher: str):
        super().__init__(title)
        self.issue_number = issue_number
        self.publisher = publisher

    def __repr__(self):
        return f"Magazine(id={self._id}, title={self.title}, issue={self.issue_number}, publisher={self.publisher})"

    @classmethod
    def build(cls, title: str, issue_number: int, publisher: str):
        return cls(title=title, issue_number=issue_number, publisher=publisher)
    