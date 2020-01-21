#####################################################
#		   	 	DICTIONNAIRE BINAIRE 64				#
#####################################################

ALPHABET = ""
ALPHABET += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Les 26 lettres de l'alphabet en majuscule (0-25)
ALPHABET += "abcdefghijklmnopqrstuvwxyz"  # Les 26 lettres de l'alphabet en minuscule (26-51)
ALPHABET += " "  # caractère 52 : espace
ALPHABET += "."  # caractère 53 : point
ALPHABET += ","  # caractère 54 : virgule
ALPHABET += "!"  # caractère 55 : point d'exclamation
ALPHABET += "?"  # caractère 56 : point d'intérogation
ALPHABET += "'"  # caractère 57 : apostrophe
ALPHABET += '"'  # caractère 58 : guillemet
ALPHABET += "é"  # caractère 59 : e accent aïgu
ALPHABET += "è"  # caractère 60 : e accent grave
ALPHABET += "à"  # caractère 61 : a accent aïgu
ALPHABET += "-"  # caractère 62 : tiret
ALPHABET += "\n"  # caractère 63 : saut de ligne

# Dans cet alphabet les caractères vont de 0 à 63.
# En binaire ça donne un champ de valeur de 0 à 111111(=1+2+4+8+16+32=63)
# ALPHABETBINAIRE est un tableau avec les nombres en binaire
ALPHABETBINAIRE = dict()
for i in range(0, 64):
    ALPHABETBINAIRE[i] = '0' * (6 - len(bin(i)[2:])) + bin(i)[2:]


# Renvoie la chaine de caractère txt avec uniquement les caractères de l'alphabet.
def filtre_txt(txt):
    res = ""
    for c in txt:
        if ALPHABET.find(c) != -1:
            res += c
        elif c == 'ê' or c == 'ë':
            res += 'e'
        elif c == 'â':
            res += 'a'
        elif c == 'ç':
            res += 'c'
        elif c == 'î':
            res += 'i'
        elif c == 'Ç':
            res += 'C'
        elif c == 'ù' or c == "û":
            res += 'u'
        elif c == 'ô':
            res += 'o'
        elif c == 'Ô':
            res += 'O'
        elif c == 'œ':
            res += 'oe'
        elif c == "À":
            res += 'A'
        elif c == "È" or c == "É":
            res += 'E'
    return res


# Prend en paramètre un texte et renvoie la chaine binaire associée (en suivant le dictionnaire)
def conv_bin(txt):
    bin_txt = ""
    for char in filtre_txt(txt):
        bin_idx = ALPHABET.find(char)
        if bin_idx != -1:
            bin_txt += ALPHABETBINAIRE[bin_idx]
    return bin_txt


# Fait l'inverse de conv_bin : prend une chaine binaire et renvoie les caractères
def nib_vnoc(txt):
    n = len(txt)
    res = ""
    iterator = 0
    while iterator < n or iterator % 6 != 0:
        if iterator % 6 == 0:
            paquet_binaire = ""
        try:
            c = txt[iterator]
        except:
            c = "0"
        if c == "1":
            paquet_binaire += "1"
        else:
            paquet_binaire += "0"
        iterator += 1
        if iterator % 6 == 0:
            for b in ALPHABETBINAIRE:
                if ALPHABETBINAIRE[b] == paquet_binaire:
                    res += ALPHABET[b]
                    break

    return res


# Test
txt0 = "Je teste au stérone!"
txt1 = conv_bin(txt0)
txt2 = nib_vnoc(txt1)
print("txt0 : ", txt0)
print("txt1 : ", txt1)
print("txt2 : ", txt2)
