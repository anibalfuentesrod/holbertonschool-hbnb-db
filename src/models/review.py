from .database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))