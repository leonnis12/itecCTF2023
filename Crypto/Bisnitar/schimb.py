#!/usr/local/bin/python3

import os
import requests

flag = os.environ['FLAG']
negustor_stoc_solidus = 10
negustor_stoc_nomisma = 10
client_stoc_solidus = 10
client_stoc_nomisma = 10
num_schimbari = 0




def afis():
    print("""
        _.-'~~`~~'-._
     .'`  A   N   A  `'.
    / M               S \\
  /`       .-'~"-.       `\\
 ; O      / `-    \      C ;
;        />  `.  -.|        ;
| R     /_     '-.__)     A |
|        |-  _.' \ |        |
;        `~~;     \\\\        ;
 ;   TARA   /      \\\\)P    ;
  \        '.___.-'`"     /
   `\                   /`
     '._   1 8 6 4   _.'
        `'-..,,,..-'`
    """)

def meniu():
    print('[1] Schimba')
    print('[2] Povesteste')
    print('[3] Paraseste')

def citeste():
    introdus = input('> ')
    return introdus

def povesteste():
    global num_schimbari, client_stoc_solidus, client_stoc_nomisma

    if num_schimbari <= 8:
        if client_stoc_nomisma + client_stoc_solidus == 4 * 10 - 1:
            return flag
        else:
            return "INCHIS"
    else:
        url = f"https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'text' in data.keys():
                return data['text']
            else:
                return "[!] Ne pare rau, a intervenit o eroare"
        else:
            return "[!] Ne pare rau, a intervenit o eroare"

def schimba():
    global num_schimbari, negustor_stoc_nomisma, negustor_stoc_solidus, client_stoc_nomisma, client_stoc_solidus

    print('[*] Ce moneda doriti sa schimbati? (N / S)')
    moneda = citeste()
    if moneda == 'N':
        print('[*] Introduceti suma pe care doriti sa o schimbati')
        suma = int(citeste(),10)
        if suma <= client_stoc_nomisma:

            x = negustor_stoc_nomisma
            y = negustor_stoc_solidus
            schimb = y - (x * y) // (x + suma);

            negustor_stoc_nomisma += suma
            negustor_stoc_solidus -= schimb 

            client_stoc_nomisma -= suma
            client_stoc_solidus += schimb 

            num_schimbari += 1

        else:
            print('[!] Fonduri induficiente!')

    elif moneda == 'S':
        print('[*] Introduceti suma pe care doriti sa o schimbati')
        suma = int(citeste(),10)
        if suma <= client_stoc_solidus:

            x = negustor_stoc_solidus
            y = negustor_stoc_nomisma
            schimb = y - (x * y) // (x + suma);

            negustor_stoc_solidus += suma 
            negustor_stoc_nomisma -= schimb
            
            client_stoc_solidus -= suma 
            client_stoc_nomisma += schimb

            num_schimbari += 1

        else:
            print('[!] Fonduri insuficiente!')

    else:
        print('[!] Moneda incorecta!')

if __name__ == "__main__":

    afis()

    while 1:
        meniu()
        actiune = citeste()


        if actiune == '1':
            if(num_schimbari >= 8):
                print('[!] INCHIS!')
            else :
                schimba()
            continue
        elif actiune == '2':
            poveste = povesteste()
            print('[*] ' + str(poveste))
            continue
        elif actiune == '3':
            print('[*] La revedere!')
            break
        else:
            print('[!] Actiune invalida!')
            continue