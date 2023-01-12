#!/usr/bin/env python3
#-*-coding:UTF-8-*-

# FIFO page replacement simulation
#
# Franciszek Plisz 264425

def fifo(frameSize, data):
    """
    Funkcja, ktora oblicza ilosc bledow stron.
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


if __name__ == "__main__":
    """
    Glowna czesc programu, gdzie wywolywane sa
    wczesniej zadeklarowane funkcje.
    """
    pages_to_access = [1,2,2,2,2,2,2]
    page_faults = fifo(3, pages_to_access)
    print(f'Pages accessed: {pages_to_access}')
    print(f'Page faults: {page_faults}')