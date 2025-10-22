#!/usr/bin/env python3

from kostka import Kostka
from lod import Lod

class Sektor:
    '''
    Sprava souboje
    '''

    def __init__(self, lod_1, lod_2, kostka):
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka

    def _vypis_lod(self, lod):
        print()
        print(f'{lod}')
        print(f'{lod._trup} HP \n')

    def souboj(self):
        import random
        print()
        print("Vitej v Narnii!")
        print('================ \n')
        print(f'Dnes se stretnou {self._lod_1} a {self._lod_2}. \n')
        print('Zahajit souboj... \n')
        input()

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
        print('================= Sektor Narnie =================== \n')
        print('Lode: \n')
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print()

if __name__ == '__main__':
    k = Kostka(10)
    lod1 = Lod('Mr. Cupcake', 100, 20, 18, k)
    lod2 = Lod('Sand Man', 100, 15, 22, k)

    narnie = Sektor(lod1, lod2, k)
    narnie.souboj()
