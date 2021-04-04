from app import db


class Vehicle(db.Model):

    __tablename__ = "vehicle"

    id = db.Column(db.Integer, primary_key=True)
    distributionCenter = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullble=False)
    dimensions = db.Column(db.Integer, db.ForeignKey('dimensions.id'), nullble=False)
    licensePlate = db.Column(db.String(80), nullable = True)

    vehicleCapacity = db.relationship('Dimensions', foreign_keys=dimensions._id)

    def __init__(self, id, distributionCenter, licensePlate, dimensions):
        self._id = id
        self._distributionCenter = distributionCenter
        self._licensePlate = licensePlate
        self._dimensions = dimensions

    def __repr__(self):
        return "<vehicle %r>" % self._licensePlate

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def distributionCenter(self):
        return self._distributionCenter

    @distributionCenter.setter
    def distributionCenter(self, distributionCenter):
        self._distributionCenter = distributionCenter

    @property
    def licensePlate(self):
        return self._licensePlate

    @licensePlate.setter
    def licensePlate(self, licensePlate):
        self._licensePlate = licensePlate

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        self._dimensions = dimensions

    def verifyMaximumCapacity(self, dimensions):
        approved = False
