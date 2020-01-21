##############################################################################
#
# Clément Legouest
#
# Functions used to crypt and decrypt DES
#
# Managed to be used under Python 3.8.0 64 bits
#
##############################################################################

import re


# create 2D array filled with zero characters
# x lines of y
def mat_zero(y, x):

    matrice = []

    for i in range(x):
        sub_matrice = []
        for j in range(y):
            sub_matrice.append('0')
        matrice.append(sub_matrice)
    return matrice


# fit in matrice
def fit_in_matrice(string, y, x):

    matrice = mat_zero(y, x)

    i = 0

    while i < len(string):
        for j in range(x):
            for k in range(y):
                matrice[j][k] = string[i]
                i += 1
    return matrice


# concatenation de tableau
def concat(array):

    result = ""
    for i in array:
        result += str(array[i])

    return result


# Le shérif de l'espace
def xor(one, two):
    if len(one) != len(two):
        return -1

    result = []

    for i in range(len(one)):
        if (one == 0 and two == 1) or (one == 1 and two == 0):
            result.append('1')
        else:
            return result.append('0')

    return concat(result)


# build 16 keys from one binary key
# return an array of 16 strings
def build_keys(binary_key):

    swapped_key = swap_key(binary_key, "CP_1")
    shifted_keys = shift(swapped_key)

    return shifted_keys


# Takes a DES constant name then return the corresponding DES constant
# Return -1 if DES constant name does not exist
def get_const(const_name):

    project_root = "E:/Developpement/ESGI4-Cryptographie/DES_project/"
    constants_file = "ConstantesDES.txt"

    constantes_des_file = open(project_root + constants_file)

    const = ""
    start = 0
    
    for line in constantes_des_file:
        if "FIN " + const_name in line:
            break
        if start == 1:
            const += line
        if const_name in line:
            start = 1
    
    const = const.split()

    if const == ['']:
        raise Exception("Constant not found exception")
        return

    return const


# Takes a 64 binary key apply a constant then return the new key
def swap_key(des_key, const_name):

    des_const = get_const(const_name)

    swapped_key = ""

    for i in range(len(des_const)):

        swapped_key += des_key[int(des_const[i]) % len(des_key) - 1]

    return swapped_key


# cut a key in half odd length return error
def cut_half(key):
    half_keys = [key[:int(len(key) / 2)], key[int(len(key) / 2):]]
    return half_keys


# shift 1 left and swap CP_2
def shift(key):

    keychain = []
    splitted_key = cut_half(key)

    for i in range(16):
        for j in range(2):
            splitted_key[j] = splitted_key[j][:28][1:]\
                              + splitted_key[j][:28][:1]\
                              + splitted_key[j][28:][1:]\
                              + splitted_key[j][28:][:1]
        keychain.append(swap_key(splitted_key[0] + splitted_key[1], "CP_2"))
    return keychain


# Splits a string in regular sized packets then store them in an array
# The last packet is filled with zeros til it gets the desired size
def split(string, size):

    splitted_string = []

    while len(string) >= size:
        splitted_string.append(string[:size])
        string = string[size:]

    if len(string) > 0:
        splitted_string.append(string + '0' * (size - len(string)))

    return splitted_string


# Paquetage
def pack(binary_message):

    return split(binary_message, 64)


# permutation initiale
def initial_permutation(packed_message):

    for i in range(len(packed_message)):
        packed_message[i] = swap_key(packed_message[i], "PI")
        print("PI[M" + str(i) + "] = " + packed_message[i])

    g = packed_message[0][:32]
    d = packed_message[0][32:]

    d = swap_key(d, "E")

    d = fit_in_matrice(d, 4, 12)

    return packed_message


# Divide the message in two equal parts
# in case of odd length, the second part gets the extra character
def gauche_et_droite(message):

    g = message[:int(len(message) / 2)]
    d = message[int(len(message) / 2):]

    return g, d


# Rondes
def rondes(pi_messages, built_keys):

    for message in pi_messages:
        g, d = gauche_et_droite(message)

        # 16 rondes
        #  Expansion of d
        d = swap_key(d, "E")

        # XOR
        d = xor(d, built_keys[0])

        # 8 blocs
        splitted_d = split(str(d), 4)
        print(splitted_d)
