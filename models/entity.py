from db import db


class EntityModel(db.Model):
    __tablename__ = 'entities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

    items = db.relationship('ItemModel', lazy='dynamic')

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_id_by_name(cls, name):
        entity = cls.query.filter_by(name=name).first()
        if entity:
            return entity.id

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
