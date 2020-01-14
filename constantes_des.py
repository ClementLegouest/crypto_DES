##############################################################################
#
# Clément Legouest
#
# Extraction of DES constants from a specific file
#
# Managed to be used under Python 3.8.0 64 bits
#
##############################################################################

import re


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

    swapped_key = []

    for i in range(len(des_const)):

        swapped_key.append(des_key[int(des_const[i]) % len(des_key)])

    return swapped_key