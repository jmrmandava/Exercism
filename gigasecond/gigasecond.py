import datetime
from datetime import timedelta


def add(moment):
    new_time = moment + timedelta(seconds=1000000000)
    return new_time
