from abc import abstractmethod, ABC


class RateLimiter(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def allow_request(self, request):
        """
        Determines if a request should be allowed based on the rate limit policy.
        
        :param request: The request to be evaluated.
        :return: True if the request is allowed, False otherwise.
        """
        pass
