import time
from turtledemo.penrose import start


# t = time.localtime()
#
# print(t)
# print(t[0])
# print(t.tm_year)
#
# t = time.strftime("%Y-%m-%d %H:%M:%S")
#
# print(t)

def pass_time():
    print("Start...")
    time.sleep(3)
    print("End!")

start_time = time.time()
pass_time()
end_time = time.time()
print("Time-consuming:", end_time-start_time)

t1 = time.gmtime()
print(t1)
