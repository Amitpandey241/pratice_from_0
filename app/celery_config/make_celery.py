import os
from celery import Celery
from dotenv import load_dotenv
from celery.schedules import crontab

load_dotenv()

def makes_celery(app):
    celery_app= Celery(
        app,
        broker=[os.getenv("RABBITMQ_URI")],
        include=['app.celery_config.celery_task']
    )
    app.config['beat_schedule'] = {
        # Executes every minute
        'periodic_task-every-minute': {
            'task': 'send_mail',
            'schedule': crontab(minute="*")
        }
    }
    celery_app.conf.update(app.config)
    TaskBase = celery_app.Task
    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery_app.Task = ContextTask
    # with app.app_context():
    #     celery_app.conf.update(app.config)
    #     celery_app.conf.accept_context = ["json","yaml"]

    return celery_app


