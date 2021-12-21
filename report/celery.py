from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
# from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'report.settings')

app = Celery('report')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.beat_schedule={
#     "scheduled_task":{
#         "task":"main.tasks.add",
#         "schedule":crontab(hour=0, minute=2),
#         "args":(10,10)
#     },
# }

# app.conf.beat_schedule={
#     "scheduled_task":{
#         "task":"main.tasks.add",
#         "schedule":crontab(),
#         "args":(10,10)
#     },
# }

# app.conf.beat_schedule={
#     "scheduled_task":{
#         "task":"main.tasks.add",
#         "schedule":30.0,
#         "args":(10,10)
#     },
# }

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request========: {self.request!r}')