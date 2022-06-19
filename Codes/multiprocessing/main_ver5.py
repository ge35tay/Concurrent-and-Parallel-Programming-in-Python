from threading import Thread
from multiprocessing import Process, Queue, Pool, cpu_count
from functools import partial
import time

def check_number_of_values_in_range(comp_list, lower, upper):
    number_of_hits = 0
    for i in range(lower, upper):
        if i in comp_list:
            number_of_hits += 1
    return number_of_hits


num_processes = 4
comparison_list = [1, 2, 3]
lower_and_upper_bounds = [(0, 25*10**6), (25*10**6, 50*10**6), (50*10**6, 75*10**6), (75*10**6, 100*10**6)]
num_of_cpu_available = cpu_count()

addition_component = 2
print("num_of_cpu_available ", num_of_cpu_available)
num_of_cpu_to_use = max(1, cpu_count() - 1)
print("num_of_cpu_to_use ", num_of_cpu_to_use)
start_time = time.time()


prepared_list = []
for i in range(len(lower_and_upper_bounds)):
    # prepared_list.append((comparison_list, lower_and_upper_bounds[i][0], lower_and_upper_bounds[i][1]))
    prepared_list.append((comparison_list, *lower_and_upper_bounds[i]))  # !easier way

print("List to use as input: ", prepared_list)


with Pool(num_of_cpu_to_use) as multiprocessing_pool:     # ! a pool of process that we can use, if the pool is not fool, 
                                                          # ! they will create a new process for the request
    # result=multiprocessing_pool.map(square, (comparison_list, power))
    result=multiprocessing_pool.starmap(check_number_of_values_in_range, prepared_list)# [(comp_list, lower, upper)...]

print(result)
print("Everything took: ", time.time() - start_time, 'seconds')
