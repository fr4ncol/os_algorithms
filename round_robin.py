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
        print("Czas: ", timer)
        print("Ukonczone: ", completed)
        if len(completed) == numberOfProcesses:
            return completed
        i = 0
        while i < len(data):
            if data[i][0] <= timer+quantum:  # sprawdzenie jakie procesy przyjda w czasie wykonywania aktualnego procesu
                queue.append(data[i])
                del data[i]
            else:
                i += 1
        print("Kolejka: ", queue)
        if len(queue)!=0:
            current_process = queue[0]
            print("Aktualnie wykonywany (ID): ",current_process[2], "\n")
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
        ct = completedData[i][2]  # completion time
        bt = inputData[i][1]  # burst time
        at = inputData[i][0]  # arrival time
        tat = ct-at  # turnaround time
        sum = (tat - bt) + sum
        i+=1
    return sum/len(inputData)

def getData(filename="dataSource/cpu_sched_source_file.txt"):    
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

def saveResults(result, inputData, quantumValue, filename="dataResults/cpu_sched_result_file.txt"):  # domyslne miejsce zapisu
    """
    Funkcja zapisujaca surowe dane.
    """
    arrival_times = []
    burst_times = []
    for i in inputData:
        arrival_times.append(i[0])
        burst_times.append(i[1])
    file = open(filename, 'a+')  # dane do pliku sa dopisywane
    file.write(f"Input data [arrival_time, burst_time, completion time, id]: {inputData} \n")
    file.write(f"Arrival times: {arrival_times} \n")
    file.write(f"Burst times: {burst_times} \n")
    file.write(f"Quantum value: {quantumValue} \n")
    file.write(f"Average waiting time: {result} \n")
    file.write("\n")
    file.close()    

if __name__ == "__main__":
    """
    Glowna czesc programu, gdzie wywolywane sa
    wczesniej zadeklarowane funkcje.
    """      
    quantum_time = 9  # ustawianie kwantu czasu
    data=getData()
    print(data)
    rr_solution = roundRobin(data, quantum_time, len(data))
    data = getData()
    avgTime = avgWaitTime(data, rr_solution)
    saveResults(avgTime, rr_solution, quantum_time)
    print(rr_solution)
    print(avgTime)
        