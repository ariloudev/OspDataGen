from time import struct_time, mktime, localtime, strptime


class Daypart:
    def __init__(self):
        pass

    start_time = localtime()

    @staticmethod
    def generate_dayparts():
        dayparts = list()

        for hour in range(0, 24):
            daypart = Daypart()
            daypart.start_time = strptime(hour.__str__() + ":00", "%H:%M")
            dayparts.append(daypart)

            daypart = Daypart()
            daypart.start_time = strptime(hour.__str__() + ":30", "%H:%M")
            dayparts.append(daypart)

        return dayparts
