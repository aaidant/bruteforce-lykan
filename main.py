import threading
from req import bruteforce

nim = "19200202"
year_start = 1996
year_end = 1999

for i in range(year_start, (year_end + 1)):
    t1 = threading.Thread(target=bruteforce, args=(i, nim))
    t1.start()
