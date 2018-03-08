
#This solution encompasses everything but the 'add' component
class Clock(object):
    def __init__(self, hours, minutes):
        self.hours, self.minutes = self.calculate(hours, minutes);

    def __str__(self):
        hour = str(self.hours).zfill(2)
        mins = str(self.minutes).zfill(2)
        return "{}:{}".format(hour,mins)

    def __eq__(self, other):
        return self.minutes == other.minutes and self.hours == other.hours

    def calculate(self, hours, minutes):
        mins = (hours*60) + minutes;
        minRemainder = mins % 60
        hours = (mins - minRemainder)/60
        timeH = int(hours % 24)
        return timeH, minRemainder

    def add(self, other):
        return Clock(self.hours, self.minutes+other)

