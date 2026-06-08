import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        
        self.sem_zero=threading.Semaphore(1)
        self.sem_even=threading.Semaphore(0)
        self.sem_odd=threading.Semaphore(0)
        self.num=1


	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        alt=True
        for i in range(1, self.n + 1):
            self.sem_zero.acquire()
            printNumber(0)

            #release alternatively
            if alt:
                self.sem_odd.release()
                alt=False
            else:
                self.sem_even.release()
                alt=True    


        
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(1, self.n + 1,2):
            self.sem_even.acquire()
            printNumber(self.num)
            self.num=self.num+1   
            self.sem_zero.release()
        
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1,2):
            self.sem_odd.acquire()
            printNumber(self.num)
            self.num=self.num+1
            self.sem_zero.release()
        
        