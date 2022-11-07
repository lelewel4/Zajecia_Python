import numpy as np
import psutil
import matplotlib.pyplot as plt
from time import perf_counter

def histogram_normal():
    t1_start = perf_counter()
    percent_usage = psutil.cpu_percent(interval=0.5, percpu=True)
    #print("percent:\t", percent_usage)
    x = np.arange(1, psutil.cpu_count() + 1, 1)
    y = percent_usage
    t1_stop = perf_counter()
    print("Czas trwania (przed wykresem):\t", t1_stop-t1_start)
    fig, ax = plt.subplots(figsize=(8,5))
    plt.xlabel("Proces logiczny")
    plt.ylabel("Zuzycie w %")
    plt.ylim(0, 100)
    plt.xlim(0, 9)
    ax.bar(x, y)
    plt.show()

if __name__ == '__main__':
    histogram_normal()