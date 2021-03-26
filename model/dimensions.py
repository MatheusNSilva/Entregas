class Dimensions:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id