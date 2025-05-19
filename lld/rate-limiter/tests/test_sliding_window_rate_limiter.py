import unittest
from unittest.mock import patch
from rate_limiter import SlidingWindowRateLimiter

class TestSlidingWindowRateLimiter(unittest.TestCase):
    @patch('time.time')
    def test_within_window_allows_up_to_max_requests(self, mock_time):
        mock_time.return_value = 1000
        rate_limiter = SlidingWindowRateLimiter(max_requests=5, window_size_seconds=10)
    
        request ={
            'user_id': 'user1'
        }

        for _ in range(5):
            self.assertTrue(rate_limiter.allow_request(request))    
        
        self.assertFalse(rate_limiter.allow_request(request))  # Should be false after 5 requests

    @patch('time.time')
    def test_after_window_allows_new_requests(self, mock_time):
        mock_time.return_value = 1000
        rate_limiter = SlidingWindowRateLimiter(max_requests=5, window_size_seconds=10)
    
        request ={
            'user_id': 'user1'
        }

        for _ in range(5):
            self.assertTrue(rate_limiter.allow_request(request))    
        
        self.assertFalse(rate_limiter.allow_request(request))  # Should be false after 5 requests
        mock_time.return_value += 10

        self.assertTrue(rate_limiter.allow_request(request))  # Should be true after window expires

    @patch('time.time')
    def test_multiple_users(self, mock_time):
        mock_time.return_value = 1000
        rate_limiter = SlidingWindowRateLimiter(max_requests=5, window_size_seconds=10)
    
        request1 = {
            'user_id': 'user1'
        }
        request2 = {
            'user_id': 'user2'
        }

        for _ in range(5):
            self.assertTrue(rate_limiter.allow_request(request1))    
            self.assertTrue(rate_limiter.allow_request(request2))    
        
        self.assertFalse(rate_limiter.allow_request(request1))  # Should be false after 5 requests
        self.assertFalse(rate_limiter.allow_request(request2))  # Should be false after 5 requests
    

if __name__ == '__main__':
    unittest.main()