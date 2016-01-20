import pickle
from app.interfaces import Dao
from app.models import Task


class PickleDao(object, Dao):
    def __init__(self, filename: str):
        self.filename = filename

    def load_notes_list(self, key: str, default: list):
        # TODO: implement
        pass

    def load_task(self, key: str, default: object) -> Task:
        # TODO: implement
        pass

    def load_tasks(self, key: str, default: list) -> list:
        # TODO: implement
        pass

    def save(self, key: str, value: object):
        pickle.dump(value, open(self.filename, 'wb'))

    def load(self, key: str) -> object:
        pickle.load(open(self.filename, 'rb'))
