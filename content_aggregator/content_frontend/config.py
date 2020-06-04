import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')  # configure later
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
