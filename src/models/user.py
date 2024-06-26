from .database import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    
    places = db.relationship('Place', backref='host', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'is_admin': self.is_admin
        }

    @staticmethod
    def create(data):
        # Check if user already exists
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            raise ValueError("User with this email already exists.")
        
        user = User(email=data['email'])
        user.set_password(data['password'])
        user.is_admin = data.get('is_admin', False)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all():
        return [user.to_dict() for user in User.query.all()]