import os

class Config(object):
    POSTGRES = {
        'user': 'vidyut',
        'pw': 'vidyut2018*',
        'db': 'vidyut',
        'host': 'ambvidyut-dev.ckhmnttmq7jx.ap-south-1.rds.amazonaws.com',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEVELOPMENT = True
    DEBUG = True
    MAINTENANCE = False

class TestingConfig(Config):
    TESTING = True