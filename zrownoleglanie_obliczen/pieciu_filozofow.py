import random
import threading
import time


class Philosopher(threading.Thread):

    def __init__(self, philosopher_num, left_fork, right_fork):
        super().__init__()  # multiple inheritance
        self.philosopher_num = philosopher_num
        self.left_fork = left_fork
        self.right_fork = right_fork

    def try_to_eat(self):
        self.left_fork.acquire()
        self.right_fork.acquire()

        print(f"Philosopher {self.philosopher_num} is eating")
        time.sleep(5)
        print(f"Philosopher {self.philosopher_num} stopped eating")

        self.left_fork.release()
        self.right_fork.release()

    def run(self):
        while True:
            print(f"Philosopher {self.philosopher_num} is thinking")
            time.sleep(random.randint(1, 6))
            self.try_to_eat()


if __name__ == '__main__':
    forks = [threading.Condition(threading.Lock()) for index in range(5)]
    philosophers = [Philosopher(index, forks[index], forks[(index + 1) % 5]) for index in range(5)]

    for p in philosophers:
        p.start()