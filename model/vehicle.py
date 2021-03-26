class Vehicle:
    def __init__(self, id, distributionCenter, licensePlate, dimensions):
        self._id = id
        self._distributionCenter = distributionCenter
        self._licensePlate = licensePlate
        self._dimensions = dimensions

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