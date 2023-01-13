#!/usr/bin/env python3
#-*-coding:UTF-8-*-

# Dataset generator used to generate data for page replacement algorithms simulations
#
# Franciszek Plisz 264425

import random

def gen(numberOfRecords, filename, randomRange):
    file = open(filename, 'w')
    for i in range(numberOfRecords):
        file.write(str(random.randint(0,randomRange))+'\n')


if __name__ == "__main__":
    gen(600, 'test.txt', 9)