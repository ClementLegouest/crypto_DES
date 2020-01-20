import constantes_des as const_des

BINARY_KEY = "0101111001011011010100100111111101010001000110101011110010010001"

built_keys = const_des.build_keys(BINARY_KEY)

print("Built keys :")
for i in range(len(built_keys)):
    print(i + 1, ":", built_keys[i])

BINARY_TEXT = "110111001011101111000100110101011110011011110111110000100011001010011101001010110110101111100011001110" \
              "1011011111"

print("rondes :", const_des.rondes(BINARY_TEXT))

print(const_des.mat_zero(3, 4))

print(const_des.fit_in_matrice("123456789012123456789012123456789012123456789012", 4, 12))
