import time
from collections import defaultdict
from rate_limiter import RateLimiter

class FixedWindowRateLimiter(RateLimiter):
    def __init__(self, max_requests: int, window_size: int):
        """
        Initializes the FixedWindowRateLimiter with a maximum number of requests and a time window.

        :param max_requests: The maximum number of requests allowed in the time window.
        :param window_size: The size of the time window in seconds.
        """
        
        super().__init__()
        self.max_requests = max_requests
        self.window_size = window_size
        self.user_requests = defaultdict(lambda:{"count": 0, "window_start": 0})
    
    def allow_request(self, request) -> bool:
        """
        Determines if a request from a user should be allowed based on the fixed window rate limiting policy.
        :param request: The request object. It should contain a user_id to identify the user.
        :return: True if the request is allowed, False otherwise.
        """

        current_time = int(time.time())
        user_id = request["user_id"]
        user_dataa = self.user_requests[user_id]

        window_start = user_dataa["window_start"]

        if current_time >= window_start + self.window_size:
            # Reset the window
            user_dataa["window_start"] = current_time
            user_dataa["count"] = 1
            return True
        else:
            if user_dataa["count"] < self.max_requests:
                user_dataa["count"] += 1
                return True
            else:
                return False
