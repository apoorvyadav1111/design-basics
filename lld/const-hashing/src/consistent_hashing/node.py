from abc import ABC, abstractmethod

class Node(ABC):

    @abstractmethod
    def get_id(self) -> str:
        """
        Returns a unique identifier for the node.
        This identifier is used in the consistent hashing algorithm.
        """
        pass
