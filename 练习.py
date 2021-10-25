import datetime
times = datetime.datetime.now()
print(times.date())
time = times.time()
print(datetime.time(0,0,0).__le__(time) and time.__lt__(datetime.time(8,0,0)))