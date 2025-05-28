import unittest
from unittest.mock import patch
from rate_limiter.token_bucket_rate_limiter import TokenBucketRateLimiter

class TestTokenBucketRateLimiter(unittest.TestCase):
    @patch('time.time')
    def test_allow_request_within_bucket(self, mock_time):
        limiter = TokenBucketRateLimiter(capacity=3, refill_rate=1)
        
        mock_time.return_value = 1000
        user_id = "user_123"
        request = {
            'user_id': user_id,
        }
        self.assertTrue(limiter.allow_request(request))
        self.assertTrue(limiter.allow_request(request))
        self.assertTrue(limiter.allow_request(request))

    @patch('time.time')
    def test_reject_request_exceeding_bucket(self, mock_time):
        limiter = TokenBucketRateLimiter(capacity=2, refill_rate=1)
        
        mock_time.return_value = 1000
        user_id = "user_123"
        request = {
            'user_id': user_id,
        }
        self.assertTrue(limiter.allow_request(request))
        self.assertTrue(limiter.allow_request(request))
        self.assertFalse(limiter.allow_request(request))

    @patch('time.time')
    def test_allow_request_after_refill(self, mock_time):
        limiter = TokenBucketRateLimiter(capacity=2, refill_rate=1)
        
        mock_time.return_value = 1000
        user_id = "user_123"
        request = {
            'user_id': user_id,
        }
        self.assertTrue(limiter.allow_request(request))
        self.assertTrue(limiter.allow_request(request))
        
        mock_time.return_value = 1001  # 1 second later
        self.assertTrue(limiter.allow_request(request))  # Should allow one more request
    
    @patch('time.time')
    def test_multiple_users(self, mock_time):
        limiter = TokenBucketRateLimiter(capacity=1, refill_rate=1)
        
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
        self.assertTrue(limiter.allow_request(request_2))
        self.assertFalse(limiter.allow_request(request_1))  # User 1 should be limited
        self.assertFalse(limiter.allow_request(request_2))  # User 2 should be limited