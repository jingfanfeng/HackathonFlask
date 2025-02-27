from . import db
from flask_login import UserMixin


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, index=True)
    deadline = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Event(id={self.id}, name={self.name}, deadline={self.deadline.strftime("%x %I:%M %p")})"


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 320 characters is the longest possible email address
    email = db.Column(db.String(320), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
