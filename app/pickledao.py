import pickle
from app.interfaces import Dao


class PickleDao(object, Dao):
    def save(self, key: str, value: object):
        pickle.dump(value, open(self.filename, 'wb'))

    def __init__(self, filename: str):
        self.filename = filename

    def load(self, key: str) -> object:
        pickle.load(open(self.filename, 'rb'))
