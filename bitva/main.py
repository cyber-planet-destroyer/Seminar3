#!/usr/bin/env python3

from kostka import Kostka
from lod import Lod, Stihac, Korveta

class Sektor:
    '''
    Sprava souboje
    '''

    def __init__(self, jmeno, lod_1, lod_2, kostka):
        self._jmeno = jmeno
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka

    def _vypis_lod(self, lod):
            print()
            print(f'{lod}')
            print(f'{lod.graficky_trup(lod._trup, lod._max_trup)} HP \n')
            if isinstance(lod, Stihac):
                print(f'Energie: {lod.graficka_energie()}')

    def souboj(self):
        import random
        print()
        print(f"Vitej v sektoru {self._jmeno}!")
        print(f'================={len(self._jmeno)*"="} \n')
        print(f'Dnes se stretnou {self._lod_1} a {self._lod_2}. \n')
        print('Zahajit souboj... \n')
        input()
        
        if random.randint(0, 1):
            self._lod_1, self._lod_2 = self._lod_2, self._lod_1

        while self._lod_1.je_operacni() and self._lod_2.je_operacni():
            self._lod_1.utoc(self._lod_2)
            self._vykreslit()
            self._vypis_zpravu(self._lod_1.vypis_zpravu())
            self._vypis_zpravu(self._lod_2.vypis_zpravu())
            self._vypis_lod(self._lod_2)

            if self._lod_2.je_operacni():
                self._lod_2.utoc(self._lod_1)
                self._vykreslit()
                self._vypis_zpravu(self._lod_2.vypis_zpravu())
                self._vypis_zpravu(self._lod_1.vypis_zpravu())
                self._vypis_lod(self._lod_1)
            else:
                print('GAME OVER!!! \n')

    def _vypis_zpravu(self, zprava):
        import time as _time
        if zprava:
            print(zprava)
            _time.sleep(0.5)

    def _vycisti(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call('clear')

    def _vykreslit(self):
        self._vycisti()
        print(f'================= {self._jmeno} =================== \n')
        print('Lode: \n')
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print()

if __name__ == '__main__':
    k = Kostka(30)
    l = Kostka(5)

    lod1 = Korveta('Mr. Cupcake', 100, 20, 18, k)
    lod2 = Stihac('Sand Man', 100, 15, 22, l, 60, 40)

    delta =  Sektor('Delta', lod1, lod2, k)
    m = Sektor("Muchomurka", lod1, lod2, k)

    delta.souboj()
    # m.souboj()
    
