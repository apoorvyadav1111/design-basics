# main.py

from src.consistent_hashing.hash_ring import ConsistentHashRing
from src.consistent_hashing.redis_node import RedisNode

ring = ConsistentHashRing(virtual_nodes=10)

# Add Redis nodes
nodes = [
    RedisNode("localhost", 6379),
    RedisNode("localhost", 6380),
    RedisNode("localhost", 6381)
]

for node in nodes:
    ring.add_node(node)

# Set some keys
for i in range(10):
    key = f"user:{i}"
    node = ring.get_node(key)
    node.set(key, f"value_{i}")
    print(f"SET {key} → {node.get_id()}")

# Get keys back
for i in range(10):
    key = f"user:{i}"
    node = ring.get_node(key)
    value = node.get(key)
    print(f"GET {key} → {value} from {node.get_id()}")
 