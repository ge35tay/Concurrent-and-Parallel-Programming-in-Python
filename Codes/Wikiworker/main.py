import time
from multiprocessing import Queue
from workers.YahooFinanceWorkers import YahooFinancePriceSchedular, YahooFinancePriceWorker
from workers.WikiWorker import WikiWorker

def main():
    symbol_queue = Queue()
    calc_start_time = time.time()

    wikiWorker = WikiWorker()
    yahoo_finance_price_schedular_threads = []
    num_yahoo_finance_price_workers = 4    # 4 workers,
    '''
    4 workers are running, each of the workers are waiting to read the queue
    whenever a symbol put in it they are start to read from it and doing their work
    '''
    for i in range(num_yahoo_finance_price_workers):
        yahooFinancePriceSchedular = YahooFinancePriceSchedular(input_queue=symbol_queue)   # ! schedular read from queue
        yahoo_finance_price_schedular_threads.append(yahooFinancePriceSchedular)

    #current_workers = []

    for symbol in wikiWorker.get_sp_500_companies():
        symbol_queue.put(symbol)   # put symbol in the queue and schedular read from it, all process independent from each other

    #     yahooFinancePriceWorker = YahooFinancePriceWorker(symbol=symbol)
    #     current_workers.append(yahooFinancePriceWorker)
    
    # for i in range(len(current_workers)):
    #     current_workers[i].join()

    for i in range(len(yahoo_finance_price_schedular_threads)):   # ! eyery thread gets single one value and 
        symbol_queue.put('DONE')   # ! waiting for the DONE value in YahooFinancePriceSchedular. once we done, then the class exist out

    for i in range(len(yahoo_finance_price_schedular_threads)):
        yahoo_finance_price_schedular_threads[i].join()
    # print(symbol_queue)
    # print(symbol_queue.get())

    
    print("Extracting time took: ", round(time.time() - calc_start_time, 1))


if __name__ == '__main__':
    main()
