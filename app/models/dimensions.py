from app import db


class Dimensions(db.Model):

    __tablename__ = "dimensions"

    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)

    def __init__(self, id, height, width, length):
        self._id = id
        self._height = height
        self._width = width
        self._length = length

    @property
    def height(self):
        return self._height

    @height.setter
    def nome(self, height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id