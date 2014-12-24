import time
from threading import Thread
class MyThread(Thread):
    def __init__(self,bignum):
        Thread.__init__(self)
        self.bignum=bignum
    def run(self):
        for l in range(10):
            for k in range(self.bignum):
                res = 0
                #print "Res 0 ",res
                for i in range(self.bignum):
                    res+=1
                #print "Res 1 ",res
    
def myadd_nothread(bignum):
    for l in range(10):
        for k in range(bignum):
            res=0
            #print "1 st  loop Res 0 ",res    
            for i in range(bignum):
                res+=1
                #print "1 st loop Res 1 ",res
    for l in  range(10):
        for k in range(bignum):
            res = 0
            #print "2nd loop Res 0 ",res
            for i in range(bignum):
                res+=1
                #print "2nd loop Res 1",res
def thread_test(bignum):
    #We create 2 Thread objects for the 2 threads.
    thr1 = MyThread(bignum)
    thr2 = MyThread(bignum)
    
    thr1.start()
    thr2.start()
    
    thr1.join()
    thr2.join()
   
def test():
    bignum = 1000
    #Let us test the threading part
    
    starttime = time.clock()
    thread_test(bignum)
    stoptime = time.clock()
    print "Running 2 threads took %.3f seconds " %(stoptime-starttime)
    
    starttime = time.clock()
    myadd_nothread(bignum)
    #thread_test(1000)
    stoptime = time.clock()
    print "Running Without Threads took %.3f seconds"%(stoptime-starttime)

if __name__ == "__main__":
    test()

            
        
        
                