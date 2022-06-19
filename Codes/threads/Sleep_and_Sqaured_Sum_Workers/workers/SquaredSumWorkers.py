import threading


class SquaredSumWorker(threading.Thread):
    def __init__(self, n, **kwargs):
        self._n = n
        super(SquaredSumWorker, self).__init__()
        self.daemon = True
        self.start()    ## make sure the thread start running

    def _calculate_sum_squares(self):
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i ** 2
        print(sum_squares)

    def run(self):
        self._calculate_sum_squares()   ## create class and run
