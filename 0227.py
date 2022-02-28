# -*- coding: UTF-8 -*-
""""
lock.sol跟0227不同在於lock.sol處理同一塊程式碼
"""
import threading
import time
import dis
lock = threading.Lock()
# 子執行緒的工作函數
def job(j):
    for i in range(j):
        print("Child thread:", i)
        time.sleep(1)

# 建立一個子執行緒
t = threading.Thread(target = job,args=(5,))

# 執行該子執行緒
t.start()

# 主執行緒繼續執行自己的工作
for i in range(3):
  print("Main thread:", i)
  time.sleep(1)

# 等待 t 這個子執行緒結束
t.join()

print("Done.")
"""
Child thread:Main thread: 0 0 似乎會印一半被斷掉 

Child thread: 1
Child thread:Main thread: 1
Main thread: 2
 2
Child thread: 3
Child thread: 4
Done.

Child thread:Main thread: 0
Main thread: 1
 0
Child thread: Main thread: 2
1
Child thread: 2
Child thread: 3
Child thread: 4
Done.

Child thread: 0
Child thread: 1Main thread:
 Child thread:0
Main thread: 1
 2
Child thread:Main thread: 3 2

Child thread: 4
Done.

"""
"""
印Child thread: 然後\n 然後數字 三階段 都可被突破
  Main thread: 
"""
dis.dis(job)