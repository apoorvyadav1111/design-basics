from rate_limiter.leaky_bucket_rate_limiter import LeakyBucketRateLimiter
import unittest
from unittest.mock import patch

class TestLeakyBucketRateLimiter(unittest.TestCase):
    @patch('time.time')
    def test_single_user_allows_within_capacity(self, mock_time):
        limiter = LeakyBucketRateLimiter(capacity=3, leak_rate=1)
        mock_time.return_value = 1000
        user_id = "user_1"
        request_1 = {
            "user_id": user_id,
        }

        # Allow first request
        self.assertTrue(limiter.allow_request(request_1))
        # Allow second request
        self.assertTrue(limiter.allow_request(request_1))
        # Allow third request
        self.assertTrue(limiter.allow_request(request_1))

        # Fourth request should exceed capacity
        self.assertFalse(limiter.allow_request(request_1))

    @patch('time.time')
    def test_leakage_allows_later_request(self, mock_time):
        limiter = LeakyBucketRateLimiter(capacity=2, leak_rate=1)
        mock_time.return_value = 1000  # Mock current time
        user_id = "user_1"
        request_1 = {
            "user_id": user_id,
        }
        # allow two requests
        self.assertTrue(limiter.allow_request(request_1))
        self.assertTrue(limiter.allow_request(request_1))
        # third request should fail
        self.assertFalse(limiter.allow_request(request_1))
        # Simulate time passing to allow leakage
        mock_time.return_value = 1001  # 1 second later
        self.assertTrue(limiter.allow_request(request_1))  # Should succeed after leakage

    @patch('time.time')
    def test_multiple_users_independent_buckets(self, mock_time):
        limiter = LeakyBucketRateLimiter(capacity=2, leak_rate=1)
        mock_time.return_value = 1000  # Mock current time
        request1 = {
            "user_id": "user_1",
        }
        request2 = {
            "user_id": "user_2",
        }


        # Fill both buckets separately
        self.assertTrue(limiter.allow_request(request1))
        self.assertTrue(limiter.allow_request(request1))
        self.assertTrue(limiter.allow_request(request2))
        self.assertTrue(limiter.allow_request(request2))
        # Both buckets should be at capacity now
        self.assertFalse(limiter.allow_request(request1))
        self.assertFalse(limiter.allow_request(request2))
