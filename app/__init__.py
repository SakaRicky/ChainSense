
from flask import Flask;
from config import Config, logger
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Use app.app_context() to ensure engine is accessible if needed,
    with app.app_context():

        @event.listens_for(Engine, "connect")
        def receive_connect(dbapi_connection, connection_record):
            """Listen for new DB connections and log them."""
            # Use the Flask app's logger for consistency
            logger.info("Successfully established a new DB connection.")

    from . import routes
    app.register_blueprint(routes.bp)

    app.logger.info("Your Flask app have started")

    return app