from app import db


class DistributionCenter(db.Model):

    __tablename__ = "distribution-center"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable = True)
    latitude = db.Column(db.String(10), nullable=False)
    longitude = db.Column(db.String(10), nullable=False)

    def __init__(self, name, latitude, longitude):
        self._name
        self._latitude
        self._longitude

    def __repr__(self):
        return "<distribution-center %r>" % self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        self._longitude = longitude