import hashlib

print(hashlib.sha256(b"password").hexdigest())
print(hashlib.sha256(b"hello wold").hexdigest())
print(hashlib.sha256(b"password123").hexdigest())


"""
The next level of security is to add a salt: a small amount of random data that’s added to the password before it’s hashed, when it’s first set. The salt is stored unhashed, and is read and reused on password validation.
For example, let’s say we generate the salt abc123 when the user sets their password/registers. The password hash would be generated like this:
"""


print(hashlib.sha256(b"abc123" + b"password123").hexdigest())


"""
The output that’s stored in the database is the final hash 01959…. In our scenario, the time it takes to log in a user goes from 0.1 seconds to 1.099 seconds (or about an extra second). Again, in reality the actual durations will be different, but even in our case this is probably not that noticeable to a user, especially since they would probably only log in once per session, not on every page. But the effect on an attacker is much more dramatic. It will slow down brute force attempts from 10 per second to less than 1 per second, meaning it would take 10 times longer to guess the password of a user.
"""

hash = hashlib.sha256(b"abc123" + b"password123").hexdigest()
for i in range(1000):
    hash = hashlib.sha256(b"abc123" + hash.encode('ascii')).hexdigest()

print(hash)
