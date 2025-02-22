    # Multithreading 
        # Multithreading is a technique which allows a CPU to execute multiple threads of one process at same time.
    
    
    # WHY Multithreading 
        # The purpose of Multithreading is to run multiple task and function at the same time.
    
# Example:
from time import sleep
from threading import Thread

class A(Thread):
    def run(self):
        for i in range(5):
            print("Nishant")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("Anand")
            sleep(1)
            
t1 = A()
t2 = B()

t1.start()
t2.start()    #Both obj with run at same time

t1.join()
t2.join()     # Both obj will run after that last print function call

print("Ended...")