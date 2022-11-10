import numpy as np
import matplotlib.pyplot as plt
import psutil
from datetime import datetime
from concurrent.futures.thread import ThreadPoolExecutor

def watek_time():
    print('Time zostal uruchomiony')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Obecna godzina: ", current_time)
    print('Time zakonczyl dzialanie\n')

def watek_percent():
    print('Percent zostal uruchomiony')
    print("Zuzycie: ", psutil.cpu_percent(interval=0.5, percpu=True))
    print('Percent zakonczyl dzialanie\n')

def watek_plt():
    print('Histogram zostal uruchomiony')
    x = np.random.normal(200, 1, 10000)
    plt.hist(x)
    plt.show()
    print('Histogram zakonczyl dzialanie')

if __name__ == '__main__':
    with ThreadPoolExecutor() as exe:
        for i in range(3):
            exe.submit(watek_time)
            exe.submit(watek_percent)
            exe.submit(watek_plt)




