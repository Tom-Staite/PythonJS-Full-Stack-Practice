# Contains db models

# Relative import
from config import db

# db.Model is a database model
class Contact(db.Model):
    __tablename__ = "Contacts"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        # takes all the fields we have on our object (above) and converts to Python dict
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }