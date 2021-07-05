import datetime
from app import db


class Chronicle(db.Model):
    min_timestamp = db.Column(db.DateTime(64), nullable=True, default=datetime.datetime.now())
    max_timestamp = db.Column(db.DateTime(64), nullable=True, default=min_timestamp + datetime.timedelta(days=20))
    source = db.Column(db.String(64), index=True)
    status = db.Column(db.String(5), default="Open")
    unique_id = db.Column(db.Integer, primary_key=True)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            "min_timestamp": self.min_timestamp,
            "max_timestamp": self.max_timestamp,
            "source": self.source,
            "status": self.status,
            "unique_id": self.unique_id
        }


class Event(db.Model):
    datetime = db.Column(db.DateTime(120), index=True, default=datetime.datetime.now())
    aircraft = db.Column(db.String(64), db.ForeignKey('chronicle.source'))
    unique_id = db.Column(db.Integer, db.ForeignKey('chronicle.unique_id'), primary_key=True)
