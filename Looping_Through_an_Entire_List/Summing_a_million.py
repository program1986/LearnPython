import time
# 

sum =0
# Geting the start time 
start_time = time.time()
for value in range (1,1000000):
    sum = sum +value

# Geting the end time
end_time = time.time()


print ("The sum is "+str(sum)+"."+"And the duration is "+str(end_time-start_time)+"s.")

# The output is 
# The sum is 499999500000.And the duration is 0.09946084022521973s.
