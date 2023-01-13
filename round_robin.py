#!/usr/bin/env python3
#-*-coding:UTF-8-*-

# Round Robin algorithm simulation
#
# Franciszek Plisz 264425

def roundRobin(data, quantum, numberOfProcesses):
    timer = 0
    queue = []  # kolejka procesow
    completed = []  # zakonczone procesy
    data = sorted(data, key=lambda x: x[0])  # sortowanie po czasach przyjscia
    while True:
        if len(completed) == numberOfProcesses:
            return completed
        i = 0
        while i < len(data):
            if data[i][0] <= timer+quantum:  # sprawdzenie jakie procesy przyjda w czasie wykonywania aktualnego procesu
                queue.append(data[i])
                del data[i]
            else:
                i += 1
        if len(queue)!=0:
            current_process = queue[0]
            queue.pop(0)  # usuwanie pierwszego elementu z kolejki (w razie nie zakonczenia procesu zostanie dodany na koniec)
            if current_process[1] > quantum:  # sprawdzenie czy zdolamy wykonac proces w czasie naszego quantum
                current_process[1] = current_process[1] - quantum  # obliczanie czasu pozostalego do zakonczenia procesu
                queue.append(current_process)

                timer+=quantum
                
            else:  # gdy uda nam sie zakonczyc proces w danej jednostce czasu quantum
                completion_time = timer + current_process[1]
                completed.append((current_process[0],current_process[1], completion_time, current_process[2]))
                timer+=current_process[1]
    
        else:
            timer+=1

def avgWaitTime(inputData, completedData):
    """
    Funkcja obliczajaca sredni czas oczekiwania
    Sortuje dane wejsciowe i dane wykonywania po indexach, a nastepnie
    odejmuje burst time od czasu zakonczenia
    """
    inputData = sorted(inputData, key=lambda x: x[2])  # sort by index
    completedData = sorted(completedData, key=lambda x: x[3])  # sort by index
    sum = 0
    i = 0
    while i<len(inputData):
        sum = (completedData[i][2] - inputData[i][1]) + sum
        i+=1
    return sum/len(inputData)

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
    data=getData()
    print(roundRobin(data, 3, len(data)))
    print(avgWaitTime(data, roundRobin(data, 3, len(data))))
        


