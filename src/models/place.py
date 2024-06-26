from .database import db

class Place(db.Model):
    __tablename__ = 'place'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    
    # Remove or comment out the relationship that references place_amenity
    # amenities = db.relationship('Amenity', secondary='place_amenity', back_populates='places')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'host_id': self.host_id,
            'price': self.price,
        }