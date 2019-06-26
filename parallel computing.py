# -*- coding: utf-8 -*-
# This script demonstrates a sample test on parallel computing v.s. serial
# computing.

import multiprocessing as mp
import time
from multiprocessing.pool import ThreadPool as Pool

# create sample function
def sum_of_cubes(n):
    return sum(x**3 for x in range(n))

# parallel computing
if __name__ == '__main__':
    
    pool = Pool(mp.cpu_count())
    start = time.time()
    res = pool.map(sum_of_cubes, range(1000, 100000, 1))
    end = time.time()
    print(end - start) # 1,961s
    
# serial computing
start = time.time()
res2 = list(map(sum_of_cubes, range(1000, 100000, 1)))
end = time.time()
print(end - start) # 7,789s


# Notes:  For a short / simple function, it is not worth computing in parallel 
# since that the dispatch overhead will dominate the actual computation time. 