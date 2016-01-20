import locale

from app.interfaces import ServiceLocator, Ui, Dao, Service
from app.models import Task


class App(object, ServiceLocator, Service):
    def add_to_plan(self, key: str, notes: list = None) -> Task:
        if notes is None:
            notes = []
        desc = '\n'.join(notes)
        task = self._find_or_create_task(self._tomorrow, key, desc)
        return task


    def switch_to(self, key: str, notes: list) -> Task:
        # TODO: implement
        pass

    def stop(self, notes: list) -> Task:
        # TODO: implement
        pass

    def add_trouble(self, desc: str) -> None:
        # TODO: implement
        pass

    def add_to_done(self, key: str, notes: list) -> Task:
        # TODO: implement
        pass

    def __init__(self, components: dict):
        locale.setlocale(locale.LC_ALL, "")

        self._ui = components['ui']()
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
        return self._dao

    def get_service(self) -> Service:
        return self

    def get_ui(self) -> Ui:
        return self._ui

    def run(self):
        self.get_ui().run()
