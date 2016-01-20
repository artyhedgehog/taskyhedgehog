from abc import abstractmethod

from app.models import Task
from lib.interface import Interface


class Dao(metaclass=Interface):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_tasks_list(self, key: str, default: list) -> dict:
        """
        :param key: Key for stored value
        :param default: Default value
        :rtype: dict[Task]
        """
        pass

    @abstractmethod
    def load_task(self, key: str, default: object) -> Task:
        pass

    @abstractmethod
    def load_notes_list(self, key: str, default: list):
        pass


class ExecutionContext(metaclass=Interface):
    @abstractmethod
    def __init__(self):
        pass


class Ui(metaclass=Interface):
    @abstractmethod
    def __init__(self, context: ExecutionContext):
        pass

    @abstractmethod
    def run(self):
        pass


class InterfaceError(Exception):
    pass


class ServiceLocator(metaclass=Interface):
    @abstractmethod
    def __init__(self, ui: Ui, service: Service, dao: Dao):
        pass

    @abstractmethod
    def get_ui(self) -> Ui:
        pass

    @abstractmethod
    def get_dao(self) -> Dao:
        pass

    @abstractmethod
    def get_service(self) -> Service:
        pass


class Service(metaclass=Interface):
    @abstractmethod
    def add_to_plan(self, key: str, notes: list) -> Task:
        pass

    @abstractmethod
    def add_to_done(self, key: str, notes: list) -> Task:
        pass

    @abstractmethod
    def switch_to(self, key: str, notes: list) -> Task:
        pass

    @abstractmethod
    def stop(self, notes: list) -> Task:
        pass

    @abstractmethod
    def add_trouble(self, desc: str) -> None:
        pass
