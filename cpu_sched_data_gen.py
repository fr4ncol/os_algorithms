#!/usr/bin/env python3
#-*-coding:UTF-8-*-

# Dataset generator used to generate data cpu scheduling algorithms simulations
#
# Franciszek Plisz 264425

import random

def gen(numberOfRecords, filename, randomRange):
    """
    format: arrive_time, burst_time, index
    """
    file = open(filename, 'w')
    for i in range(numberOfRecords):
        file.write(str(random.randint(0,randomRange))+';')  # arrival_time
        file.write(str(random.randint(1,randomRange))+';')  # burst_time
        file.write(str(i)+'\n')


if __name__ == "__main__":
    gen(10, 'test.txt', 9)