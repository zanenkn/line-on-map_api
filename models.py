
from app import db


class Path(db.Model):
    __tablename__ = 'paths'
    id = db.Column(db.Integer, primary_key=True)
    svg = db.Column(db.Text, nullable=False)


