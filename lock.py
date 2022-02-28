from threading import Thread, Lock
some_var = 0

def some_func(id):
    lo = Lock()
    with lo:
        global some_var
        print("{} here!".format(id),100,2000,30000)
        print("!".format(id), 100, 2000, 12232)
        for i in range(100):
            print('1','2','3','4','5')
            some_var += 1
        print("{} leaving!".format(id),100,2000,12232)


t1 = Thread(target=some_func, args=(1,))
t2 = Thread(target=some_func, args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()
print(some_var)