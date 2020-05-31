from datetime import datetime
from db import db

#from db.sql import func


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

    @classmethod
    def best_status(cls, currency: str):
        '''
        SELECT Max(buy) AS buy, MIN(sale) AS sale
        FROM items AS one
        JOIN
        (SELECT MAX(created_date) as created_date
        FROM items
        WHERE name='USD'
        GROUP BY handler_id) AS two
        ON (one.created_date = two.created_date)
        '''

        stmt = db.session.query(db.func.max(cls.created_date).label('created_date')).filter(
            cls.name == currency).group_by(cls.handler_id).subquery()
        query = db.session.query(db.func.max(cls.buy).label('buy_max'), db.func.min(cls.sale).label('sale_min')).join(
            stmt, cls.created_date == stmt.c.created_date)
        for one, two in query:
           print('timer = {} | {}'.format(one, two))


        return
