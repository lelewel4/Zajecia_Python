from threading import Thread
import numpy as np
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import time

#global
logic_proccess = psutil.cpu_count()  #8
percent_usage = []
t1_start = 0
t1_stop = 0

def watek_read(nazwa):
    global percent_usage, t1_start
    t1_start = time.perf_counter()
    print(nazwa, 'zostal uruchomiony')
    percent_usage = psutil.cpu_percent(interval=0.5, percpu=True)
    print("percent:\t", percent_usage)
    print(nazwa, 'zakonczyl dzialanie')

def watek_plot(nazwa):
    global percent_usage, logic_proccess, t1_stop
    print(nazwa, 'zostal uruchomiony')
    time.sleep(1)
    dfx = np.arange(1, psutil.cpu_count() + 1, 1)
    dfy = percent_usage
    t1_stop = time.perf_counter()
    print("Czas trwania (przed wykresem):\t", t1_stop-t1_start)
    x = []
    y = []
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(x, y)
    counter = count(0, 10)
    def update(i):
        idx = next(counter)+1
        x.append(dfx[i])
        y.append(dfy[i])
        plt.cla()
        ax.bar(x, y)
        plt.xlabel("Proces logiczny")
        plt.ylabel("Zuzycie w %")
        plt.ylim(0, 100)
        plt.xlim(0, 9)
    ani = FuncAnimation(fig=fig, repeat=True, func=update, interval=200)
    plt.show()
    print(nazwa, 'zakonczyl dzialanie')

lista_watkow = [Thread(target=watek_read, args=("czytanie",)),
                Thread(target=watek_plot, args=("wykreslenie",))]

for x in lista_watkow:
    x.start()

if __name__ == '__main__':
    while(True):
        pass



