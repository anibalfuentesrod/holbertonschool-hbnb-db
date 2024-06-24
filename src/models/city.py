from config import db

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    country_code = db.Column(db.String(10), db.ForeignKey('countries.code'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country_code': self.country_code
        }