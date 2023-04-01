#!/usr/local/bin/python3

import os

flag = os.environ['FLAG']

def afis():
    print("""
    .-----------.
    |           |
    |         O |
    | SCRISOARE |
    |  PIERDUTA |
    |           |
    |     I.L.C |
    .___________.
    """)


def ascunde(data1, data2):
        
    plaintext_length = len(data1)
    assert (plaintext_length >= 3), "Eroare lungime mesaj"

    if plaintext_length % 3 != 0 :
        if 3 - (plaintext_length % 3) == 2 :
            data1.append(0)
            data1.append(0)
            data1 = plaintext_length + 2
        else:
            data1.append(0)
            plaintext_length = plaintext_length + 1

    complete_plaintext = []
    complete_plaintext.append(4)
    complete_plaintext.append(15)
    complete_plaintext.append(11)
    complete_plaintext.append(0)
    complete_plaintext.append(13)
    complete_plaintext.append(4)
    complete_plaintext.append(19)
    complete_plaintext.append(19)
    complete_plaintext.append(19)
    for i in data1:
        complete_plaintext.append(ord(i))
    plaintext_length = plaintext_length + 9

    key = data2
    assert (len(key) == 9), "Eroare lungime cheie"

    a11 = ord(key[0])
    a12 = ord(key[1])
    a13 = ord(key[2])
    a21 = ord(key[3])
    a22 = ord(key[4])
    a23 = ord(key[5])
    a31 = ord(key[6])
    a32 = ord(key[7])
    a33 = ord(key[8])
    
    i = 0
    ciphertext = []
    while i < plaintext_length :
        p11 = complete_plaintext[i+0]
        p21 = complete_plaintext[i+1]
        p31 = complete_plaintext[i+2]

        c11 = ( (a11 * p11) + (a12 * p21) + (a13 * p31) ) % 26
        c21 = ( (a21 * p11) + (a22 * p21) + (a23 * p31) ) % 26
        c31 = ( (a31 * p11) + (a32 * p21) + (a33 * p31) ) % 26

        ciphertext.append(c11)
        ciphertext.append(c21)
        ciphertext.append(c31)

        i = i + 3

    return ciphertext

def distribuie(data):
    distribuit = []
    for i in data:
        distribuit.append(i)
    return distribuit

def verifica(data):
    if data == [19, 16, 17, 24, 22, 8, 5, 15, \
                         16, 15, 4, 21, 1, 9, 18, 21, \
                         25, 0, 1, 19, 24, 25, 6, 11, \
                         22, 24, 24, 19, 13, 12, 13, \
                         1, 0, 22, 9, 3, 18, 15, 5, \
                         17, 23, 0, 9, 18, 19, 0, 2, \
                         10, 15, 11, 8, 7, 12, 3, 1, \
                         23, 22, 5, 10, 9, 24, 3, 23, \
                         9, 25, 18, 19, 12, 1, 11, 0, 19, 23, 16, 3]:
        return flag
    else:
        return "Interzis cetatenilor turmentate!"

if __name__ == "__main__":

    afis()

    mesaj = input(" Introduceti mesajul: ")
    cheie = input(" Introduceti cheia: ")
    print("[*] ",  verifica(ascunde(distribuie(mesaj), distribuie(cheie))))