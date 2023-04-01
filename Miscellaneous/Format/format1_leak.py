#!/usr/local/bin/python3
import dataclasses
import random

FLAG = "ITEC{S4_NU_A1_1NCREDER3_1N_F0RM4T}"


@dataclasses.dataclass
class Message:
    message: str

    def __str__(self):
        return self.message

    __repr__ = __str__


MESSAGES = [
    Message("Salut! Cum te numești?"),
    Message("Imi place să mă plimb prin parcul din apropiere."),
    Message("Azi este o zi frumoasă de primăvară."),
    Message("Am cumpărat niște fructe și legume proaspete de la piață.")
]

while(1):
    inputt = input(">Da-mi un cuvant\n")
    multiplier = int(input(">Da-mi un numar\n"))

    final_pattern = inputt * multiplier
    print(f"{{message}} {final_pattern}".format(message=random.choice(MESSAGES)))
