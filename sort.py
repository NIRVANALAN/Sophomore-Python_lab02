from random import randint
l = []
for i in range(50):
    l.append(randint(1, 50))


def selectSort(l):
    size = len(l) - 1
    for i in range(size):
        k = i
        j = i + 1
        while j <= size:
            if l[k] > l[j]:
                k = j
            j += 1
        l[i], l[k] = l[k], l[i]
    # print(l)
    return l


if __name__ == '__main__':
    selectSort(l)
