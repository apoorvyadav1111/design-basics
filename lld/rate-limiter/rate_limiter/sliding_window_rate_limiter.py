import time
from collections import deque, defaultdict
from rate_limiter.rate_limiter import RateLimiter

class SlidingWindowRateLimiter(RateLimiter):
    def __init__(self, max_requests: int, window_size_seconds:int):
        super().__init__()
        self.max_requests = max_requests
        self.window_size = window_size_seconds
        self.request_timestamps = defaultdict(deque)
    
    def allow_request(self, request):
        current_time = time.time()  
        user_id = request["user_id"]
        

        while self.request_timestamps[user_id] and self.request_timestamps[user_id][0] <= current_time - self.window_size:
            self.request_timestamps[user_id].popleft()
        
        if len(self.request_timestamps[user_id]) < self.max_requests:
            self.request_timestamps[user_id].append(current_time)
            return True
        else:
            return False
