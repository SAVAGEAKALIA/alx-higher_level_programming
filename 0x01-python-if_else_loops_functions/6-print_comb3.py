#!/usr/bin/python3
for i in range(10):
    for n in range(i + 1, 10):
        if i == 1 and n == 0:
            print(f'{i}{n+1}, ', end=" ")
        elif i == 8 and n == 9:
            print(f'{i}{n}')
            break
        else:
            print(f'{i}{n}, ', end=" ")
