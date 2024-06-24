from config import db

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code
        }