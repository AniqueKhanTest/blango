
# This script does not work in this environment

import requests

# Credentials
EMAIL_ADDRESS = "admin@gmail.com"
PASSWORD = "admin"
BASE_URL = "http://localhost:8000/"

anonymous_post_response = requests.get(BASE_URL+"api/posts")
anonymous_post_response.raise_for_status()

anonymous_post_count = anonymous_post_response.json()['count']
print(f"Anonymous user have {anonymous_post_count} post{'' if anonymous_post_count==1 else 's'}")

auth_resp = requests.post(
    BASE_URL+"api/token-auth/",
    json={"username":EMAIL_ADDRESS,"password":PASSWORD}
)

auth_resp.raise_for_status()
token = auth_resp.json()['token']

# Use the token in a request
authenticated_post_resp = requests.get(BASE_URL+"api/posts/",headers={"Authorization":f"Token {token}"})

# Url paramters / Search query included
# authenticated_post_resp = requests.get(BASE_URL+"api/posts/",headers={"Authorization":f"Token {token}"},
# params={"author": 10,"content":"This is to test the query parameters with the requests module"})


authenticated_post_count = authenticated_post_resp.json()['count']
print(f"Authenticated user has {authenticated_post_count} post{'' if authenticated_post_count==1 else 's'}")

# Since requests does not remember headers between requests, this next request is unauthenticated again
anonymous_post_response = requests.get(BASE_URL+"api/posts/")