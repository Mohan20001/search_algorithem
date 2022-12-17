import time

num = range(1,500+1)

target = 500
Tries = 1
value = -1

initial_time = time.time()
for item in num:
    if item == target:
        value = item
        break
    Tries += 1
    time.sleep(.1)

final_time = time.time()
#if it return negative value then the existence of target is absent.
print("target found: {}".format(value))
print("No of Tries: {}".format(Tries))
print("Excution time: {}".format(final_time-initial_time))
