##############################################################################
#
# HADJI Mohamed Allam
# DINIC Damian
# LEGOUEST Clément
#
# Main program used to crypt and decrypt DES
#
# Managed to be used under Python 3.8.0 64 bits
#
##############################################################################


import constantes_des as const_des
import ConvAlphaBin as conv
import utils

binary_key_file = open("binary_key.txt", "r")
BINARY_KEY = binary_key_file.read()
built_keys = const_des.build_keys(BINARY_KEY)

text_file = open("message.txt", "r")
text = text_file.read()
BINARY_TEXT = conv.conv_bin(text)

# Paquetage
message = const_des.pack(BINARY_TEXT)

# Permutation initiale
for i in range(len(message)):
    message["M " + str(i + 1)] = (const_des.swap_key(message["M " + str(i + 1)], "PI"))

# Gauche droite
for i in range(len(message)):
    message["M " + str(i + 1)] = const_des.gauche_et_droite(message["M " + str(i + 1)])

# rondes
# Expansion droite
for a in range(16):
    for i in range(len(message)):

        # Sauvegarde droite
        ancien_droite = message["M " + str(i + 1)]["droite"]

        # Expansion droite
        message["M " + str(i + 1)]["droite"] = const_des.swap_key(message["M " + str(i + 1)]["droite"], "E")

        # xor droite x K1
        message["M " + str(i + 1)]["droite"] = const_des.xor_string(message["M " + str(i + 1)]["droite"], built_keys[a])

        # split M1 droite en 6
        message["M " + str(i + 1)]["droite"] = const_des.split(message["M " + str(i + 1)]["droite"], 6)

        # swap S1 à S8
        for j in range(len(message["M " + str(i + 1)]["droite"])):

            const = const_des.get_const("S" + str(j + 1))

            bin_pos = message["M " + str(i + 1)]["droite"]["M " + str(j + 1)]
            line = int(bin_pos[0:1] + bin_pos[5:6], 2)
            column = int(bin_pos[1:5], 2)

            message["M " + str(i + 1)]["droite"]["M " + str(j + 1)] = "{0:04b}".format(int(const[line * 16 + column]))

        message["M " + str(i + 1)]["droite"] = const_des.concat(message["M " + str(i + 1)]["droite"])

        # Permutation des rondes
        message["M " + str(i + 1)]["droite"] = const_des.swap_key(message["M " + str(i + 1)]["droite"], "PERM")

        message["M " + str(i + 1)]["droite"] = const_des.xor_string(message["M " + str(i + 1)]["droite"], message["M " + str(i + 1)]["gauche"])

        message["M " + str(i + 1)]["gauche"] = ancien_droite

for i in range(len(message)):
    message["M " + str(i + 1)] = message["M " + str(i + 1)]["gauche"] + message["M " + str(i + 1)]["droite"]

for i in range(len(message)):
    message["M " + str(i + 1)] = const_des.swap_key(message["M " + str(i + 1)], "PI_I")

crypted_message = ""
for i in range(len(message)):
    crypted_message += message["M " + str(i + 1)]

print(crypted_message)
