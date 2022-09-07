import threading
from req import bruteforce

nim = "19200076"
year_start = 1985
year_end = 1990

for i in range(year_start, (year_end + 1)):
    t1 = threading.Thread(target=bruteforce, args=(i, nim))
    t1.start()
