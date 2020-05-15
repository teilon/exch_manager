from datetime import datetime
from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(3), nullable=False)
    sale = db.Column(db.Float(precision=2), nullable=False)
    buy = db.Column(db.Float(precision=2), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    handler_id = db.Column(db.Integer, db.ForeignKey('handlers.id'), nullable=False)
    handler = db.relationship('HandlerModel')

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).order_by(cls.sale).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
