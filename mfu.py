#!/usr/bin/env python3
#-*-coding:UTF-8-*-

# MFU page replacement algorithm simulation
#
# Franciszek Plisz 264425

def mfu(frameSize, data):
    """
    Funkcja, ktora oblicza ilosc bledow stron.
    Pozwala na uzycie dowolnej dlugosci ramki oraz
    dowolnej ilosci stron.
    """
    page_faults = 0  # ilosc bledow stron
    time_count = 0  # czas sluzacy do sprawdzania ktora strona jest starsza w przypadku rownej czestotliwosci
    page_list = []  # lista stron w kolejce
    page_frequency = {}  # slownik przechowujacy czestotliwosc wystepowania danej strony
    page_age = {}  # slownik przechowujacy wiek stron w kolejce

    for page in data:
        if page not in page_list:
            page_faults += 1
            if len(page_list) == frameSize:
                max_frequency = max(page_frequency.values())  # sprawdzenie najczestszej strony
                same_frequency_pages = [k for k, v in page_frequency.items() if v == max_frequency]  # lista z powtorzajacymi sie najczestszymi stronami
                if len(same_frequency_pages) > 1:  # sprawdzenie czy wystepuja powtorzenia
                    oldest_page = min(same_frequency_pages, key=lambda x: page_age[x])  # wyszukiwanie najstarszego page'a
                    page_list.remove(oldest_page)
                    del page_frequency[oldest_page]
                    del page_age[oldest_page]
                else:
                    oldest_page = same_frequency_pages[0]
                    page_list.remove(oldest_page)
                    del page_frequency[oldest_page]
                    del page_age[oldest_page]
            page_list.append(page)
            page_frequency[page] = 1
            if page not in page_age:  # warunek, ktory nie pozwala "aktualizowac" sie page_age w wypadku wystepowania w slowniku
                page_age[page] = time_count
            time_count += 1
        else:
            page_frequency[page] += 1
            if page not in page_age:
                page_age[page] = time_count
            time_count += 1

    return page_faults

def getData(filename="test.txt"):  # domyslna wartosc test.txt
    """
    Funkcja odpowiadajaca za odczyt danych z datasetu
    """
    data = []
    file = open(filename)
    for line in file:
        data.append(int(line))
    return data


if __name__ == "__main__":
    """
    Glowna czesc programu, gdzie wywolywane sa
    wczesniej zadeklarowane funkcje.
    """
    print(mfu(3, getData()))
