# Time module handles time-related tasks.

# time.time():
# It returns us the seconds of time that have elapsed since the Unix epoch. 
# In simple words, it tells us the time in seconds that have passed since 1 January 1970. 
# Its syntax is simple and easy to use.

import time
seconds = time.time()
print("Seconds in Epoch =", seconds)

localtime = time.asctime()
print(localtime)
# We use the function time.asctime() to print the local time onto the screen. 
# There are a lot of other ways to do it but time.asctime() prints the time in a sequence using a 24 characters string. 
# The format will be something like this: Mon Feb 10 08:01:02 2020

# time.sleep()
# What sleep() function does is, it delays the execution of further commands for given specific seconds.

# time.localtime()
# The time.localtime() is used to convert the number of seconds to local time. 
# This function takes seconds as a parameter and returns the date and time in time.struct_time format. 
# It is optional to pass seconds as a parameter. If seconds is not provided, 
# the current time will be returned by time() is used.

import time

initial = time.time()
k = 0
while(k<45):
    print("Hello world")
    # time.sleep(2)
    k+=1
print("While loop ran in", time.time() - initial, "seconds")

initial1 = time.time()
for i in range(45):
    print("Greetings of the day")
print("For loop ran in", time.time() - initial1, "seconds")