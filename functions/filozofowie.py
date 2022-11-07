import threading
import time

class Philosopher(threading.Thread):
    running = True

    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while (self.running):
            time.sleep(3)
            print('Filozof %s jest glodny' % self.index)
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
        while self.running:
            fork1.acquire()                 #blokuj
            locked = fork2.acquire(False)   #nie blokuj
            if locked:
                break
            fork1.release()                 #zwolnienie blokady
            print('Filozof %s zmienia widelec' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print('Filozof %s zaczyna jesc' % self.index)
        time.sleep(3)
        print('Filozof %s skonczyl jesc' % self.index)

if __name__ == "__main__":
    forks = [threading.Semaphore() for n in range(5)]                       #stworzenie sztuccow
    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5])        #inicjalizacja
                    for i in range(5)]
    Philosopher.running = True
    for p in philosophers: p.start()                                        #wywolanie watkow
    time.sleep(20)
    Philosopher.running = False
    print("Zjedlismy")