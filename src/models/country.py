from .database import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    cities = db.relationship('City', backref='country', lazy=True)