#!/usr/bin/env python3
#-*-coding:UTF-8-*-

# Shortest Job First algorithm simulation
#
# Franciszek Plisz 264425


def sjf_sim(data, numberOfProcesses):
    """
    Funkcja zwracjaca liste procesow, wraz z czasami zakonczenia
    (completion time)
    """
    timer = 0
    queue = []  # kolejka procesow oczekajacych na wykonanie
    completed = []
    
    while True:
        if len(completed) == numberOfProcesses:
            return completed
        i = 0
        while i < len(data):
            if data[i][0] <= timer:  # sprawdzenie czy dany proces juz dotarl
                queue.append(data[i])  # gdy dotarl dodanie go do kolejki
                del data[i]
            else:
                i += 1
        queue = sorted(queue, key=lambda x: x[1])  # Sortowanie, by sprawdzic najmniejszy burst time
        if len(queue)!=0:
            current_process = queue[0]
            completion_time = current_process[1] + timer  # obliczanie czasu wykonania procesu
            completed.append((current_process[0],current_process[1], completion_time))
            timer = current_process[1] + timer
            queue.pop(0)  # usuniecie procesu z kolejki po jego wykonaniu
    
        else:
            timer+=1

def avgWaitingTime(data):
    """
    Funkcja sluzaca do obliczenia sredniego czasu oczekiwania
    """
    sum = 0
    for i in data:
        print(i)
        sum = i[2]-i[1]-i[0] + sum
    return sum/len(data)

def getData(filename="test.txt"):    
    """
    Funkcja odpowiadajaca za odczyt danych z datasetu
    """
    data = []
    file = open(filename)
    for line in file:
        splitted = []
        splitted = line.split(';')
        splitted[0] = int(splitted[0])
        splitted[1] = int(splitted[1])
        splitted[2] = int(splitted[2])
        data.append(splitted)
    return data


if __name__ == "__main__":
    """
    Glowna czesc programu, gdzie wywolywane sa
    wczesniej zadeklarowane funkcje.
    """        
    data = getData()
    print(data)
    solution = sjf_sim(data,len(data))
    print(avgWaitingTime(solution))