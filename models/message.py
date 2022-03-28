import email
from utils.db import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(100), nullable=False)

    def __init__(self, firstname, lastname, email, message) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.message = message

    def __repr__(self):
        return f"User({self.id}, '{self.firstname}', '{self.lastname}', '{self.email}', '{self.message}')"
