from flask_restful import Resource,Api
from flask import Flask, request, jsonify,Blueprint
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os
from celery.schedules import crontab
from app.celery_config.make_celery import makes_celery
load_dotenv()
app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] =os.getenv("MONGO_URI")
app.config["event_serializer"] ='json'
app.config["result_serializer"] = 'json'
app.config["task_serializer"] = 'json'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mongo = PyMongo(app)
mail = Mail(app)
celery = makes_celery(app)
