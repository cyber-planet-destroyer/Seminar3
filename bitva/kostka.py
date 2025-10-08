#!/usr/bin/env python3

import random

class Kostka:
    def __init__(self, pocet_sten):
        self.__pocet_sten = pocet_sten

    def __str__(self):
        return f"Toto je kostka se {self.__pocet_sten} stenami."

    def hod(self):
        return random.randint(1,self.__pocet_sten)

    def getPocet_sten(self):
        return self.__pocet_sten

def main():
    k1 = Kostka(6)
    k2 = Kostka(12)
    print(k1.hod())
    print(k2.hod())

if __name__ == '__main__':
    main()