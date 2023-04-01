#!/usr/local/bin/python3

def afis():
    print("""
         |/|
         |/|
         |/|
         |/|
         |/|
         |/|
         |/| /�)
         |/|/\/
         |/|\/
        (���)
        (���)
        (���)
        (���)
        (���)
        /��/\\
       / ,^./\\
      / /   \/\\
     / /     \/\\
    ( (       )/)
    | |       |/|
    | |       |/|
    | |       |/|
    ( (       )/)
     \ \     / /
      \ `---' /
       `-----' 
    """)
    
def citeste():
    introdus = input('> ')
    return introdus

if __name__ == "__main__":
    afis()

    print("[*] Introduceti cuvantul pentru ghicit")
    cuvant = citeste()

    assert len(cuvant) == 51

    tmp1 = ord(cuvant[2]) 
    tmp2 = ord(cuvant[3]) 
    assert (tmp1 ^ 27) ^ tmp2 == 29 

    tmp1 = ord(cuvant[3]) 
    tmp2 = ord(cuvant[27]) 
    assert (tmp1 ^ 91) ^ tmp2 == 118 

    tmp1 = ord(cuvant[13]) 
    tmp2 = ord(cuvant[16]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2736 

    tmp1 = ord(cuvant[10]) 
    tmp2 = ord(cuvant[15]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 21996 

    tmp1 = ord(cuvant[45]) 
    tmp2 = ord(cuvant[13]) 
    assert (tmp1 * tmp2) == 5200 

    tmp1 = ord(cuvant[38]) 
    tmp2 = ord(cuvant[39]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 5472 

    tmp1 = ord(cuvant[18]) 
    tmp2 = ord(cuvant[50]) 
    assert (tmp1 & tmp2) == 93 

    tmp1 = ord(cuvant[46]) 
    tmp2 = ord(cuvant[6]) 
    assert (tmp1 + tmp2) == 165 

    tmp1 = ord(cuvant[31]) 
    assert ((tmp1 >> 7) & 29) == 0 

    tmp1 = ord(cuvant[20]) 
    tmp2 = ord(cuvant[6]) 
    assert (tmp1 * tmp2) == 5814 

    tmp1 = ord(cuvant[14]) 
    assert (tmp1 & 125) == 116 

    tmp1 = ord(cuvant[23]) 
    tmp2 = ord(cuvant[38]) 
    assert (tmp1 + tmp2) == 104 

    tmp1 = ord(cuvant[49]) 
    tmp2 = ord(cuvant[0]) 
    assert (tmp1 & tmp2) == 0 

    tmp1 = ord(cuvant[17]) 
    assert ((tmp1 >> 4) & 249) == 1 

    tmp1 = ord(cuvant[17]) 
    tmp2 = ord(cuvant[7]) 
    assert (tmp1 * tmp2) == 2548 

    tmp1 = ord(cuvant[15]) 
    tmp2 = ord(cuvant[28]) 
    assert (tmp1 ^ 78) ^ tmp2 == 15 

    tmp1 = ord(cuvant[35]) 
    tmp2 = ord(cuvant[27]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 4840 

    tmp1 = ord(cuvant[30]) 
    tmp2 = ord(cuvant[15]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 50544 

    tmp1 = ord(cuvant[3]) 
    tmp2 = ord(cuvant[39]) 
    assert (tmp1 * tmp2) == 7638 

    tmp1 = ord(cuvant[28]) 
    tmp2 = ord(cuvant[21]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 19760 

    tmp1 = ord(cuvant[19]) 
    tmp2 = ord(cuvant[48]) 
    assert (tmp1 + tmp2) == 151 

    tmp1 = ord(cuvant[28]) 
    tmp2 = ord(cuvant[0]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 3796 

    tmp1 = ord(cuvant[24]) 
    tmp2 = ord(cuvant[37]) 
    assert (tmp1 - tmp2) == 40 

    tmp1 = ord(cuvant[48]) 
    tmp2 = ord(cuvant[13]) 
    assert (tmp1 ^ 194) ^ tmp2 == 197 

    tmp1 = ord(cuvant[23]) 
    assert ((tmp1 >> 2) & 127) == 13 

    tmp1 = ord(cuvant[41]) 
    tmp2 = ord(cuvant[45]) 
    assert (tmp1 + tmp2) == 197 

    tmp1 = ord(cuvant[11]) 
    tmp2 = ord(cuvant[48]) 
    assert (tmp1 - tmp2) == 1 

    tmp1 = ord(cuvant[36]) 
    tmp2 = ord(cuvant[31]) 
    assert (tmp1 - tmp2) == -65 

    tmp1 = ord(cuvant[42]) 
    tmp2 = ord(cuvant[9]) 
    assert (tmp1 * tmp2) == 5995 

    tmp1 = ord(cuvant[17]) 
    tmp2 = ord(cuvant[31]) 
    assert (tmp1 - tmp2) == -68 

    tmp1 = ord(cuvant[22]) 
    tmp2 = ord(cuvant[17]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 1176 

    tmp1 = ord(cuvant[30]) 
    tmp2 = ord(cuvant[39]) 
    assert (tmp1 ^ 133) ^ tmp2 == 154 

    tmp1 = ord(cuvant[43]) 
    tmp2 = ord(cuvant[47]) 
    assert (tmp1 - tmp2) == -46 

    tmp1 = ord(cuvant[20]) 
    tmp2 = ord(cuvant[44]) 
    assert (tmp1 * tmp2) == 4845 

    tmp1 = ord(cuvant[28]) 
    tmp2 = ord(cuvant[18]) 
    assert (tmp1 + tmp2) == 147 

    tmp1 = ord(cuvant[36]) 
    tmp2 = ord(cuvant[7]) 
    assert (tmp1 * tmp2) == 2704 

    tmp1 = ord(cuvant[16]) 
    tmp2 = ord(cuvant[8]) 
    assert (tmp1 * tmp2) == 5586 

    tmp1 = ord(cuvant[46]) 
    tmp2 = ord(cuvant[40]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 10560 

    tmp1 = ord(cuvant[15]) 
    tmp2 = ord(cuvant[35]) 
    assert (tmp1 & tmp2) == 85 

    tmp1 = ord(cuvant[42]) 
    tmp2 = ord(cuvant[45]) 
    assert (tmp1 & tmp2) == 36 

    tmp1 = ord(cuvant[27]) 
    assert ((tmp1 >> 4) & 25) == 0 

    tmp1 = ord(cuvant[48]) 
    tmp2 = ord(cuvant[40]) 
    assert (tmp1 + tmp2) == 161 

    tmp1 = ord(cuvant[2]) 
    tmp2 = ord(cuvant[20]) 
    assert (tmp1 ^ 77) ^ tmp2 == 59 

    tmp1 = ord(cuvant[22]) 
    assert ((tmp1 >> 1) & 117) == 17 

    tmp1 = ord(cuvant[42]) 
    tmp2 = ord(cuvant[13]) 
    assert (tmp1 * tmp2) == 2860 

    tmp1 = ord(cuvant[27]) 
    assert (tmp1 & 165) == 36 

    tmp1 = ord(cuvant[43]) 
    tmp2 = ord(cuvant[17]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 4704 

    tmp1 = ord(cuvant[23]) 
    tmp2 = ord(cuvant[49]) 
    assert (tmp1 + tmp2) == 104 

    tmp1 = ord(cuvant[1]) 
    tmp2 = ord(cuvant[50]) 
    assert (tmp1 ^ 86) ^ tmp2 == 127 

    tmp1 = ord(cuvant[32]) 
    tmp2 = ord(cuvant[31]) 
    assert (tmp1 + tmp2) == 231 

    tmp1 = ord(cuvant[48]) 
    tmp2 = ord(cuvant[15]) 
    assert (tmp1 * tmp2) == 5967 

    tmp1 = ord(cuvant[41]) 
    tmp2 = ord(cuvant[44]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 36480 

    tmp1 = ord(cuvant[29]) 
    assert ((tmp1 >> 1) & 11) == 11 

    tmp1 = ord(cuvant[33]) 
    tmp2 = ord(cuvant[34]) 
    assert (tmp1 ^ 13) ^ tmp2 == 81 

    tmp1 = ord(cuvant[41]) 
    tmp2 = ord(cuvant[38]) 
    assert (tmp1 ^ 115) ^ tmp2 == 38 

    tmp1 = ord(cuvant[6]) 
    tmp2 = ord(cuvant[44]) 
    assert (tmp1 - tmp2) == 19 

    tmp1 = ord(cuvant[4]) 
    tmp2 = ord(cuvant[18]) 
    assert (tmp1 ^ 149) ^ tmp2 == 177 

    tmp1 = ord(cuvant[8]) 
    tmp2 = ord(cuvant[47]) 
    assert (tmp1 + tmp2) == 144 

    tmp1 = ord(cuvant[18]) 
    assert (tmp1 & 241) == 81 

    tmp1 = ord(cuvant[7]) 
    assert (tmp1 & 32) == 32 

    tmp1 = ord(cuvant[18]) 
    assert ((tmp1 >> 2) & 10) == 2 

    tmp1 = ord(cuvant[22]) 
    assert ((tmp1 >> 5) & 91) == 1 

    tmp1 = ord(cuvant[1]) 
    assert (tmp1 & 18) == 16 

    tmp1 = ord(cuvant[27]) 
    tmp2 = ord(cuvant[48]) 
    assert (tmp1 - tmp2) == 59 

    tmp1 = ord(cuvant[37]) 
    tmp2 = ord(cuvant[18]) 
    assert (tmp1 - tmp2) == -40 

    tmp1 = ord(cuvant[13]) 
    assert (tmp1 & 21) == 20 

    tmp1 = ord(cuvant[36]) 
    tmp2 = ord(cuvant[18]) 
    assert (tmp1 & tmp2) == 20 

    tmp1 = ord(cuvant[41]) 
    tmp2 = ord(cuvant[5]) 
    assert (tmp1 - tmp2) == -19 

    tmp1 = ord(cuvant[8]) 
    tmp2 = ord(cuvant[15]) 
    assert (tmp1 + tmp2) == 166 

    tmp1 = ord(cuvant[48]) 
    tmp2 = ord(cuvant[25]) 
    assert (tmp1 & tmp2) == 48 

    tmp1 = ord(cuvant[40]) 
    assert (tmp1 & 138) == 10 

    tmp1 = ord(cuvant[27]) 
    tmp2 = ord(cuvant[3]) 
    assert (tmp1 - tmp2) == 43 

    tmp1 = ord(cuvant[29]) 
    assert (tmp1 & 189) == 29 

    tmp1 = ord(cuvant[29]) 
    tmp2 = ord(cuvant[43]) 
    assert (tmp1 & tmp2) == 17 

    tmp1 = ord(cuvant[6]) 
    tmp2 = ord(cuvant[39]) 
    assert (tmp1 & tmp2) == 114 

    tmp1 = ord(cuvant[5]) 
    tmp2 = ord(cuvant[14]) 
    assert (tmp1 & tmp2) == 116 

    tmp1 = ord(cuvant[31]) 
    assert (tmp1 & 205) == 69 

    tmp1 = ord(cuvant[27]) 
    assert (tmp1 & 68) == 68 

    tmp1 = ord(cuvant[44]) 
    assert ((tmp1 >> 6) & 18) == 0 

    tmp1 = ord(cuvant[29]) 
    tmp2 = ord(cuvant[4]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 10824 

    tmp1 = ord(cuvant[50]) 
    tmp2 = ord(cuvant[20]) 
    assert (tmp1 & tmp2) == 49 

    tmp1 = ord(cuvant[29]) 
    assert ((tmp1 >> 3) & 183) == 3 

    tmp1 = ord(cuvant[24]) 
    assert ((tmp1 >> 1) & 206) == 14 

    tmp1 = ord(cuvant[15]) 
    tmp2 = ord(cuvant[50]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 29000 

    tmp1 = ord(cuvant[47]) 
    tmp2 = ord(cuvant[42]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 5060 

    tmp1 = ord(cuvant[13]) 
    tmp2 = ord(cuvant[24]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 4940 

    tmp1 = ord(cuvant[39]) 
    assert ((tmp1 >> 7) & 192) == 0 

    tmp1 = ord(cuvant[23]) 
    tmp2 = ord(cuvant[40]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 11440 

    tmp1 = ord(cuvant[13]) 
    tmp2 = ord(cuvant[47]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 4940 

    tmp1 = ord(cuvant[38]) 
    tmp2 = ord(cuvant[44]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 9880 

    tmp1 = ord(cuvant[29]) 
    assert ((tmp1 >> 1) & 103) == 39 

    tmp1 = ord(cuvant[15]) 
    assert ((tmp1 >> 5) & 66) == 2 

    tmp1 = ord(cuvant[1]) 
    assert ((tmp1 >> 6) & 107) == 1 

    tmp1 = ord(cuvant[27]) 
    tmp2 = ord(cuvant[28]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 2808 

    tmp1 = ord(cuvant[19]) 
    assert ((tmp1 >> 4) & 228) == 4 

    tmp1 = ord(cuvant[37]) 
    assert ((tmp1 >> 6) & 29) == 0 

    tmp1 = ord(cuvant[3]) 
    tmp2 = ord(cuvant[40]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1760 

    tmp1 = ord(cuvant[47]) 
    assert ((tmp1 >> 7) & 123) == 0 

    tmp1 = ord(cuvant[21]) 
    tmp2 = ord(cuvant[19]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 37600 

    tmp1 = ord(cuvant[35]) 
    tmp2 = ord(cuvant[17]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 18424 

    tmp1 = ord(cuvant[0]) 
    tmp2 = ord(cuvant[26]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 14976 

    tmp1 = ord(cuvant[5]) 
    assert ((tmp1 >> 7) & 82) == 0 

    tmp1 = ord(cuvant[34]) 
    assert ((tmp1 >> 1) & 163) == 34 

    tmp1 = ord(cuvant[21]) 
    tmp2 = ord(cuvant[16]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 21432 

    tmp1 = ord(cuvant[38]) 
    assert ((tmp1 >> 1) & 153) == 24 

    tmp1 = ord(cuvant[41]) 
    assert ((tmp1 >> 7) & 222) == 0 

    tmp1 = ord(cuvant[35]) 
    assert ((tmp1 >> 4) & 117) == 5 

    tmp1 = ord(cuvant[2]) 
    tmp2 = ord(cuvant[44]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 6460 

    tmp1 = ord(cuvant[8]) 
    assert ((tmp1 >> 5) & 123) == 1 

    tmp1 = ord(cuvant[29]) 
    assert ((tmp1 >> 4) & 108) == 4 

    tmp1 = ord(cuvant[27]) 
    assert ((tmp1 >> 5) & 88) == 0 

    tmp1 = ord(cuvant[10]) 
    assert ((tmp1 >> 4) & 112) == 0 

    tmp1 = ord(cuvant[6]) 
    assert ((tmp1 >> 3) & 127) == 14 

    tmp1 = ord(cuvant[14]) 
    assert ((tmp1 >> 4) & 140) == 4 

    tmp1 = ord(cuvant[34]) 
    tmp2 = ord(cuvant[44]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 20520 

    tmp1 = ord(cuvant[29]) 
    assert ((tmp1 >> 2) & 40) == 0 

    tmp1 = ord(cuvant[17]) 
    assert ((tmp1 >> 2) & 93) == 12 

    tmp1 = ord(cuvant[1]) 
    assert ((tmp1 >> 4) & 128) == 0 

    tmp1 = ord(cuvant[41]) 
    assert ((tmp1 >> 3) & 196) == 4 

    tmp1 = ord(cuvant[13]) 
    assert ((tmp1 >> 2) & 158) == 12 

    tmp1 = ord(cuvant[9]) 
    assert ((tmp1 >> 3) & 197) == 5 

    tmp1 = ord(cuvant[22]) 
    tmp2 = ord(cuvant[23]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 2600 

    tmp1 = ord(cuvant[28]) 
    tmp2 = ord(cuvant[17]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 2352 

    tmp1 = ord(cuvant[25]) 
    tmp2 = ord(cuvant[32]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 3192 

    tmp1 = ord(cuvant[40]) 
    assert ((tmp1 >> 2) & 222) == 26 

    tmp1 = ord(cuvant[19]) 
    tmp2 = ord(cuvant[48]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 10200 

    tmp1 = ord(cuvant[5]) 
    assert ((tmp1 >> 2) & 155) == 25 

    tmp1 = ord(cuvant[36]) 
    tmp2 = ord(cuvant[22]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 2652 

    tmp1 = ord(cuvant[31]) 
    tmp2 = ord(cuvant[15]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 6552 

    tmp1 = ord(cuvant[30]) 
    assert ((tmp1 >> 7) & 178) == 0 

    tmp1 = ord(cuvant[0]) 
    assert ((tmp1 >> 7) & 50) == 0 

    tmp1 = ord(cuvant[6]) 
    assert ((tmp1 >> 7) & 175) == 0 

    tmp1 = ord(cuvant[31]) 
    assert ((tmp1 >> 5) & 109) == 1 

    tmp1 = ord(cuvant[0]) 
    tmp2 = ord(cuvant[46]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 7344 

    tmp1 = ord(cuvant[46]) 
    assert ((tmp1 >> 4) & 17) == 1 

    tmp1 = ord(cuvant[38]) 
    assert ((tmp1 >> 7) & 179) == 0 

    tmp1 = ord(cuvant[24]) 
    tmp2 = ord(cuvant[11]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 4784 

    tmp1 = ord(cuvant[8]) 
    tmp2 = ord(cuvant[41]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1164 

    tmp1 = ord(cuvant[47]) 
    assert ((tmp1 >> 6) & 227) == 1 

    tmp1 = ord(cuvant[7]) 
    tmp2 = ord(cuvant[26]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 5408 

    tmp1 = ord(cuvant[35]) 
    tmp2 = ord(cuvant[43]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1078 

    tmp1 = ord(cuvant[19]) 
    assert ((tmp1 >> 2) & 135) == 1 

    tmp1 = ord(cuvant[21]) 
    assert ((tmp1 >> 6) & 55) == 1 

    tmp1 = ord(cuvant[27]) 
    assert ((tmp1 >> 1) & 57) == 49 

    tmp1 = ord(cuvant[50]) 
    assert ((tmp1 >> 2) & 120) == 24 

    tmp1 = ord(cuvant[43]) 
    tmp2 = ord(cuvant[48]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 2448 

    tmp1 = ord(cuvant[6]) 
    assert ((tmp1 >> 4) & 89) == 1 

    tmp1 = ord(cuvant[29]) 
    tmp2 = ord(cuvant[19]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 9200 

    tmp1 = ord(cuvant[36]) 
    assert ((tmp1 >> 7) & 238) == 0 

    tmp1 = ord(cuvant[16]) 
    assert ((tmp1 >> 1) & 70) == 0 

    tmp1 = ord(cuvant[3]) 
    assert ((tmp1 >> 6) & 134) == 0 

    tmp1 = ord(cuvant[19]) 
    assert ((tmp1 >> 3) & 82) == 0 

    tmp1 = ord(cuvant[28]) 
    tmp2 = ord(cuvant[8]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 2548 

    tmp1 = ord(cuvant[48]) 
    assert ((tmp1 >> 7) & 120) == 0 

    tmp1 = ord(cuvant[22]) 
    assert ((tmp1 >> 2) & 169) == 8 

    tmp1 = ord(cuvant[48]) 
    tmp2 = ord(cuvant[1]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 4032 

    tmp1 = ord(cuvant[34]) 
    assert ((tmp1 >> 1) & 182) == 54 

    tmp1 = ord(cuvant[15]) 
    tmp2 = ord(cuvant[8]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 5488 

    tmp1 = ord(cuvant[38]) 
    assert ((tmp1 >> 4) & 20) == 0 

    tmp1 = ord(cuvant[30]) 
    tmp2 = ord(cuvant[42]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 23760 

    tmp1 = ord(cuvant[6]) 
    assert ((tmp1 >> 6) & 80) == 0 

    tmp1 = ord(cuvant[43]) 
    assert ((tmp1 >> 6) & 139) == 0 

    tmp1 = ord(cuvant[28]) 
    assert ((tmp1 >> 5) & 1) == 1 

    tmp1 = ord(cuvant[6]) 
    tmp2 = ord(cuvant[14]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 12992 

    tmp1 = ord(cuvant[22]) 
    tmp2 = ord(cuvant[48]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 4896 

    tmp1 = ord(cuvant[26]) 
    assert ((tmp1 >> 2) & 237) == 13 

    tmp1 = ord(cuvant[33]) 
    tmp2 = ord(cuvant[5]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1392 

    tmp1 = ord(cuvant[15]) 
    assert ((tmp1 >> 7) & 37) == 0 

    tmp1 = ord(cuvant[14]) 
    assert ((tmp1 >> 2) & 95) == 29 

    tmp1 = ord(cuvant[28]) 
    tmp2 = ord(cuvant[30]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2616 

    tmp1 = ord(cuvant[12]) 
    assert ((tmp1 >> 6) & 179) == 1 

    tmp1 = ord(cuvant[32]) 
    assert ((tmp1 >> 3) & 141) == 12 

    tmp1 = ord(cuvant[28]) 
    assert ((tmp1 >> 3) & 200) == 0 

    tmp1 = ord(cuvant[3]) 
    tmp2 = ord(cuvant[34]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 6976 

    tmp1 = ord(cuvant[9]) 
    assert ((tmp1 >> 7) & 142) == 0 

    tmp1 = ord(cuvant[40]) 
    tmp2 = ord(cuvant[44]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 5130 

    tmp1 = ord(cuvant[18]) 
    tmp2 = ord(cuvant[30]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 10246 

    tmp1 = ord(cuvant[2]) 
    tmp2 = ord(cuvant[47]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 12920 

    tmp1 = ord(cuvant[18]) 
    assert ((tmp1 >> 1) & 185) == 41 

    tmp1 = ord(cuvant[27]) 
    tmp2 = ord(cuvant[37]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 5940 

    tmp1 = ord(cuvant[46]) 
    assert ((tmp1 >> 7) & 146) == 0 

    tmp1 = ord(cuvant[30]) 
    assert ((tmp1 >> 2) & 67) == 3 

    tmp1 = ord(cuvant[24]) 
    assert ((tmp1 >> 5) & 52) == 0 

    tmp1 = ord(cuvant[26]) 
    tmp2 = ord(cuvant[16]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2736 

    tmp1 = ord(cuvant[11]) 
    tmp2 = ord(cuvant[49]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 1248 

    tmp1 = ord(cuvant[5]) 
    assert ((tmp1 >> 3) & 65) == 0 

    tmp1 = ord(cuvant[15]) 
    assert ((tmp1 >> 2) & 46) == 12 

    tmp1 = ord(cuvant[6]) 
    tmp2 = ord(cuvant[9]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 12208 

    tmp1 = ord(cuvant[17]) 
    assert ((tmp1 >> 6) & 105) == 0 

    tmp1 = ord(cuvant[20]) 
    tmp2 = ord(cuvant[25]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2688 

    tmp1 = ord(cuvant[48]) 
    assert ((tmp1 >> 3) & 15) == 6 

    tmp1 = ord(cuvant[2]) 
    assert ((tmp1 >> 6) & 102) == 0 

    tmp1 = ord(cuvant[48]) 
    assert ((tmp1 >> 1) & 200) == 8 

    tmp1 = ord(cuvant[36]) 
    tmp2 = ord(cuvant[0]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 7592 

    tmp1 = ord(cuvant[5]) 
    assert ((tmp1 >> 6) & 245) == 1 

    tmp1 = ord(cuvant[34]) 
    assert ((tmp1 >> 6) & 127) == 1 

    tmp1 = ord(cuvant[11]) 
    tmp2 = ord(cuvant[22]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 1224 

    tmp1 = ord(cuvant[21]) 
    assert ((tmp1 >> 1) & 61) == 45 

    tmp1 = ord(cuvant[46]) 
    tmp2 = ord(cuvant[9]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 2616 

    tmp1 = ord(cuvant[21]) 
    tmp2 = ord(cuvant[7]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 19552 

    tmp1 = ord(cuvant[37]) 
    assert ((tmp1 >> 7) & 71) == 0 

    tmp1 = ord(cuvant[38]) 
    assert ((tmp1 >> 3) & 149) == 4 

    tmp1 = ord(cuvant[50]) 
    tmp2 = ord(cuvant[30]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 27032 

    tmp1 = ord(cuvant[23]) 
    assert ((tmp1 >> 6) & 132) == 0 

    tmp1 = ord(cuvant[30]) 
    assert ((tmp1 >> 4) & 162) == 2 

    tmp1 = ord(cuvant[28]) 
    assert ((tmp1 >> 7) & 217) == 0 

    tmp1 = ord(cuvant[24]) 
    tmp2 = ord(cuvant[3]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 5896 

    tmp1 = ord(cuvant[3]) 
    tmp2 = ord(cuvant[1]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 22176 

    tmp1 = ord(cuvant[27]) 
    tmp2 = ord(cuvant[17]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 5096 

    tmp1 = ord(cuvant[3]) 
    assert ((tmp1 >> 3) & 199) == 0 

    tmp1 = ord(cuvant[15]) 
    tmp2 = ord(cuvant[28]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2912 

    tmp1 = ord(cuvant[11]) 
    assert ((tmp1 >> 3) & 140) == 4 

    tmp1 = ord(cuvant[33]) 
    tmp2 = ord(cuvant[40]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 21120 

    tmp1 = ord(cuvant[24]) 
    tmp2 = ord(cuvant[12]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 10152 

    tmp1 = ord(cuvant[32]) 
    tmp2 = ord(cuvant[33]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 2744 

    tmp1 = ord(cuvant[15]) 
    assert ((tmp1 >> 7) & 127) == 0 

    tmp1 = ord(cuvant[46]) 
    tmp2 = ord(cuvant[17]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 1176 

    tmp1 = ord(cuvant[32]) 
    tmp2 = ord(cuvant[3]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 30552 

    tmp1 = ord(cuvant[7]) 
    assert ((tmp1 >> 2) & 227) == 1 

    tmp1 = ord(cuvant[1]) 
    assert ((tmp1 >> 6) & 244) == 0 

    tmp1 = ord(cuvant[42]) 
    tmp2 = ord(cuvant[0]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 1752 

    tmp1 = ord(cuvant[12]) 
    tmp2 = ord(cuvant[45]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 21600 

    tmp1 = ord(cuvant[16]) 
    tmp2 = ord(cuvant[43]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 10976 

    tmp1 = ord(cuvant[17]) 
    tmp2 = ord(cuvant[38]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 2496 

    tmp1 = ord(cuvant[11]) 
    assert ((tmp1 >> 4) & 171) == 3 

    tmp1 = ord(cuvant[2]) 
    assert ((tmp1 >> 2) & 43) == 1 

    tmp1 = ord(cuvant[39]) 
    tmp2 = ord(cuvant[46]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2856 

    tmp1 = ord(cuvant[33]) 
    tmp2 = ord(cuvant[0]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 7008 

    tmp1 = ord(cuvant[32]) 
    assert ((tmp1 >> 2) & 72) == 8 

    tmp1 = ord(cuvant[33]) 
    assert ((tmp1 >> 2) & 30) == 12 

    tmp1 = ord(cuvant[18]) 
    assert ((tmp1 >> 5) & 206) == 2 

    tmp1 = ord(cuvant[1]) 
    tmp2 = ord(cuvant[44]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 7600 

    tmp1 = ord(cuvant[6]) 
    assert ((tmp1 >> 4) & 56) == 0 

    tmp1 = ord(cuvant[39]) 
    assert ((tmp1 >> 1) & 197) == 1 

    tmp1 = ord(cuvant[15]) 
    assert ((tmp1 >> 5) & 56) == 0 

    tmp1 = ord(cuvant[14]) 
    tmp2 = ord(cuvant[17]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 2842 

    tmp1 = ord(cuvant[3]) 
    tmp2 = ord(cuvant[25]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 14336 

    tmp1 = ord(cuvant[48]) 
    tmp2 = ord(cuvant[0]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 7300 

    tmp1 = ord(cuvant[19]) 
    assert ((tmp1 >> 2) & 237) == 9 

    tmp1 = ord(cuvant[12]) 
    assert ((tmp1 >> 6) & 36) == 0 

    tmp1 = ord(cuvant[12]) 
    assert ((tmp1 >> 7) & 156) == 0 

    tmp1 = ord(cuvant[38]) 
    tmp2 = ord(cuvant[25]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 23296 

    tmp1 = ord(cuvant[41]) 
    assert ((tmp1 >> 3) & 162) == 0 

    tmp1 = ord(cuvant[20]) 
    assert ((tmp1 >> 5) & 19) == 1 

    tmp1 = ord(cuvant[36]) 
    tmp2 = ord(cuvant[22]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 2448 

    tmp1 = ord(cuvant[10]) 
    assert ((tmp1 >> 7) & 31) == 0 

    tmp1 = ord(cuvant[3]) 
    assert ((tmp1 >> 5) & 86) == 2 

    tmp1 = ord(cuvant[29]) 
    tmp2 = ord(cuvant[8]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 4606 

    tmp1 = ord(cuvant[47]) 
    tmp2 = ord(cuvant[6]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 20976 

    tmp1 = ord(cuvant[10]) 
    tmp2 = ord(cuvant[23]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 9568 

    tmp1 = ord(cuvant[17]) 
    assert ((tmp1 >> 3) & 154) == 2 

    tmp1 = ord(cuvant[4]) 
    tmp2 = ord(cuvant[37]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 3300 

    tmp1 = ord(cuvant[44]) 
    tmp2 = ord(cuvant[3]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 12328 

    tmp1 = ord(cuvant[10]) 
    assert ((tmp1 >> 3) & 239) == 11 

    tmp1 = ord(cuvant[15]) 
    assert ((tmp1 >> 2) & 16) == 16 

    tmp1 = ord(cuvant[0]) 
    assert ((tmp1 >> 3) & 219) == 9 

    tmp1 = ord(cuvant[10]) 
    tmp2 = ord(cuvant[46]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 2346 

    tmp1 = ord(cuvant[39]) 
    tmp2 = ord(cuvant[35]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 5320 

    tmp1 = ord(cuvant[21]) 
    assert ((tmp1 >> 6) & 115) == 1 

    tmp1 = ord(cuvant[24]) 
    assert ((tmp1 >> 4) & 16) == 0 

    tmp1 = ord(cuvant[41]) 
    assert ((tmp1 >> 3) & 239) == 12 

    tmp1 = ord(cuvant[8]) 
    assert ((tmp1 >> 6) & 56) == 0 

    tmp1 = ord(cuvant[30]) 
    assert ((tmp1 >> 4) & 47) == 6 

    tmp1 = ord(cuvant[20]) 
    assert ((tmp1 >> 4) & 107) == 3 

    tmp1 = ord(cuvant[27]) 
    tmp2 = ord(cuvant[28]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 5720 

    tmp1 = ord(cuvant[43]) 
    assert ((tmp1 >> 4) & 182) == 2 

    tmp1 = ord(cuvant[40]) 
    assert ((tmp1 >> 5) & 173) == 1 

    tmp1 = ord(cuvant[7]) 
    tmp2 = ord(cuvant[14]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1392 

    tmp1 = ord(cuvant[6]) 
    assert ((tmp1 >> 4) & 110) == 6 

    tmp1 = ord(cuvant[3]) 
    tmp2 = ord(cuvant[1]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2688 

    tmp1 = ord(cuvant[18]) 
    assert ((tmp1 >> 7) & 34) == 0 

    tmp1 = ord(cuvant[46]) 
    tmp2 = ord(cuvant[34]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 10464 

    tmp1 = ord(cuvant[41]) 
    tmp2 = ord(cuvant[36]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1248 

    tmp1 = ord(cuvant[39]) 
    assert ((tmp1 >> 4) & 16) == 0 

    tmp1 = ord(cuvant[11]) 
    assert ((tmp1 >> 3) & 135) == 6 

    tmp1 = ord(cuvant[32]) 
    tmp2 = ord(cuvant[33]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 5488 

    tmp1 = ord(cuvant[2]) 
    assert ((tmp1 >> 4) & 76) == 4 

    tmp1 = ord(cuvant[7]) 
    assert ((tmp1 >> 5) & 245) == 1 

    tmp1 = ord(cuvant[42]) 
    assert ((tmp1 >> 7) & 57) == 0 

    tmp1 = ord(cuvant[40]) 
    assert ((tmp1 >> 4) & 160) == 0 

    tmp1 = ord(cuvant[9]) 
    assert ((tmp1 >> 5) & 87) == 3 

    tmp1 = ord(cuvant[8]) 
    assert ((tmp1 >> 5) & 31) == 1 

    tmp1 = ord(cuvant[42]) 
    assert ((tmp1 >> 6) & 80) == 0 

    tmp1 = ord(cuvant[34]) 
    tmp2 = ord(cuvant[18]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 20520 

    tmp1 = ord(cuvant[32]) 
    assert ((tmp1 >> 5) & 104) == 0 

    tmp1 = ord(cuvant[26]) 
    assert ((tmp1 >> 5) & 161) == 1 

    tmp1 = ord(cuvant[50]) 
    assert ((tmp1 >> 6) & 17) == 1 

    tmp1 = ord(cuvant[8]) 
    assert ((tmp1 >> 4) & 98) == 2 

    tmp1 = ord(cuvant[26]) 
    assert ((tmp1 >> 7) & 83) == 0 

    tmp1 = ord(cuvant[12]) 
    assert ((tmp1 >> 7) & 208) == 0 

    tmp1 = ord(cuvant[45]) 
    assert ((tmp1 >> 5) & 83) == 3 

    tmp1 = ord(cuvant[1]) 
    tmp2 = ord(cuvant[15]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 9828 

    tmp1 = ord(cuvant[21]) 
    assert ((tmp1 >> 3) & 63) == 11 

    tmp1 = ord(cuvant[2]) 
    tmp2 = ord(cuvant[21]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 12920 

    tmp1 = ord(cuvant[44]) 
    assert ((tmp1 >> 4) & 101) == 5 

    tmp1 = ord(cuvant[25]) 
    tmp2 = ord(cuvant[31]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 13104 

    tmp1 = ord(cuvant[34]) 
    tmp2 = ord(cuvant[33]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 5292 

    tmp1 = ord(cuvant[49]) 
    assert ((tmp1 >> 2) & 71) == 5 

    tmp1 = ord(cuvant[29]) 
    tmp2 = ord(cuvant[50]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 23500 

    tmp1 = ord(cuvant[48]) 
    tmp2 = ord(cuvant[35]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2280 

    tmp1 = ord(cuvant[6]) 
    tmp2 = ord(cuvant[27]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 12540 

    tmp1 = ord(cuvant[0]) 
    tmp2 = ord(cuvant[7]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 3744 

    tmp1 = ord(cuvant[12]) 
    tmp2 = ord(cuvant[32]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 5928 

    tmp1 = ord(cuvant[6]) 
    tmp2 = ord(cuvant[19]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 2800 

    tmp1 = ord(cuvant[7]) 
    assert ((tmp1 >> 5) & 223) == 1 

    tmp1 = ord(cuvant[37]) 
    assert ((tmp1 >> 4) & 149) == 1 

    tmp1 = ord(cuvant[43]) 
    tmp2 = ord(cuvant[40]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 10560 

    tmp1 = ord(cuvant[33]) 
    assert ((tmp1 >> 2) & 37) == 4 

    tmp1 = ord(cuvant[50]) 
    assert ((tmp1 >> 7) & 166) == 0 

    tmp1 = ord(cuvant[24]) 
    assert ((tmp1 >> 2) & 89) == 17 

    tmp1 = ord(cuvant[8]) 
    tmp2 = ord(cuvant[48]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 9792 

    tmp1 = ord(cuvant[44]) 
    assert ((tmp1 >> 2) & 26) == 18 

    tmp1 = ord(cuvant[27]) 
    assert ((tmp1 >> 2) & 213) == 17 

    tmp1 = ord(cuvant[5]) 
    tmp2 = ord(cuvant[31]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 6786 

    tmp1 = ord(cuvant[25]) 
    tmp2 = ord(cuvant[1]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 2352 

    tmp1 = ord(cuvant[27]) 
    tmp2 = ord(cuvant[30]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 23544 

    tmp1 = ord(cuvant[3]) 
    assert ((tmp1 >> 4) & 205) == 4 

    tmp1 = ord(cuvant[12]) 
    assert ((tmp1 >> 1) & 141) == 4 

    tmp1 = ord(cuvant[31]) 
    assert ((tmp1 >> 3) & 255) == 14 

    tmp1 = ord(cuvant[39]) 
    tmp2 = ord(cuvant[3]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 3752 

    tmp1 = ord(cuvant[19]) 
    tmp2 = ord(cuvant[23]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1248 

    tmp1 = ord(cuvant[1]) 
    tmp2 = ord(cuvant[47]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 7980 

    tmp1 = ord(cuvant[34]) 
    tmp2 = ord(cuvant[38]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 5616 

    tmp1 = ord(cuvant[23]) 
    assert ((tmp1 >> 1) & 199) == 2 

    tmp1 = ord(cuvant[17]) 
    assert ((tmp1 >> 3) & 86) == 6 

    tmp1 = ord(cuvant[28]) 
    assert ((tmp1 >> 6) & 135) == 0 

    tmp1 = ord(cuvant[5]) 
    tmp2 = ord(cuvant[22]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 11832 

    tmp1 = ord(cuvant[6]) 
    assert ((tmp1 >> 6) & 186) == 0 

    tmp1 = ord(cuvant[28]) 
    assert ((tmp1 >> 6) & 90) == 0 

    tmp1 = ord(cuvant[15]) 
    assert ((tmp1 >> 7) & 23) == 0 

    tmp1 = ord(cuvant[31]) 
    assert ((tmp1 >> 5) & 234) == 2 

    tmp1 = ord(cuvant[27]) 
    assert ((tmp1 >> 3) & 16) == 0 

    tmp1 = ord(cuvant[11]) 
    tmp2 = ord(cuvant[38]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 2496 

    tmp1 = ord(cuvant[20]) 
    assert ((tmp1 >> 7) & 44) == 0 

    tmp1 = ord(cuvant[25]) 
    assert ((tmp1 >> 2) & 180) == 20 

    tmp1 = ord(cuvant[26]) 
    tmp2 = ord(cuvant[5]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1392 

    tmp1 = ord(cuvant[22]) 
    tmp2 = ord(cuvant[39]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 5472 

    tmp1 = ord(cuvant[37]) 
    assert ((tmp1 >> 5) & 71) == 1 

    tmp1 = ord(cuvant[23]) 
    assert ((tmp1 >> 3) & 75) == 2 

    tmp1 = ord(cuvant[13]) 
    tmp2 = ord(cuvant[22]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 10608 

    tmp1 = ord(cuvant[34]) 
    tmp2 = ord(cuvant[10]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 5130 

    tmp1 = ord(cuvant[17]) 
    assert ((tmp1 >> 1) & 163) == 0 

    tmp1 = ord(cuvant[5]) 
    assert ((tmp1 >> 2) & 158) == 28 

    tmp1 = ord(cuvant[2]) 
    assert ((tmp1 >> 6) & 163) == 1 

    tmp1 = ord(cuvant[9]) 
    tmp2 = ord(cuvant[29]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 20520 

    tmp1 = ord(cuvant[21]) 
    tmp2 = ord(cuvant[23]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 9568 

    tmp1 = ord(cuvant[41]) 
    assert ((tmp1 >> 3) & 158) == 12 

    tmp1 = ord(cuvant[43]) 
    assert ((tmp1 >> 2) & 161) == 0 

    tmp1 = ord(cuvant[22]) 
    assert ((tmp1 >> 5) & 80) == 0 

    tmp1 = ord(cuvant[48]) 
    assert ((tmp1 >> 6) & 109) == 0 

    tmp1 = ord(cuvant[48]) 
    tmp2 = ord(cuvant[32]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 2736 

    tmp1 = ord(cuvant[33]) 
    assert ((tmp1 >> 3) & 217) == 0 

    tmp1 = ord(cuvant[49]) 
    tmp2 = ord(cuvant[7]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 10816 

    tmp1 = ord(cuvant[37]) 
    assert ((tmp1 >> 2) & 172) == 12 

    tmp1 = ord(cuvant[11]) 
    assert ((tmp1 >> 3) & 173) == 4 

    tmp1 = ord(cuvant[33]) 
    tmp2 = ord(cuvant[46]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 1224 

    tmp1 = ord(cuvant[42]) 
    tmp2 = ord(cuvant[29]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2280 

    tmp1 = ord(cuvant[45]) 
    assert ((tmp1 >> 4) & 178) == 2 

    tmp1 = ord(cuvant[23]) 
    assert ((tmp1 >> 7) & 212) == 0 

    tmp1 = ord(cuvant[2]) 
    tmp2 = ord(cuvant[42]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 880 

    tmp1 = ord(cuvant[13]) 
    tmp2 = ord(cuvant[31]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1404 

    tmp1 = ord(cuvant[6]) 
    assert ((tmp1 >> 2) & 213) == 20 

    tmp1 = ord(cuvant[21]) 
    tmp2 = ord(cuvant[1]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 3696 

    tmp1 = ord(cuvant[12]) 
    tmp2 = ord(cuvant[39]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 6156 

    tmp1 = ord(cuvant[2]) 
    tmp2 = ord(cuvant[48]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 3264 

    tmp1 = ord(cuvant[20]) 
    tmp2 = ord(cuvant[6]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 5700 

    tmp1 = ord(cuvant[47]) 
    tmp2 = ord(cuvant[9]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 10246 

    tmp1 = ord(cuvant[24]) 
    assert ((tmp1 >> 4) & 229) == 5 

    tmp1 = ord(cuvant[12]) 
    tmp2 = ord(cuvant[37]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 5940 

    tmp1 = ord(cuvant[33]) 
    tmp2 = ord(cuvant[30]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1308 

    tmp1 = ord(cuvant[2]) 
    assert ((tmp1 >> 6) & 4) == 0 

    tmp1 = ord(cuvant[20]) 
    assert ((tmp1 >> 3) & 17) == 0 

    tmp1 = ord(cuvant[16]) 
    tmp2 = ord(cuvant[21]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 43320 

    tmp1 = ord(cuvant[5]) 
    tmp2 = ord(cuvant[8]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 22736 

    tmp1 = ord(cuvant[15]) 
    tmp2 = ord(cuvant[12]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 25056 

    tmp1 = ord(cuvant[23]) 
    tmp2 = ord(cuvant[32]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 5928 

    tmp1 = ord(cuvant[32]) 
    assert ((tmp1 >> 5) & 224) == 0 

    tmp1 = ord(cuvant[25]) 
    assert ((tmp1 >> 7) & 18) == 0 

    tmp1 = ord(cuvant[20]) 
    assert ((tmp1 >> 5) & 37) == 1 

    tmp1 = ord(cuvant[40]) 
    assert ((tmp1 >> 4) & 203) == 2 

    tmp1 = ord(cuvant[14]) 
    tmp2 = ord(cuvant[35]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 11020 

    tmp1 = ord(cuvant[13]) 
    tmp2 = ord(cuvant[8]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 10192 

    tmp1 = ord(cuvant[37]) 
    assert ((tmp1 >> 1) & 86) == 18 

    tmp1 = ord(cuvant[3]) 
    assert ((tmp1 >> 4) & 210) == 0 

    tmp1 = ord(cuvant[32]) 
    assert ((tmp1 >> 2) & 188) == 28 

    tmp1 = ord(cuvant[7]) 
    assert ((tmp1 >> 1) & 177) == 16 

    tmp1 = ord(cuvant[0]) 
    tmp2 = ord(cuvant[46]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 1836 

    tmp1 = ord(cuvant[43]) 
    tmp2 = ord(cuvant[15]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2808 

    tmp1 = ord(cuvant[34]) 
    assert ((tmp1 >> 4) & 10) == 2 

    tmp1 = ord(cuvant[33]) 
    assert ((tmp1 >> 6) & 21) == 0 

    tmp1 = ord(cuvant[31]) 
    assert ((tmp1 >> 5) & 195) == 3 

    tmp1 = ord(cuvant[39]) 
    tmp2 = ord(cuvant[42]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 6270 

    tmp1 = ord(cuvant[45]) 
    assert ((tmp1 >> 4) & 22) == 6 

    tmp1 = ord(cuvant[50]) 
    assert ((tmp1 >> 3) & 40) == 8 

    tmp1 = ord(cuvant[26]) 
    assert ((tmp1 >> 7) & 247) == 0 

    tmp1 = ord(cuvant[32]) 
    assert ((tmp1 >> 3) & 98) == 2 

    tmp1 = ord(cuvant[49]) 
    tmp2 = ord(cuvant[33]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 10192 

    tmp1 = ord(cuvant[25]) 
    assert ((tmp1 >> 2) & 52) == 20 

    tmp1 = ord(cuvant[2]) 
    assert ((tmp1 >> 5) & 222) == 2 

    tmp1 = ord(cuvant[36]) 
    assert ((tmp1 >> 2) & 36) == 4 

    tmp1 = ord(cuvant[41]) 
    assert ((tmp1 >> 7) & 139) == 0 

    tmp1 = ord(cuvant[0]) 
    tmp2 = ord(cuvant[35]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 13680 

    tmp1 = ord(cuvant[31]) 
    assert ((tmp1 >> 6) & 35) == 1 

    tmp1 = ord(cuvant[44]) 
    assert ((tmp1 >> 5) & 42) == 2 

    tmp1 = ord(cuvant[26]) 
    assert ((tmp1 >> 1) & 149) == 16 

    tmp1 = ord(cuvant[28]) 
    assert ((tmp1 >> 5) & 143) == 1 

    tmp1 = ord(cuvant[47]) 
    assert ((tmp1 >> 4) & 111) == 5 

    tmp1 = ord(cuvant[35]) 
    assert ((tmp1 >> 1) & 56) == 40 

    tmp1 = ord(cuvant[41]) 
    tmp2 = ord(cuvant[50]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 12000 

    tmp1 = ord(cuvant[31]) 
    tmp2 = ord(cuvant[6]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 12768 

    tmp1 = ord(cuvant[50]) 
    tmp2 = ord(cuvant[31]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 29016 

    tmp1 = ord(cuvant[40]) 
    assert ((tmp1 >> 3) & 99) == 1 

    tmp1 = ord(cuvant[11]) 
    tmp2 = ord(cuvant[40]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 11440 

    tmp1 = ord(cuvant[30]) 
    assert ((tmp1 >> 7) & 117) == 0 

    tmp1 = ord(cuvant[48]) 
    assert ((tmp1 >> 2) & 26) == 8 

    tmp1 = ord(cuvant[35]) 
    tmp2 = ord(cuvant[47]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 2090 

    tmp1 = ord(cuvant[34]) 
    assert ((tmp1 >> 2) & 72) == 8 

    tmp1 = ord(cuvant[22]) 
    assert ((tmp1 >> 6) & 35) == 0 

    tmp1 = ord(cuvant[27]) 
    tmp2 = ord(cuvant[0]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 3796 

    tmp1 = ord(cuvant[2]) 
    tmp2 = ord(cuvant[49]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 7072 

    tmp1 = ord(cuvant[13]) 
    assert ((tmp1 >> 2) & 172) == 12 

    tmp1 = ord(cuvant[13]) 
    assert ((tmp1 >> 1) & 142) == 10 

    tmp1 = ord(cuvant[9]) 
    assert ((tmp1 >> 3) & 106) == 8 

    tmp1 = ord(cuvant[11]) 
    tmp2 = ord(cuvant[23]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 2704 

    tmp1 = ord(cuvant[31]) 
    assert ((tmp1 >> 5) & 136) == 0 

    tmp1 = ord(cuvant[48]) 
    tmp2 = ord(cuvant[22]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 612 

    tmp1 = ord(cuvant[19]) 
    assert ((tmp1 >> 5) & 198) == 2 

    tmp1 = ord(cuvant[32]) 
    assert ((tmp1 >> 2) & 155) == 24 

    tmp1 = ord(cuvant[1]) 
    tmp2 = ord(cuvant[34]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 8720 

    tmp1 = ord(cuvant[45]) 
    tmp2 = ord(cuvant[2]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 13800 

    tmp1 = ord(cuvant[34]) 
    assert ((tmp1 >> 7) & 135) == 0 

    tmp1 = ord(cuvant[41]) 
    assert ((tmp1 >> 3) & 129) == 0 

    tmp1 = ord(cuvant[9]) 
    tmp2 = ord(cuvant[23]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 5408 

    tmp1 = ord(cuvant[19]) 
    assert ((tmp1 >> 4) & 163) == 2 

    tmp1 = ord(cuvant[19]) 
    assert ((tmp1 >> 2) & 31) == 25 

    tmp1 = ord(cuvant[23]) 
    assert ((tmp1 >> 2) & 4) == 4 

    tmp1 = ord(cuvant[12]) 
    assert ((tmp1 >> 1) & 195) == 2 

    tmp1 = ord(cuvant[46]) 
    assert ((tmp1 >> 1) & 240) == 16 

    tmp1 = ord(cuvant[29]) 
    tmp2 = ord(cuvant[13]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 4784 

    tmp1 = ord(cuvant[11]) 
    assert ((tmp1 >> 3) & 247) == 6 

    tmp1 = ord(cuvant[25]) 
    tmp2 = ord(cuvant[12]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 12096 

    tmp1 = ord(cuvant[3]) 
    tmp2 = ord(cuvant[46]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 1632 

    tmp1 = ord(cuvant[25]) 
    tmp2 = ord(cuvant[45]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 11200 

    tmp1 = ord(cuvant[9]) 
    tmp2 = ord(cuvant[23]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2704 

    tmp1 = ord(cuvant[46]) 
    tmp2 = ord(cuvant[4]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 2952 

    tmp1 = ord(cuvant[21]) 
    tmp2 = ord(cuvant[15]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 2574 

    tmp1 = ord(cuvant[12]) 
    tmp2 = ord(cuvant[42]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 11880 

    tmp1 = ord(cuvant[10]) 
    assert ((tmp1 >> 6) & 206) == 0 

    tmp1 = ord(cuvant[26]) 
    tmp2 = ord(cuvant[1]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 4368 

    tmp1 = ord(cuvant[27]) 
    assert ((tmp1 >> 2) & 240) == 16 

    tmp1 = ord(cuvant[44]) 
    tmp2 = ord(cuvant[24]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 4180 

    tmp1 = ord(cuvant[10]) 
    assert ((tmp1 >> 7) & 97) == 0 

    tmp1 = ord(cuvant[21]) 
    tmp2 = ord(cuvant[8]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 9016 

    tmp1 = ord(cuvant[11]) 
    assert ((tmp1 >> 5) & 72) == 0 

    tmp1 = ord(cuvant[13]) 
    tmp2 = ord(cuvant[47]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 4940 

    tmp1 = ord(cuvant[12]) 
    tmp2 = ord(cuvant[4]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 53136 

    tmp1 = ord(cuvant[32]) 
    assert ((tmp1 >> 6) & 75) == 1 

    tmp1 = ord(cuvant[1]) 
    tmp2 = ord(cuvant[16]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 9576 

    tmp1 = ord(cuvant[23]) 
    assert ((tmp1 >> 2) & 81) == 1 

    tmp1 = ord(cuvant[29]) 
    assert ((tmp1 >> 3) & 25) == 9 

    tmp1 = ord(cuvant[45]) 
    tmp2 = ord(cuvant[2]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 3450 

    tmp1 = ord(cuvant[47]) 
    assert ((tmp1 >> 4) & 246) == 4 

    tmp1 = ord(cuvant[46]) 
    assert ((tmp1 >> 2) & 100) == 4 

    tmp1 = ord(cuvant[3]) 
    assert ((tmp1 >> 1) & 103) == 33 

    tmp1 = ord(cuvant[34]) 
    assert ((tmp1 >> 3) & 34) == 0 

    tmp1 = ord(cuvant[28]) 
    tmp2 = ord(cuvant[0]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 3796 

    tmp1 = ord(cuvant[41]) 
    assert ((tmp1 >> 1) & 158) == 16 

    tmp1 = ord(cuvant[10]) 
    tmp2 = ord(cuvant[7]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 2288 

    tmp1 = ord(cuvant[42]) 
    assert ((tmp1 >> 5) & 22) == 0 

    tmp1 = ord(cuvant[12]) 
    assert ((tmp1 >> 3) & 188) == 12 

    tmp1 = ord(cuvant[12]) 
    assert ((tmp1 >> 7) & 230) == 0 

    tmp1 = ord(cuvant[11]) 
    assert ((tmp1 >> 7) & 172) == 0 

    tmp1 = ord(cuvant[31]) 
    assert ((tmp1 >> 7) & 47) == 0 

    tmp1 = ord(cuvant[48]) 
    assert ((tmp1 >> 7) & 85) == 0 

    tmp1 = ord(cuvant[20]) 
    tmp2 = ord(cuvant[21]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 19000 

    tmp1 = ord(cuvant[24]) 
    assert ((tmp1 >> 2) & 60) == 20 

    tmp1 = ord(cuvant[10]) 
    assert ((tmp1 >> 5) & 77) == 0 

    tmp1 = ord(cuvant[32]) 
    tmp2 = ord(cuvant[17]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 5488 

    tmp1 = ord(cuvant[47]) 
    assert ((tmp1 >> 5) & 241) == 0 

    tmp1 = ord(cuvant[19]) 
    assert ((tmp1 >> 4) & 209) == 0 

    tmp1 = ord(cuvant[11]) 
    tmp2 = ord(cuvant[47]) 
    assert ((tmp1 >> 3) * (tmp2 << 1)) == 1140 

    tmp1 = ord(cuvant[9]) 
    tmp2 = ord(cuvant[10]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 41040 

    tmp1 = ord(cuvant[9]) 
    tmp2 = ord(cuvant[13]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 5616 

    tmp1 = ord(cuvant[49]) 
    tmp2 = ord(cuvant[40]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 11440 

    tmp1 = ord(cuvant[3]) 
    assert ((tmp1 >> 1) & 159) == 1 

    tmp1 = ord(cuvant[13]) 
    tmp2 = ord(cuvant[34]) 
    assert ((tmp1 >> 2) * (tmp2 << 2)) == 5668 

    tmp1 = ord(cuvant[37]) 
    assert ((tmp1 >> 2) & 241) == 1 

    tmp1 = ord(cuvant[42]) 
    assert ((tmp1 >> 1) & 79) == 11 

    tmp1 = ord(cuvant[24]) 
    tmp2 = ord(cuvant[42]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 5170 

    tmp1 = ord(cuvant[46]) 
    tmp2 = ord(cuvant[14]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 2784 

    tmp1 = ord(cuvant[39]) 
    assert ((tmp1 >> 6) & 105) == 1 

    tmp1 = ord(cuvant[7]) 
    assert ((tmp1 >> 1) & 235) == 10 

    tmp1 = ord(cuvant[38]) 
    tmp2 = ord(cuvant[44]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 4560 

    tmp1 = ord(cuvant[8]) 
    assert ((tmp1 >> 2) & 104) == 8 

    tmp1 = ord(cuvant[12]) 
    assert ((tmp1 >> 5) & 124) == 0 

    tmp1 = ord(cuvant[22]) 
    assert ((tmp1 >> 1) & 158) == 24 

    tmp1 = ord(cuvant[34]) 
    tmp2 = ord(cuvant[3]) 
    assert ((tmp1 >> 3) * (tmp2 << 2)) == 3484 

    tmp1 = ord(cuvant[1]) 
    assert ((tmp1 >> 4) & 27) == 1 

    tmp1 = ord(cuvant[11]) 
    assert ((tmp1 >> 3) & 136) == 0 

    tmp1 = ord(cuvant[13]) 
    tmp2 = ord(cuvant[11]) 
    assert ((tmp1 >> 2) * (tmp2 << 1)) == 1352 

    tmp1 = ord(cuvant[49]) 
    tmp2 = ord(cuvant[31]) 
    assert ((tmp1 >> 1) * (tmp2 << 1)) == 6084 

    tmp1 = ord(cuvant[28]) 
    tmp2 = ord(cuvant[46]) 
    assert ((tmp1 >> 2) * (tmp2 << 3)) == 5304 

    tmp1 = ord(cuvant[15]) 
    assert ((tmp1 >> 3) & 180) == 4 

    tmp1 = ord(cuvant[41]) 
    assert ((tmp1 >> 5) & 242) == 2 

    tmp1 = ord(cuvant[50]) 
    assert ((tmp1 >> 5) & 52) == 0 

    tmp1 = ord(cuvant[37]) 
    tmp2 = ord(cuvant[46]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 2448 

    tmp1 = ord(cuvant[19]) 
    assert ((tmp1 >> 4) & 44) == 4 

    tmp1 = ord(cuvant[38]) 
    tmp2 = ord(cuvant[6]) 
    assert ((tmp1 >> 1) * (tmp2 << 3)) == 23712 

    tmp1 = ord(cuvant[44]) 
    tmp2 = ord(cuvant[18]) 
    assert ((tmp1 >> 1) * (tmp2 << 2)) == 17860 

    tmp1 = ord(cuvant[7]) 
    assert ((tmp1 >> 4) & 97) == 1 

    tmp1 = ord(cuvant[26]) 
    assert ((tmp1 >> 7) & 70) == 0 

    tmp1 = ord(cuvant[49]) 
    tmp2 = ord(cuvant[20]) 
    assert ((tmp1 >> 3) * (tmp2 << 3)) == 2448 

    print("[*] Felicitari! Ai castigat!")