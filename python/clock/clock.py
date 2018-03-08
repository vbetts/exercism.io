import math

def Clock(hours=0, minutes=0):

    mins = (hours*60) + minutes;

    minRemainder = mins % 60

    hours = (mins - minRemainder)/60

    timeH = int(hours % 24)

    return str(timeH).zfill(2) + ":" + str(minRemainder).zfill(2)

