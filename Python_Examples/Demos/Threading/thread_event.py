import thread
import time
from threading import *

def event_set(event):
    time.sleep(2)
    
    while 1:
        #We wait for the flag to be set.
        while not event.isSet():
            event.wait()
        print currentThread(),"...Woken Up"
        event.clear()

if __name__ == "__main__":
    event = Event()
    thread.start_new_thread(event_set,(event,))
    while 1:
        event.set()
        print event,"Has Been set "
        time.sleep(2)