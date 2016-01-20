from cmd import Cmd
from datetime import datetime

from app.interfaces import Ui, ServiceLocator
from app.models import Task, Interval


class Shell(Ui, Cmd):
    prompt = '>\|/C. '

    def run(self):
        self.cmdloop('Type help or ? to list commands.\n')

    def __init__(self, locator: ServiceLocator):
        super().__init__()
        self.service = locator.get_service()

    def do_plan(self, desc: str):
        self.service.add_to_plan(desc)

    def do_done(self, desc: str):
        args = desc.split(maxsplit=2)
        self.service.add_to_done(args.pop(0), args)

    def do_do(self, desc: str):
        if self.current is not None:
            self.paused.insert(0, self.current)
        self.current = Task(self._generate_id(), desc)

    def do_list(self, arg: str):
        print('\nCurrent:\n')
        print(self.current)
        print('\nToday:\n')
        for task in self.today:
            print(task)
        print('\nTomorrow:\n')
        for task in self.tomorrow:
            print(task)

    def do_report(self, arg: str):
        print('Фамилия и имя заполняющего')
        print('Коломыцев Артём')
        print()
        print('Что было выполнено за день?')
        for task in self.today:
            print(task)
        print()
        print('Что будет сделано завтра?')
        for task in self.tomorrow:
            print(task)
        print()
        print('Какие проблемы возникли по ходу работы?')
        for entry in self.troubles:
            print(entry)
        print()
        print('Какие проблемы могут помешать недельному плану?')
        for entry in self.interferences:
            print(entry)
        print()

    def do_debug(self):
        pass

    def _generate_id(self):
        task_id = self._next_task_id
        self._next_task_id += 1
        return task_id
