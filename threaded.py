import threading
global a

def do_something():
       print(f"{threading.current_thread().name} is running ")
       for i in range(1,1001):
              global a
              a = a+1
              print(a)


a = 0
thread1 = threading.Thread(target=do_something,name="Thread 1")
thread2 = threading.Thread(target=do_something,name="Thread 2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("the final val is:",a)
