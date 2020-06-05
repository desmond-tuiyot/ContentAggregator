import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from content_frontend.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    ENV = 'prod'
    if ENV == 'dev':
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SHOP###dez7228@localhost/content_aggreggator'
    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cdpsefgabpblxg:cbf62189bbd895a92260e2c54dd92324a35c5fcafc204' \
                                            'b662d8f95e4999c907d@ec2-52-202-146-43.compute-1.amazonaws.com:5432/d4hb0b' \
                                            'qnaoorsg'

    db.init_app(app)
    # db.create_all()

    from content_frontend.posts.routes import posts
    app.register_blueprint(posts)

    if not app.debug and not app.testing:
        # ...

        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/content_aggregator.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Content aggregator startup')

    return app