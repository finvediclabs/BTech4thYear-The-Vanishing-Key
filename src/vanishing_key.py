"""
Title: The Vanishing Key
Description: Redis cache inconsistency due to TTL or key collisions
Theme: Redis Caching Bug
"""

import redis
import time

# Intentionally buggy Redis cache handler
class VanishingKeyCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def set_with_ttl(self, key, value, ttl):
        # BUG: TTL is not set properly if value is None
        if value is None:
            self.r.set(key, value)  # Should not cache None values
        else:
            self.r.set(key, value, ex=ttl)

    def get(self, key):
        return self.r.get(key)

    def set_with_collision(self, user_id, value):
        # BUG: Key collision due to poor key naming
        key = f"user:{user_id % 10}"  # Only 10 possible keys for any user
        self.r.set(key, value, ex=5)

    def demo_vanishing_key(self):
        self.set_with_ttl('temp', 'data', 1)
        time.sleep(2)
        # BUG: Key should have expired, but may not if TTL was not set
        return self.get('temp')

    def demo_collision(self):
        for uid in range(15):
            self.set_with_collision(uid, f"value_{uid}")
        # BUG: Some values will be overwritten due to key collision
        return [self.get(f"user:{i}") for i in range(10)]

if __name__ == "__main__":
    cache = VanishingKeyCache()
    print("Vanishing Key Demo:", cache.demo_vanishing_key())
    print("Collision Demo:", cache.demo_collision())
