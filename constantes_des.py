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
def get_const(name):

    project_root = "E:/Developpement/ESGI4-Cryptographie/DES_project/"
    constants_file = "ConstantesDES.txt"

    constantes_des_file = open(project_root + constants_file)

    const = ""
    start = 0
    
    for line in constantes_des_file:
        if "FIN " + name in line:
            break
        if start == 1:
            const += line
        if name in line:
            start = 1
    
    const = re.split('[\t\n]', const)

    if const == "":
        return -1

    return const
