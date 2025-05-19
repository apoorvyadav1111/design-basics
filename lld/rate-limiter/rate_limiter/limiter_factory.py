from .fixed_window_rate_limiter import FixedWindowRateLimiter
from rate_limiter import RateLimiter

def get_rate_limiter(strategy: str, config: dict) -> RateLimiter:
    """
    Factory function to get the appropriate rate limiter based on the strategy.

    :param strategy: The rate limiting strategy to use (e.g., "fixed_window").
    :param config: Configuration parameters for the rate limiter.
    """
    if strategy == "fixed_window":
        max_requests = config.get("max_requests", 100)
        window_size = config.get("window_size", 60)
        return FixedWindowRateLimiter(max_requests, window_size)
    else:
        raise ValueError(f"Unknown rate limiting strategy: {strategy}")