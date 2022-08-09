from flask import Flask, render_template, request, redirect, url_for
from os import path, getenv
from .config import DevelopmentConfig, Config, StagingConfig


def create_app():
    app = Flask(__name__)
    # sets development/production enviornment
    env_config = getenv("APP_SETTINGS", "DevelopmentConfig")
    if env_config == 'Config':
        env_config = Config
    elif env_config == 'StagingConfig':
        env_config = StagingConfig
    else:
        env_config = DevelopmentConfig
    print(env_config)
    app.config.from_object(env_config)
    

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app