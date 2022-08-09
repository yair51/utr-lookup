import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    FLASK_APP = "main.py"
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dfal;dfkad adf")


class StagingConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True