def clear_file(filename):
    with open(filename, 'w'):
        pass


def my_sort(iterable, *, key=lambda x: x, reverse=False):
    schimb = True
    while schimb:
        schimb = False
        for i in range(len(iterable) - 1):
            if key(iterable[i]) > key(iterable[i + 1]):
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
                schimb = True

    if not reverse:
        return iterable
    else:
        return list(reversed(iterable))
