#!/usr/bin/env python3

class Lod:
    '''
    Zakladni trida reprezentujici bitevni lod.
    '''
    def __init__(self, jmeno, trup, utok, stit, kostka):
        self._jmeno = jmeno
        self._trup = trup
        self._utok = utok 
        self._stit = stit
        self._kostka = kostka
        self._zprava = ''

    def __str__(self):
        return str(self._jmeno)

    def utoc(self, souper):
        uder = self._utok + self._kostka.hod()
        zprava = f'{self._jmeno} pali rakety za {uder} HP!!'
        self.nastav_zpravu(zprava)
        souper.bran_se(uder)

    def bran_se(self, uder):
        poskozeni = uder - (self._stit + self._kostka.hod())
        if poskozeni > 0:
            zprava = f'{self._jmeno} utrpel(a) zasah o sile {poskozeni} HP na trupu!'
            self._trup -= poskozeni
        else:
            zprava = f'{self._jmeno} odrazil(a) utok stitem!'
        self.nastav_zpravu(zprava)

    def je_operacni(self):
        return self._trup > 0 

    def nastav_zpravu(self, zprava):
        self._zprava = zprava 

    def vypis_zpravu(self):
        return self._zprava
