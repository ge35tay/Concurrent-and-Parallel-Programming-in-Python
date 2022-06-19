from threading import Thread
from multiprocessing import Process, Queue, Pool, cpu_count
from functools import partial
import time

def square(x, y):   
    return x ** y


num_processes = 4
comparison_list = [1, 2, 3]
num_of_cpu_available = cpu_count()
power_list = [4, 5, 6]
addition_component = 2
print("num_of_cpu_available ", num_of_cpu_available)
num_of_cpu_to_use = max(1, cpu_count() - 1)
print("num_of_cpu_to_use ", num_of_cpu_to_use)
start_time = time.time()


prepared_list = []
for i in range(len(comparison_list)):
    prepared_list.append((comparison_list[i], power_list[i]))

print("List to use as input: ", prepared_list)


with Pool(num_of_cpu_to_use) as multiprocessing_pool:     # ! a pool of process that we can use, if the pool is not fool, 
                                                          # ! they will create a new process for the request
    # result=multiprocessing_pool.map(square, (comparison_list, power))
    result=multiprocessing_pool.starmap(square, prepared_list)# [square(1, 4), square(2, 5), square(3, 6)]

print(result)
print("Everything took: ", time.time() - start_time, 'seconds')
