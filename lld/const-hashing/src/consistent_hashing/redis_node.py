# src/consistent_hashing/redis_node.py

from .node import Node
import redis

class RedisNode(Node):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = redis.Redis(host=host, port=port)

    def get_id(self) -> str:
        return f"{self.host}:{self.port}"

    def set(self, key: str, value: str):
        self.client.set(key, value)

    def get(self, key: str) -> str:
        return self.client.get(key)

    def __repr__(self):
        return f"RedisNode({self.get_id()})"
