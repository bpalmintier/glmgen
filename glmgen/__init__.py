
__version__ = '1.1.0'

import os

def schedule_dir():
    return os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/schedules')