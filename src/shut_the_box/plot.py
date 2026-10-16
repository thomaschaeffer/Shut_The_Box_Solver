import matplotlib.pyplot as plt
import numpy as np
import time
from solver import win_probability_unoptimized,win_probability_optimized, memo

UNOPTIMIZED_RANGE = 8

if __name__=="__main__":
    unoptimized=[]
    optimized=[]
    x_unoptimized=[]
    x_optimized=[]

    for i in range(1,UNOPTIMIZED_RANGE + 1):
        remaining = set(range(1, i + 1))
        t1=time.time()
        win_probability_unoptimized(remaining)
        t2=time.time()
        unoptimized.append(t2-t1)
        x_unoptimized.append(i)

    for i in range(1,13):
        remaining = set(range(1, i + 1))
        t1=time.time()
        win_probability_optimized(remaining)
        t2=time.time()
        optimized.append(t2-t1)
        x_optimized.append(i)
        memo.clear()


    xpoints = np.array([1, 12])
    plt.plot(x_unoptimized, unoptimized, label="Curve 1")
    plt.plot(x_optimized, optimized, label="Curve 2")

    plt.xlabel("Number of tiles")
    plt.ylabel("Execution time (seconds)")
    plt.title("Time difference between the optimized curve and the non-optimized curve ")
    plt.legend()
    plt.grid(True)
    plt.show()
