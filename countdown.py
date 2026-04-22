import sys
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, flush=True)
        time.sleep(1)
        t -= 1
    print("Time's up!")

t = int(input("Input the amount of time in seconds: "))

countdown(t)

