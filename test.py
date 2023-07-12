from multiprocessing import Pool
import time


def f(x):
    time.sleep(0.5)
    return


if __name__ == "__main__":
    start_time = time.time()
    for i in range(10):
        f(i)
    end_time = time.time()
    print("Execution time 1 :", end_time - start_time, "seconds")
    start_time = time.time()
    with Pool(10) as p:
        p.map(f, range(10))
    end_time = time.time()
    print("Execution time 2 :", end_time - start_time, "seconds")
