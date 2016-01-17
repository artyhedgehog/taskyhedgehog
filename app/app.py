import locale

from app.interfaces import ServiceLocator, InterfaceError, Ui, Dao, \
    Service
from app.models import Task
from app.pickledao import PickleDao
from app.shell import TaskyHedgehogShell
from lib.interface import implements


class App(object, ServiceLocator, Service):
    def __init__(self, config: dict):
        locale.setlocale(locale.LC_ALL, "")

        components = config['components']
        self._ui = components['ui']()
        self._service = components['service']()
        self._dao = components['dao']()

        self._next_task_id = 0

        dao = self.get_dao()
        self._today = dao.load_tasks_list('today', [])
        self._tomorrow = dao.load_tasks_list('tomorrow', [])
        self._current = dao.load_task('current', None)
        self._paused = dao.load_tasks_list('paused', [])
        self._troubles = dao.load_notes_list('troubles', [])
        self._interferences = dao.load_notes_list('interferences', [])

    def get_dao(self) -> Dao:
        pass

    def get_service(self) -> Service:
        pass

    def get_ui(self) -> Ui:
        pass

    def add_to_plan(self, desc: str):
        self._tomorrow.append(Task(self._generate_id(), desc))
