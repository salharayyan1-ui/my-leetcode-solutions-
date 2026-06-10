import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i=0
        self.sem_fizz=threading.Semaphore(0)
        self.sem_buzz=threading.Semaphore(0)
        self.sem_fizzbuzz=threading.Semaphore(0)
        self.sem_number=threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1,self.n+1):
            if i%3==0 and i%5!=0:
                self.sem_fizz.acquire()
                printFizz()
                self.sem_number.release()

        

    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
       for i in range(1,self.n+1):
            if i%3!=0 and i%5==0:
                self.sem_buzz.acquire()
                printBuzz()
                self.sem_number.release()

        


    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1,self.n+1):
            if i%3==0 and i%5==0:
                self.sem_fizzbuzz.acquire()
                printFizzBuzz()
                self.sem_number.release()


    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        
        for i in range(1,self.n+1):
            self.sem_number.acquire()  #move to next iter only when other methods complete their iter 
            if i%3 !=0 and i%5!=0:
                
                printNumber(i)
                self.sem_number.release()
            elif i%3==0 and i%5!=0:
                self.sem_fizz.release()
            elif i%3!=0 and i%5==0:
                self.sem_buzz.release()
            else:
                self.sem_fizzbuzz.release()           

        