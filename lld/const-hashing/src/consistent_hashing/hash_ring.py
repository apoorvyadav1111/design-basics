from bisect import bisect
from .utils import hash_md5
from .node import Node


class ConsistentHashRing:
    def __init__(self, virtual_nodes: int = 3):
        """
        Initializes the ConsistentHashRing with a specified number of virtual nodes.
        
        :param virtual_nodes: The number of virtual nodes to create for each real node.
        """
        self.virtual_nodes = virtual_nodes
        self.ring = []
        self.hash_to_nodes = dict()
    
    def __get_virtual_node_key(self, node: Node, index: int) -> str:
        """
        Generates a virtual node key for a given node and index.
        
        :param node: The node for which to generate the key.
        :param index: The index of the virtual node.
        :return: A string representing the virtual node key.
        """
        return f"{node.get_id()}#{index}"
    
    def add_node(self, node: Node):
        for i in range(self.virtual_nodes):
            vnode_key = self.__get_virtual_node_key(node, i)
            hash_value = hash_md5(vnode_key)
            self.ring.append(hash_value)
            self.hash_to_nodes[hash_value] = node
        self.ring.sort()

    def get_node(self, key: str) -> Node:
        if not self.ring:
            raise ValueError("No nodes in the hash ring")
        
        hash_value = hash_md5(key)
        idx = bisect(self.ring, hash_value) % len(self.ring)
        return self.hash_to_nodes[self.ring[idx]]

    def remove_node(self, node: Node):
        for i in range(self.virtual_nodes):
            vnode_key = self.__get_virtual_node_key(node, i)
            hash_value = hash_md5(vnode_key)
            if hash_value in self.hash_to_nodes:
                del self.hash_to_nodes[hash_value]
                self.ring.remove(hash_value)