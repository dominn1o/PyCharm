import time

timer = input("Enter the time in seconds: ")
timer = int(timer)

for sec in range(timer, 0, -1):
    print(sec)
    time.sleep(1)

print("end")