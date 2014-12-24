import  time
import thread

def myfunction(string,sleeptime,*args):
    while 1:
        print string
        time.sleep(sleeptime) #sleep for a specified amount of time
if __name__ == "__main__" :
    thread.start_new(myfunction,("Thread N0 : 1 ",2))
    while 1 :pass