from celery import Celery
from .config import config

celery_app = Celery(
    "bot_worker",
    broker=config.CELERY_BROKER_URL,
    backend=config.CELERY_RESULT_BACKEND
)

@celery_app.task
def example_task(x, y):
    return x + y
