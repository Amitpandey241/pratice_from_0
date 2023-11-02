import os
from app import app,mongo,celery,mail
from app.celery_config.make_celery import makes_celery
from celery import shared_task
from flask_mail import Message,Mail
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@celery.task(name='jib')
def jib(name):
    print(name)


@celery.task(name='send_mail')
def send_mail():
    mail = Mail(app)
    try:
        email ="pamit1687@gmail.com"
        msg = Message('Testing', sender='ap7788546@gmail.com', recipients=[email])
        msg.body = "Cronejob mail"
        mail.send(msg)
        logger.info("Hello! from periodic task mail")
    except Exception as error:
        logger.info(str(error))




