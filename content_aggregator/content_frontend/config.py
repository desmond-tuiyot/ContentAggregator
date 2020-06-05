import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URL = 'postgresql://postgres:SHOP###dez7228@localhost/content_aggreggator'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
        # os.environ.get('SQLALCHEMY_DATABASE_URI')  # configure later
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')



class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
