from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

@dataclass
class Word(db.Model, SerializerMixin):
    id: int
    value: str
    frequency: int
    docs: list
    sentences: list

    id = db.Column(db.Integer, unique=True, primary_key=True)
    value = db.Column(db.String(100), unique=True, nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    docs = db.Column(db.String, nullable=False)
    sentences = db.Column(db.String, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<User %r>' % self.name
