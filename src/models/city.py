from .database import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

    places = db.relationship('Place', backref='city', lazy=True)