from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False) # Nullable set to False to ensure name is provided
    surname = db.Column(db.String(100), unique=False, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False) # Unique email so that no duplicates exist
    phone = db.Column(db.String(20), nullable=True) # Phone can be nullable

    def to_dict(self): # Method to serialize the object to a dictionary so that it can be easily converted to JSON.
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone': self.phone
        }