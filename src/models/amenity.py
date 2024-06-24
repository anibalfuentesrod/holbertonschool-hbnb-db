from config import db

class Amenity(db.Model):
    __tablename__ = 'amenities'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }