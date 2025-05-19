from rate_limiter.limiter_factory import get_rate_limiter
import time

def main():
    limiter = get_rate_limiter("fixed_window", {"max_requests": 5, "window_size": 10})
    user_id = "user_123"
    for i in range(10):
        if limiter.allow_request(user_id):
            print(f"Request {i + 1} allowed")
        else:
            print(f"Request {i + 1} denied")
        time.sleep(1)  # Simulate a delay between requests
if __name__ == "__main__":
    main()