from config.shell import TaskyHedgehogShell
from config.pickledao import PickleDao

config = {
    'components': {
        'ui': TaskyHedgehogShell,
        'dao': PickleDao
    }
}
