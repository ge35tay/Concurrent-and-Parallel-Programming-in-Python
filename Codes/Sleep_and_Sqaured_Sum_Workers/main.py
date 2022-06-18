import time
import threading
from workers.SleepyWorkers import SleepyWorker
from workers.SquaredSumWorkers import SquaredSumWorker


def main():
    calc_start_time = time.time()

    current_workers = []
    for i in range(5):
        maximum_value = (i+1) * 1000000
        squaredSumWorker = SquaredSumWorker(n=maximum_value)
        # t = threading.Thread(target=calculate_sun_squares, args=(maximum_value, ), daemon=False)   # ! no parentness here, just call a reference to the function, args is a tuple
        # t.start()    #! need to call the start function here
        current_workers.append(squaredSumWorker)   #! append current thread, so we can reference later
        # calculate_sun_squares(maximum_value)
    

    for i in range(len(current_workers)):
        current_workers[i].join()   #! block the execution until the thread is done, otherwise nothing would happen
    print("Calculating sum of sqaures took: ", round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()
    current_workers = []
    for second in range(1, 6):
        # t = threading.Thread(target=sleep_a_little, args =  (second, ), daemon=False)
        # t.start()
        sleepyWorker = SleepyWorker(seconds=second)
        current_workers.append(sleepyWorker)
        # sleep_a_little(second)
    
    for i in range(len(current_workers)):
        current_workers[i].join()  # 
    print("Calculating sum of sqaures took: ", round(time.time() - calc_start_time, 1))
    
    print("Sleep took: ", round(time.time() - sleep_start_time, 1))  # ? you can notice that the sleeping time equal to maximum time


if __name__ == "__main__":
    main()
