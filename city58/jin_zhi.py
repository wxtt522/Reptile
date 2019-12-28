# dec = 15
#
# print(str(int(hex(dec).upper(), 16)))

import math


def hex_to_dec():
    hex = [ord(n) - 55 if n in list("ABCDEF") else ord(n) - 48 for n in input('Input a hex number: ').upper()]
    dec = [hex[-i - 1] * math.pow(16, i) for i in range(len(hex))]
    return sum(dec)

print(hex_to_dec())