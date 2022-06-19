from threading import Thread
from multiprocessing import Process, Queue, Pool, cpu_count
from functools import partial
import time

def square(y, addition_component, x):   # ! provided parametere should be in a specific order, the basic variable that we want to change should be in very end
    print(x)
    return x ** y + addition_component


num_processes = 4
comparison_list = [1, 2, 3]
num_of_cpu_available = cpu_count()
power = 3
addition_component = 2
print("num_of_cpu_available ", num_of_cpu_available)
num_of_cpu_to_use = max(1, cpu_count() - 1)
print("num_of_cpu_to_use ", num_of_cpu_to_use)
start_time = time.time()

partial_function = partial(square, power, addition_component)   # ! provide the first parameter as power, so the function should be in order

with Pool(num_of_cpu_to_use) as multiprocessing_pool:     # ! a pool of process that we can use, if the pool is not fool, 
                                                          # ! they will create a new process for the request
    # result=multiprocessing_pool.map(square, (comparison_list, power))
    result=multiprocessing_pool.map(partial_function, comparison_list)

print(result)
print("Everything took: ", time.time() - start_time, 'seconds')
