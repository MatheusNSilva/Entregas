from app import db


class Course(db.Model):

    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key = True)
    vehicle = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullble = False)
    nextDeliverys = db.Column(db.Text, nullable=False)
    kmTotal = db.Column(db.Float, nullable = False)

    vehicleCourse = db.relationship('Vehicle', foreign_keys=vehicle._id)

    def __init__(self, vehicle, nextDeliverys, kmTotal):
        self._vehicle = vehicle
        self._nextDeliverys = nextDeliverys
        self._kmTotal = kmTotal

    def __repr__(self):
        return "<Course %r>" % self._vehicle

    @property
    def vehicle(self):
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        self._vehicle = vehicle

    @property
    def nextDeliverys(self):
        return self._nextDeliverys

    @nextDeliverys.setter
    def nextDelivery(self, nextDeliverys):
        self._nextDeliverys = nextDeliverys

    @property
    def kmTotal(self):
        return self._kmTotal

    @kmTotal.setter
    def kmTotal(self, kmTotal):
        self._kmTotal = kmTotal