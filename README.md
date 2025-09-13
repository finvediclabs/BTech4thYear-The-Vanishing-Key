# The Vanishing Key

This project demonstrates Redis cache inconsistency bugs, focusing on TTL mismanagement and key collisions.

## Theme
**Redis Caching Bug**

## Description
Redis is a popular in-memory cache, but improper usage can lead to subtle bugs. This project intentionally includes:
- Keys vanishing unexpectedly due to TTL mismanagement
- Key collisions due to poor key naming

## Files
- `src/vanishing_key.py`: Contains buggy cache logic

## How It Works
- `set_with_ttl`: May fail to set TTL, causing keys to persist or vanish unexpectedly
- `set_with_collision`: Uses a key naming scheme that causes collisions

## Requirements
- Python 3.x
- `redis` Python package
- Local Redis server running

## Installation
Add the following to a `requirements.txt` file:

```
redis
```

No need to install or run; this is for reference only.

## Note
This project is intentionally buggy and not meant for production use.
