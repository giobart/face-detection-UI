from flask import Flask
from controller import blueprints
from flask_cors import CORS
import os

__all__ = ('create_app',)


def create_app(config=None, app_name='face-detection-UI'):
    """
    Initializes the application and its utilities.
    """

    app = Flask(app_name, template_folder=os.path.join('src', 'templates'), static_folder=os.path.join('src','static'))
    CORS(app)

    if config:
        app.config.from_pyfile(config)

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5006)
