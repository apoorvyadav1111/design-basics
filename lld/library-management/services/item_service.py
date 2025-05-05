class ItemService:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        for item in self.items:
            if item._id == item_id:
                self.items.remove(item)
                return True
        return False

    def get_item(self, item_id):
        for item in self.items:
            if item._id == item_id:
                return item
        return None

    def list_items(self):
        return self.items
    