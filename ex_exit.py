import time
import sys

for i in range(10):
    print(i)
    time.sleep(0.1)

    if i==8:
        print("종료")
        #sys.exit()
