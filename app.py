#!/usr/bin/python3
# coding: utf-8
import cmd, datetime, locale


class TaskyHedgehogShell(cmd.Cmd):
    intro = 'Type help or ? to list commands.\n'
    prompt = '>\|/C. '

    def __init__(self):
        super().__init__()
        self._next_task_id = 0
        locale.setlocale(locale.LC_ALL, "")
        self.today = []  # :type : list[Task]
        self.tomorrow = []  # :type : list[Task]
        self.current = None # :type : Task
        self.paused = []  # :type : list[Task]
        self.troubles = []  # :type : list[str]
        self.interferences = []  # :type : list[str]

    def do_plan(self, desc):
        self.tomorrow.append(Task(self._generate_id(), desc))
        pass

    def do_done(self, desc: str = ''):
        if desc == '':
            if self.current is not None:
                task = self.current
                self.current = None
            else:
                print('No current task specified')
                return
        else:
            task = Task(self._generate_id(), desc, [Interval(end=datetime.datetime.now())])
        self.today.append(task)

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


class Task(object):
    def __init__(self, id: int, desc: str = '', times: list = None):
        if times is None:
            times = []
        self.id = id
        self.desc = desc
        self.intervals = times

    def start(self, dt=None) -> None:
        if dt is None:
            dt = datetime.datetime.now()
        self.intervals.append(Interval())


class Interval(object):
    def __init__(self, start: datetime.datetime = datetime.datetime.now(), end: datetime.datetime = None):
        self.start = start
        self.end = end

    def duration(self) -> datetime.timedelta:
        if self.start is None or self.end is None:
            return None
        return self.end - self.start


if __name__ == '__main__':
    TaskyHedgehogShell().cmdloop()
