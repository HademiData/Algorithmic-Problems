The dining philosophers problem is a classic synchronization problem that
involves a group of philosophers sitting around a table, each with a plate of
spaghetti and a fork on either side of the plate. There are as many forks as there are 
philosophers, and each philosopher needs two forks to eat. The problem is to create a
program that allows each philosopher to take the forks and eat without causing a deadlock.

Here is a sample solution in Python using the threading module


import threading
import time
import random

# Number of philosophers
NUM_PHILOSOPHERS = 5

# Locks for each fork
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

    def run(self):
        while True:
            print("Philosopher", self.index, "is thinking.")
            time.sleep(random.uniform(0, 5))

            # Pick up left fork
            print("Philosopher", self.index, "is hungry and tries to pick up left fork.")
            forks[self.index].acquire()
            print("Philosopher", self.index, "picked up left fork.")

            # Pick up right fork
            print("Philosopher", self.index, "tries to pick up right fork.")
            forks[(self.index + 1) % NUM_PHILOSOPHERS].acquire()
            print("Philosopher", self.index, "picked up right fork.")

            # Eat spaghetti
            print("Philosopher", self.index, "is eating spaghetti.")
            time.sleep(random.uniform(0, 5))

            # Put down right fork
            print("Philosopher", self.index, "put down right fork.")
            forks[(self.index + 1) % NUM_PHILOSOPHERS].release()

            # Put down left fork
            print("Philosopher", self.index, "put down left fork.")
            forks[self.index].release()

if __name__ == '__main__':
    # Create and start the philosopher threads
    philosophers = [Philosopher(i) for i in range(NUM_PHILOSOPHERS)]
    for philosopher in philosophers:
        philosopher.start()

    # Wait for all philosopher threads to finish
    for philosopher in philosophers:
        philosopher.join()
