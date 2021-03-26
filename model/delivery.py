class Delivery:
    def __init__(self, addressee, dimensions, address, latitude, longitude):
        self._addressee = addressee
        self._dimensions = dimensions
        self._address = address
        self._latitude = latitude
        self._longitude = longitude

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

