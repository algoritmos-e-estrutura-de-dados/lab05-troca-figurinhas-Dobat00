m = [1, 1, 2, 3, 5, 7, 8, 8, 9, 15]
j = [2, 2, 2, 3, 4, 6, 10, 11, 11]


def Figurinha(m, j):
    i = 0
    if len(m) < len(j):
        for i in range(len(m)):
            for z in range(len(j)):
                if m[i] == j[z]:
                    i += 1
        quantidade = len(m) - i

    elif len(j) < len(m):
        for i in range(len(j)):
            for z in range(len(m)):
                if j[i] == m[z]:
                    i += 1
        quantidade = len(j) - i

    else:
        for i in range(len(m)):
            for z in range(len(j)):
                if m[i] == j[z]:
                    i += 1
        quantidade = len(m) - i

    return quantidade


print(Figurinha(m, j))
