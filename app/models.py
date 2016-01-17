from datetime import datetime, timedelta


class Task(object):
    def __init__(self, id: int, desc: str = '', times: list = None):
        if times is None:
            times = []
        self.id = id
        self.desc = desc
        self.intervals = times

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


