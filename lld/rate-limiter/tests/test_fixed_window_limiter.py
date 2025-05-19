import unittest
from unittest.mock import patch
from rate_limiter.fixed_window_rate_limiter import FixedWindowRateLimiter

class TestFixedWindowRateLimiter(unittest.TestCase):
    @patch('time.time')
    def test_allow_request_within_window(self, mock_time):
        limiter = FixedWindowRateLimiter(max_requests=3, window_size=60)
        
        mock_time.return_value = 1000
        user_id = "user_123"
        request = {
            'user_id': user_id,
        }
        self.assertTrue(limiter.allow_request(request))
        self.assertTrue(limiter.allow_request(request))
        self.assertTrue(limiter.allow_request(request))
    
    @patch('time.time')
    def test_allow_request_exceeding_limit(self, mock_time):
        limiter = FixedWindowRateLimiter(max_requests=2, window_size=60)
        
        mock_time.return_value = 1000
        user_id = "user_123"
        request = {
            'user_id': user_id,
        }
        self.assertTrue(limiter.allow_request(request))
        self.assertTrue(limiter.allow_request(request))
        self.assertFalse(limiter.allow_request(request))

    @patch('time.time')
    def test_allow_request_after_window_reset(self, mock_time):
        limiter = FixedWindowRateLimiter(max_requests=2, window_size=60)
        
        mock_time.return_value = 1000
        user_id = "user_123"
        request = {
            'user_id': user_id,
        }
        self.assertTrue(limiter.allow_request(request))
        self.assertTrue(limiter.allow_request(request))
        
        mock_time.return_value = 1061
        self.assertTrue(limiter.allow_request(request)) 
    
    @patch('time.time')
    def test_multple_users(self, mock_time):
        limiter = FixedWindowRateLimiter(max_requests=2, window_size=60)
        
        mock_time.return_value = 1000
        user_id_1 = "user_123"
        user_id_2 = "user_456"
        request_1 = {
            'user_id': user_id_1,
        }
        request_2 = {
            'user_id': user_id_2,
        }
        
        self.assertTrue(limiter.allow_request(request_1))
        self.assertTrue(limiter.allow_request(request_1))
        self.assertFalse(limiter.allow_request(request_1))
        
        self.assertTrue(limiter.allow_request(request_2))
        self.assertTrue(limiter.allow_request(request_2))
        self.assertFalse(limiter.allow_request(request_2))
    

if __name__ == '__main__':
    unittest.main()
    