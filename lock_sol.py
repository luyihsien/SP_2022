from threading import Thread, Lock
some_var = 0
lo = Lock()
c=100

def some_func(id):
    global lo
    with lo:
        global some_var
        print("{} here!".format(id),c,200)
        for i in range(150):
            print('1', '2', '3', '4', '5')
            some_var += 1
        print("{} leaving!".format(id),c,200)
t1 = Thread(target=some_func, args=(1,))
t2 = Thread(target=some_func, args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()
print(some_var)