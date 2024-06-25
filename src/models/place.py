from . import db

class Place(db.Model):
    __tablename__ = 'place'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Integer, nullable=False)
    
    reviews = db.relationship('Review', backref='place', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'host_id': self.host_id,
            'price': self.price
        }