from entities.item import Item


class CD(Item):
    def __init__(self, title: str, artist: str, duration_minutes: float):
        super().__init__(title)
        self.artist = artist
        self.duration = duration_minutes

    def __repr__(self):
        return f"CD(id={self._id}, title={self.title}, artist={self.artist}, duration={self.duration} mins)"
    
    @classmethod
    def build(cls, title: str, artist: str, duration_minutes: float):
        return cls(title=title, artist=artist, duration_minutes=duration_minutes)