#!/usr/bin/env python3
#-*-coding:UTF-8-*-

# Dataset generator used to generate data for page replacement algorithms simulations
#
# Franciszek Plisz 264425

import random

def gen(numberOfRecords, filename, randomRange):
    file = open(filename, 'w')  # plik jest nadpisywany
    for i in range(numberOfRecords):
        file.write(str(random.randint(0,randomRange))+'\n')


if __name__ == "__main__":
    gen(15, 'dataSource/pr_source_file.txt', 9)
