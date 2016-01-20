from datetime import datetime, timedelta


class Task(object):
    def __init__(self, key: str, desc: str = '', times: list = None):
        if times is None:
            times = []
        self.key = key
        self.desc = desc
        self.intervals = times

    @staticmethod
    def find_or_create(store: dict, key: str, desc: str) -> Task:
        task = store.get(key)
        if task is None:
            task = Task(key, desc)
        store[key] = task
        return task

    def start(self, dt=None) -> None:
        if dt is None:
            dt = datetime.now()
        self.intervals.append(Interval())


class Interval(object):
    def __init__(self, start: datetime = datetime.now(), end: datetime = None):
        self.start = start
        self.end = end

    def duration(self) -> timedelta:
        if self.start is None or self.end is None:
            return None
        return self.end - self.start


