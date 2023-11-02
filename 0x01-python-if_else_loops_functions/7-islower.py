def islower(c):
    ascii = ord(c)
    for i in range(97, 123):
        if ascii == i:
            return True
        else:
            return False
