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
import utils

BINARY_KEY = "0101111001011011010100100111111101010001000110101011110010010001"

built_keys = const_des.build_keys(BINARY_KEY)

print("Built keys :")
for i in range(len(built_keys)):
    print(i + 1, ":", built_keys[i])
print('\n')

BINARY_TEXT = "110111001011101111000100110101011110011011110111110000100011001010011101001010110110101111100011001110" \
              "1011011111"

# Paquetage
message = const_des.pack(BINARY_TEXT)

print("Après paquetage")
utils.display_dict(message)
print('\n')

# Permutation initiale
for i in range(len(message)):
    message["M " + str(i + 1)] = (const_des.swap_key(message["M " + str(i + 1)], "PI"))

print("Après permutation initiale")
utils.display_dict(message)
print('\n')

# Gauche droite
for i in range(len(message)):
    message["M " + str(i + 1)] = const_des.gauche_et_droite(message["M " + str(i + 1)])

print("après gauche droite")
utils.display_dict(message)
print('\n')

# rondes
# Expansion droite
for i in range(len(message)):
    message["M " + str(i + 1)]["droite"] = const_des.swap_key(message["M " + str(i + 1)]["droite"], "E")

print("après expansion droite")
utils.display_dict(message)
print('\n')

for i in range(len(message)):
    message["M " + str(i + 1)]["droite"] = const_des.xor_string(message["M " + str(i + 1)]["droite"], built_keys[0])

print("après xor droite x K1")
utils.display_dict(message)
print('\n')

for i in range(len(message)):
    message["M " + str(i + 1)]["droite"] = const_des.split(message["M " + str(i + 1)]["droite"], 6)

print("après split M1 droite en 6")
utils.display_dict(message)
print('\n')

for i in range(len(message)):
    for j in range(len(message["M " + str(i + 1)]["droite"])):

        const = const_des.get_const("S" + str(j + 1))

        bin_pos = message["M " + str(i + 1)]["droite"]["M " + str(j + 1)]
        line = int(bin_pos[0:1] + bin_pos[5:6], 2)
        column = int(bin_pos[1:5], 2)

        message["M " + str(i + 1)]["droite"]["M " + str(j + 1)] = "{0:04b}".format(int(const[line * 16 + column]))

for i in range(len(message)):
    message["M " + str(i + 1)]["droite"] = const_des.concat(message["M " + str(i + 1)]["droite"])

print("après swap S1 à S8")
utils.display_dict(message)
print('\n')

for i in range(len(message)):
    print(message["M " + str(i + 1)]["droite"])
    message["M " + str(i + 1)]["droite"] = const_des.swap_key(message["M " + str(i + 1)]["droite"], "P")
    print(message["M " + str(i + 1)]["droite"])

print("après Permutation des rondes")
utils.display_dict(message)
print('\n')
