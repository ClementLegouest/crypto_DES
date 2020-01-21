import constantes_des as const_des

BINARY_KEY = "0101111001011011010100100111111101010001000110101011110010010001"

built_keys = const_des.build_keys(BINARY_KEY)

print("Built keys :")
for i in range(len(built_keys)):
    print(i + 1, ":", built_keys[i])

BINARY_TEXT = "110111001011101111000100110101011110011011110111110000100011001010011101001010110110101111100011001110" \
              "1011011111"

# a retirer
print("BINARY_TEXT : " + BINARY_TEXT)
# fin a retirer

packed_message = const_des.split(BINARY_TEXT, 64)

# a retirer
print("message après paquetage")
for i in range(len(packed_message)):
    print(str(i) + " : " + packed_message[i])
# fin a retirer

permuted_message = const_des.initial_permutation(packed_message)

# a retirer
print("message après permutation initiale")
for i in range(len(permuted_message)):
    print(str(i) + " : " + permuted_message[i])
# fin a retirer

const_des.rondes(permuted_message, built_keys)
