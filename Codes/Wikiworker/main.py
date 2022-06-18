import time
from workers.YahooFinanceWorkers import YahooFinancePriceWorker
from workers.WikiWorker import WikiWorker

def main():
    calc_start_time = time.time()

    wikiWorker = WikiWorker()
    current_workers = []
    for symbol in wikiWorker.get_sp_500_companies():
        yahooFinancePriceWorker = YahooFinancePriceWorker(symbol=symbol)
        current_workers.append(yahooFinancePriceWorker)
    
    for i in range(len(current_workers)):
        current_workers[i].join()
    
    print("Extracting time took: ", round(time.tinḿe() - calc_start_time, 1))


if __name__ == '__main__':
    main()
