from .node import Node

class DummyResource(Node):
    def __init__(self, name: str):
        """
        Initializes a DummyResource with a given name.
        
        :param name: The name of the resource.
        """
        self.name = name
    
    def get_id(self) -> str:
        """
        Returns the name of the resource as its unique identifier.
        
        :return: The name of the resource.
        """
        return self.name

    def __repr__(self) -> str:
        """
        Returns a string representation of the DummyResource.
        
        :return: A string representation of the DummyResource.
        """
        return f"DummyResource(name={self.name})"
    
