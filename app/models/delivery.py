from app import db


class Delivery(db.Model):

    __tablename__ = "delivery"

    id = db.Column(db.Integer, primary_key=True)
    dimensions = db.Column(db.Integer, db.ForeignKey('dimensions.id'), nullble=False)
    addressee = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.String(10), nullable=False)
    longitude = db.Column(db.String(10), nullable=False)

    deliverySize = db.relationship('Dimensions', foreign_keys=dimensions._id)

    def __init__(self, addressee, dimensions, address, latitude, longitude):
        self._addressee = addressee
        self._dimensions = dimensions
        self._address = address
        self._latitude = latitude
        self._longitude = longitude

    def __repr__(self):
        return "<delivery %r>" % self._addressee

    @property
    def addressee(self):
        return self._addressee

    @addressee.setter
    def addressee(self, addressee):
        self._addressee = addressee

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        self._dimensions = dimensions

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def address(self, latitude):
        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def address(self, longitude):
        self._longitude = longitude

