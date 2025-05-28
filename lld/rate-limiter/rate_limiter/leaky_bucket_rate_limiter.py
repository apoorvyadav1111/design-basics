from rate_limiter import RateLimiter
import time
from collections import defaultdict

class LeakyBucket:
    def __init__(self, capacity: int, leak_rate: float):
        """
        Initialize the Leaky Bucket.

        :param capacity: The maximum number of requests that can be processed at once.
        :param leak_rate: The rate at which requests are processed (requests per second).
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_level = 0.0
        self.last_leak_time = time.time()

    def _leak(self):
        now = time.time()
        elapsed_time = now - self.last_leak_time
        leaked_amount = elapsed_time * self.leak_rate
        self.current_level = max(0.0, self.current_level - leaked_amount)
        self.last_leak_time = now

    def allow_request(self):
        self._leak()
        if self.current_level < self.capacity:
            self.current_level += 1.0
            return True
        return False
    
class LeakyBucketRateLimiter(RateLimiter):
    def __init__(self, capacity: int, leak_rate: float):
        """
        Initialize the Leaky Bucket Rate Limiter.

        :param capacity: The maximum number of requests that can be processed at once.
        :param leak_rate: The rate at which requests are processed (requests per second).
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.buckets = defaultdict(lambda: LeakyBucket(capacity, leak_rate))


    def allow_request(self, request):
        bucket = self.buckets[request['user_id']]
        return bucket.allow_request()