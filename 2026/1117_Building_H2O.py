import threading
class H2O:
    def __init__(self):
        self.sem_hydrogen= threading.Semaphore(2)
        self.sem_oxygen=threading.Semaphore(0)
        self.lock=threading.Lock()
        self.counter=0


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.            
        self.sem_hydrogen.acquire()
        releaseHydrogen()
        with self.lock:
            self.counter=self.counter+1
            if self.counter==2:
                self.counter=0
                self.sem_oxygen.release()
 
        


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.sem_oxygen.acquire()
        releaseOxygen()
        self.sem_hydrogen.release(2)