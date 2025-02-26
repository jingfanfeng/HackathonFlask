from . import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, index=True)
    deadline = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Event(id={self.id}, name={self.name}, deadline={self.deadline.strftime("%x %I:%M %p")})"
