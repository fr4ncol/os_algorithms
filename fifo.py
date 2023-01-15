#!/usr/bin/env python3
#-*-coding:UTF-8-*-

# FIFO page replacement simulation
#
# Franciszek Plisz 264425

def fifo(frameSize, data):
    """
    Funkcja, ktora oblicza ilosc bledow stron.m
    Pozwala na uzycie dowolnej dlugosci ramki oraz
    dowolnej ilosci stron.
    """
    pages = []  # lista przechowujaca strony w kolejce
    page_faults = 0  # zmienna przechowywujaca liczbe bledow stron
    for page in data:
        if page not in pages:  
            page_faults += 1
            if len(pages) == frameSize:
                pages.pop(0)  # wyrzucenie strony z poczatku kolejki
            pages.append(page)  # dodanie strony na jej koniec
    return page_faults

def getData(filename="dataSource/pr_source_file.txt"):  # domyslna wartosc lokalizacja pilku
    """
    Funkcja odpowiadajaca za odczyt danych z datasetu
    """
    data = []
    file = open(filename)
    for line in file:
        data.append(int(line))
    return data

def saveResults(result, inputData, filename="dataResults/pr_result_file.txt"):
    """
    Funkcja zapisujaca surowe dane.
    """
    pageCount = len(inputData)
    file = open(filename, 'a+')  # dane do pliku sa dopisywane
    file.write(f"Input data: {inputData} \n")
    file.write(f"Number of pages: {pageCount} \n")
    file.write(f"FIFO algorithm page faults: {result} \n")
    file.write("\n")
    file.close()



if __name__ == "__main__":
    """
    Glowna czesc programu, gdzie wywolywane sa
    wczesniej zadeklarowane funkcje.
    """
    data = getData()
    page_faults = fifo(3, getData())  # algorytm fifo o ramce 3
    print("Dane wejsciowe: ", data)
    print("Page faults: ", page_faults)
    saveResults(page_faults, data)
    