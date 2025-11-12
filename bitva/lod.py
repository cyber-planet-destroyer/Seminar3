#!/usr/bin/env python3

class Lod:
    '''
    Zakladni trida reprezentujici bitevni lod.
    '''
    def __init__(self, jmeno, trup, utok, stit, kostka):
        self._jmeno = jmeno
        self._trup = trup
        self._max_trup = trup
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
            if self._trup < 0:
                self._trup = 0
                zprava = f'{zprava[:-1]} a byl(a) znicen(a)!!!!'
        else:
            zprava = f'{self._jmeno} odrazil(a) utok stitem!'
        self.nastav_zpravu(zprava)

    def graficky_ukazatel(self, aktualni,maximalni):
        celkem = 20
        pocet = int(aktualni / maximalni * celkem)
        if pocet == 0 and self.je_operacni():
            pocet = 1
        return f'[{"#"*pocet}{" "*(celkem - pocet)}]'


    def graficky_trup(self, trup, max_trup):
        return self.graficky_ukazatel(self._trup, self._max_trup)

    def je_operacni(self):
        return self._trup > 0 

    def nastav_zpravu(self, zprava):
        self._zprava = zprava 

    def vypis_zpravu(self):
        return self._zprava


class Stihac(Lod):
    def __init__(self, jmeno, trup, utok, stit, kostka, energie, laserovy_utok):
        super().__init__(jmeno, trup, utok, stit, kostka)
        self._energie = energie
        self._max_energie = energie
        self._laserovy_utok = laserovy_utok

    def utoc(self, souper):
        if self._energie < self._max_energie:
            self._energie = min(self._max_energie, self._energie + 10)
            super().utoc(souper)
        else:
            uder = self._laserovy_utok + self._kostka.hod()
            self.nastav_zpravu (f'{self._jmeno} utoci laserem za {uder} HP!!!')
            self._energie = 0
            souper.bran_se(uder)

    def graficka_energie(self):
        return self.graficky_ukazatel(self._energie, self._max_energie)


class Korveta(Lod):
    """
    bran se: k+2
    """
    def bran_se(self, uder):
        poskozeni = uder - (self._stit + self._kostka.hod() + 2)
        if poskozeni > 0:
            self._trup -= poskozeni
            if self._trup < 0:
                self._trup = 0
            self.nastav_zpravu(f'{self._jmeno} utrpela {poskozeni} HP po prurazu stitu!!')
        else:
            self.nastav_zpravu(f'{self._jmeno} zcela odrazila utok adaptivnim stitem.')
