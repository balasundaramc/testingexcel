import threading
import time

# The worker loops for about 1 minute adding numbers to a set
# unless the event is set, at which point it breaks the loop and terminates
def worker(e):
    data = set()
    for i in range(60):
        data.add(i)
        if not e.isSet():
            print "foo"
            time.sleep(1)
        else:
            print "bar"
            break
			
			
#ihave added the new comments			

e = threading.Event()
t = threading.Thread(target=worker, args=(e,))
t.start()

# wait 30 seconds for the thread to finish its work
t.join(30)

# Always signal the event. Whether the thread has already finished or not, 
# the result will be the same.
e.set()

# Now join without a timeout knowing that the thread is either already 
# finished or will finish "soon."
t.join()


