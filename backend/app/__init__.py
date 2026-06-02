"""Backend application package."""
from flask import Flask
from flask_cors import CORS

from app.config import Config
from app.extensions import db
from app.utils.file_utils import ensure_folder_exists

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    ensure_folder_exists(app.config["STORAGE_FOLDER"])
    ensure_folder_exists(app.config["REGISTERED_FACES_FOLDER"])
    ensure_folder_exists(app.config["TEMP_FRAMES_FOLDER"])
    ensure_folder_exists(app.config["ENCODINGS_FOLDER"])
    ensure_folder_exists(app.instance_path)

    from app.models import Person, FaceEncoding, RecognitionLog
    from app.routes.health_routes import health_bp
    from app.routes.person_routes import person_bp
    from app.routes.registration_routes import registration_bp
    from app.routes.live_recognition_routes import live_recognition_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(person_bp)
    app.register_blueprint(registration_bp)
    app.register_blueprint(live_recognition_bp)

    with app.app_context():
        db.create_all()

    return app