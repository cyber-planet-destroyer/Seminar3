#!/usr/bin/env python3

filename = 'studenti.csv'

def readcsv(csvfile):
    with open(csvfile, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        print('\t'.join(line.strip().split(',')))
    return lines

def writecsv(csvfile):
    seznam = []
    seznam.append(input('Zadej jmeno: '))
    seznam.append(input('Zadej prijmeni: '))
    seznam.append(input('Zadej tridu: '))
    seznam.append(input('Zadej rok narozeni: '))
    record = ','.join(seznam)
    with open(csvfile, 'a', encoding='utf-8') as f:
        f.write(record)


def main(filename):
    print('1 - nacteni')
    print('2 - zapis')
    print('3 - konec')
    action = input(">> ")
    if action == '3':
        print('Bye.')
        exit()
    elif action == '2':
        writecsv(filename)
    elif action == '1':
        readcsv(filename)
    else:
        print('Nespravna volba.')

if __name__ == '__main__':
    main(filename)