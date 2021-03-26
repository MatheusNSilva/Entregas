class Course:
    def __init__(self, vehicle, nextDeliverys, kmTotal):
        self._vehicle = vehicle
        self._nextDeliverys = nextDeliverys
        self._kmTotal = kmTotal

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