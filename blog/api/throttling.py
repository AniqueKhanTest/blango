from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonSustainedThrottle(AnonRateThrottle):
    scope = "anon_sustained"


class AnonBurstThrottle(AnonRateThrottle):
    scope = "anon_burst"


class UserSustainedThrottle(UserRateThrottle):
    scope = "user_sustained"


class UserBurstThrottle(UserRateThrottle):
    scope = "user_burst"

"""
You can write your own throttling classes and override the 
allow_request() method: return True or False to allow or deny the request. 
Here's an example class that the DRF documentation provides, 
which will randomly deny one in every ten requests:
"""

# import random
# from rest_framework.throttling import BaseThrottle

# class RandomRateThrottle(BaseThrottle):
#     def allow_request(self, request, view):
#         return random.randint(1, 10)!=1