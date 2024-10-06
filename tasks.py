from app import celery

@celery.task
def track_click(short_url):
    pass
