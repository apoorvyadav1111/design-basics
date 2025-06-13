import hashlib

def hash_md5(key: str) -> int:
    """
    Generate a hash value for the given key using MD5.
    
    Args:
        key (str): The key to hash.
        
    Returns:
        int: The hash value as an integer.
    """
    h = hashlib.md5(key.encode()).hexdigest()
    return int(h, 16)

