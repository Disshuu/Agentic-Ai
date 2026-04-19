import redis
import json

# Try connecting to Redis
try:
    r = redis.Redis(
        host="localhost",
        port=6379,
        db=0,
        decode_responses=True
    )
    r.ping()
    print("✅ Connected to Redis")

    USE_REDIS = True

except Exception as e:
    print("⚠️ Redis not available, using in-memory queue:", e)
    USE_REDIS = False


# Fallback queue (in-memory)
queue = []


def push_task(task):
    if USE_REDIS:
        try:
            r.lpush("task_queue", json.dumps(task))
        except Exception as e:
            print("Redis push failed, fallback used:", e)
            queue.insert(0, task)
    else:
        queue.insert(0, task)


def pop_task():
    if USE_REDIS:
        try:
            task = r.rpop("task_queue")
            if task:
                return json.loads(task)
        except Exception as e:
            print("Redis pop failed, fallback used:", e)

    if queue:
        return queue.pop()

    return None