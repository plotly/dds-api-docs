from celery import Celery
from celery.schedules import crontab
import redis

import os
import json
from datetime import datetime

from example import get_all_apps_data


redis_url = os.environ.get("REDIS_URL", "redis://localhost:6379")

redis_instance = redis.StrictRedis.from_url(redis_url, decode_responses=True)

celery_app = Celery("celery_instance", broker=redis_url)


def r_set_all():
    r_set_run_start_time()
    r_set_run_finish_time(in_process=True)
    app_data = get_all_apps_data()
    r_set_app_data(app_data)
    r_set_run_finish_time()


def r_set_app_data(app_data):
    redis_instance.hset("ALL_APPS", "METADATA", json.dumps(app_data))
    return


def r_set_run_finish_time(in_process=False):
    if in_process:
        redis_instance.hset("TIMESTAMPS", "FINISH_TIME", "Running...")
        return
    redis_instance.hset("TIMESTAMPS", "FINISH_TIME", str(datetime.now()))
    return


def r_set_run_start_time():
    redis_instance.hset("TIMESTAMPS", "START_TIME", str(datetime.now()))
    return


def r_get_app_data():
    return json.loads(redis_instance.hget("ALL_APPS", "METADATA"))


def r_get_run_finish_time():
    return redis_instance.hget("TIMESTAMPS", "FINISH_TIME")


def r_get_run_start_time():
    return redis_instance.hget("TIMESTAMPS", "START_TIME")


### Celery
# Celery Scheduler
@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes Every 4 hours
    sender.add_periodic_task(crontab(minute="*/240"), update_data.s())


# Celery Task -
@celery_app.task
def update_data():
    r_set_all()
