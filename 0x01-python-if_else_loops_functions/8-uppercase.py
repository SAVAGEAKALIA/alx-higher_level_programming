def uppercase(str):
    ascii = ""

    for i in (str):
        if 'a' <= i <= 'z':
            ascii += chr(ord(i) - 32)
        else:
            ascii += i

    print(ascii)
