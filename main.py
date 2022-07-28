from enigma import ALPHABET, Reflector

if __name__ == '__main__':
    r = Reflector('BACD')
    i = r.reflect(ALPHABET.index('A'))
    print(ALPHABET[i])
    i = r.reflect(ALPHABET.index('B'))
    print(ALPHABET[i])
    i = r.reflect(ALPHABET.index('C'))
    print(ALPHABET[i])
    i = r.reflect(ALPHABET.index('D'))
    print(ALPHABET[i])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
