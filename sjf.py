#!/usr/bin/env python3
#-*-coding:UTF-8-*-

import queue

class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.waiting_time = 0

def calculate_avg_waiting_time(processes, n):
    waiting_time = 0
    for i in range(n):
        waiting_time += processes[i].waiting_time
    return waiting_time / n

def SJF_scheduling(process_list, num_processes):
    q = queue.PriorityQueue()
    current_time = 0
    waiting_time = 0
    for i in range(num_processes):
        q.put((process_list[i].arrival_time, process_list[i].burst_time, process_list[i]))

    while not q.empty():
        current_process = q.get()[2]
        current_time += current_process.burst_time
        current_process.waiting_time = current_time - current_process.arrival_time - current_process.burst_time
        print("Zadanie", current_process.pid, "rozpoczyna się o czasie", current_time)

    avg_waiting_time = calculate_avg_waiting_time(process_list, num_processes)
    print("Średni czas oczekiwania:", avg_waiting_time)

# przykładowe zadania
process_list = [Process(1, 20, 2), Process(2, 8, 6), Process(3, 4, 6)]
num_processes = 3

# uruchamiamy algorytm
SJF_scheduling(process_list, num_processes)
