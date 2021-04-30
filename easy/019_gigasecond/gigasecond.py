from datetime import datetime, timedelta

def add(moment):
    ''' 1 gigasecond = 1.000.000.000 seconds'''
    return moment + timedelta(seconds=1000000000)
