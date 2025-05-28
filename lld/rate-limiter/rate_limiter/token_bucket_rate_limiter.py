import time
from rate_limiter.rate_limiter import RateLimiter
from collections import defaultdict

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        """
        Initialize the Token Bucket.

        :param capacity: The maximum number of tokens in the bucket.
        :param refill_rate: The rate at which tokens are added to the bucket (tokens per second).
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_time = time.time()

    def _refill(self):
        now = time.time()
        elapsed_time = now - self.last_refill_time
        tokens_to_add = elapsed_time * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = now

    def allow(self) -> bool:
        self._refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
    
class TokenBucketRateLimiter(RateLimiter):
    def __init__(self, capacity: int, refill_rate: float):
        """
        Initialize the Token Bucket Rate Limiter.

        :param capacity: The maximum number of tokens in the bucket.
        :param refill_rate: The rate at which tokens are added to the bucket (tokens per second).
        """
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.user_buckets = defaultdict(self._create_user_bucket)

    def _create_user_bucket(self):

        return TokenBucket(self.tokens, self.refill_rate)

    def allow_request(self, request):
        user_id = request["user_id"]
        return self.user_buckets[user_id].allow()