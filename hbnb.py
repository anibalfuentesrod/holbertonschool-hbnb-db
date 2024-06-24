from flask import Flask
from flask_migrate import Migrate
from src.models import db, User, Place, Review  # Ensure correct import

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Register blueprints here
    from src.routes.users import users_bp
    app.register_blueprint(users_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run()