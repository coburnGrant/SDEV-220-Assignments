import multiprocessing
import time
import random
from datetime import datetime

def print_date(wait_time: int):
    time.sleep(wait_time)
    print(f"[{multiprocessing.current_process().name}] Current time: {datetime.now()}")

def main():
    processes = []

    for i in range(3):
        wait = random.uniform(0, 1)
        p = multiprocessing.Process(
            target=print_date, 
            name=f"process {i}", 
            args=(wait,)
        )
        processes.append(p)

    print("Starting processes...")
    for p in processes:
        p.start()

    for p in processes:
        p.join()
    print("All processes have finished.")

if __name__ == "__main__":
    main()