#!/usr/bin/env python3
#-*-coding:UTF-8-*-

data = [[2,6],[5,2],[1,8],[0,3],[4,4]] # arrival timer, burst timer
 
def sjf_sim(data, numberOfProcesses):
    timer = 0
    queue = []
    completed = []
    
    while True:
        if len(completed) == numberOfProcesses:
            return completed
        i = 0
        while i < len(data):
            if data[i][0] <= timer:
                queue.append(data[i])
                del data[i]
            else:
                i += 1
        queue = sorted(queue, key=lambda x: x[1])  # sort by bursttimer
        if len(queue)!=0:
            current_process = queue[0]
            completion_timer = current_process[1] + timer
            completed.append((current_process[0],current_process[1], completion_timer))
            timer = current_process[1] + timer
            queue.pop(0)
    
        else:
            timer+=1

def avgWaitingTime(data):
    sum = 0
    for i in data:
        print(i)
        sum = i[2]-i[1]-i[0] + sum
    return sum/len(data)
        

sol = sjf_sim(data,len(data))
print(len(sol))
print(avgWaitingTime(sol))