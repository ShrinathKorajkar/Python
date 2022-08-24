class Time:
    # hour = 0
    # minute = 0
    # second = 0
    def __init__(self, hour=0, minute=0, second=0):  # constructor
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):  # override print()
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def increment(self, seconds):
        seconds += time_to_int(self)
        return int_to_time(seconds)

    def __add__(self, other):  # + operator overload
        if isinstance(other, Time):  # other is instance of Time
            return add_time(self, other)
        else:
            return self.increment(other)  # type based dispatch

    def __radd__(self, other):
        return self.__add__(other)


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.seconds = divmod(seconds, 60)  #return divident and remainder
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
    # sum = Time()
    # sum.hour = t1.hour + t2.hour
    # sum.minute = t1.minute + t2.minute
    # sum.second = t1.second + t2.second
    # return sum


time = Time()
time.hour = 11
time.minute = 20
time.second = 32

duration = Time()
duration.hour = 1
duration.minute = 20
duration.second = 23

print(time)
print(duration)
done = add_time(time, duration)
done.print_time()
print(duration.increment(199))
print(time + duration)
print(time + 200)
print(200 + time)
