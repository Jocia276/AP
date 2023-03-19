def show_menu():
    print(" ")
    print("1. Citire lista.")
    print("2. Afisare cea mai lunga subsecventa care are toate elementele neprime.")
    print("3. Afisare cea mai lunga subsecventa care are media numerelor mai mica decat o valoare data.")
    print("4. Afisare cea mai lunga subsecventa cu proprietatea ca numarul de cifre sa fie in ordine descrescatoare.")
    print("x. Exit")


def read_list() -> list[int]:
    lst = []
    lst_str = input("Dati numerele separate prin spatiu: ")
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

#proprietatea 18

def number_of_digits(num):
    nr_cif = 0
    while num:
        nr_cif = nr_cif + 1
        num = num // 10
    return nr_cif


def digit_count_desc(lst):

    """
    Determina daca o lista are o secventa de numere ordonate descrescator in functie de numarul de cifre
    :param lst: lista de numere
    :return: True daca lista este ordonata desresctor si False in caz contrar
    """

    for i in range(len(lst) - 1):
        if number_of_digits(lst[i]) < number_of_digits(lst[i + 1]):
            return False
    return True


def test_digit_count_desc():

    assert digit_count_desc([5, 46, 2]) is False
    assert digit_count_desc([2, 54, 65741, 21]) is False
    assert digit_count_desc([12345, 1234, 123, 12, 1]) is True
    assert digit_count_desc([245, 24, 5]) is True
    assert digit_count_desc([22, 1, 656, 8953]) is False
    assert digit_count_desc([7564, 653, 35, 10, 5]) is True


def get_longest_digit_count_desc(lst: list[int]) -> list[int]:
    """
    Determina cea mai lunga secventa cu propietatea ca numarul de cifre sa fie in ordine descrescatoare
    :param lst:Lista de numere
    :return: Lista maxima determinata
    """
    lista_secvente = []

    for start in range(0, len(lst) + 1):
        for end in range(start + 1, len(lst) + 1):
            if digit_count_desc(lst[start:end]):
                lista_secvente.append(lst[start:end])
    secventa_max = []
    for secventa in lista_secvente:
        if len(secventa) > len(secventa_max):
            secventa_max = secventa

    return secventa_max


def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([765, 43, 2, 1, 56]) == [765, 43, 2, 1]
    assert get_longest_digit_count_desc([8]) == [8]
    assert get_longest_digit_count_desc([1, 2, 56, 898]) == [1, 2]
    assert get_longest_digit_count_desc([3, 12, 356]) == [3]
    assert get_longest_digit_count_desc([1, 34, 1000, 99, 3000, 1234, 456, 34, 7, 9]) == [3000, 1234, 456, 34, 7, 9]


#proprietatea 17

def get_average_of_numbers(lst):

    """

    Determina media aritmetica a numerelor din lista
    :param lst: lista de numere

    """

    suma = 0
    for num in lst:
        suma = suma + num
    avg = float(suma / len(lst))

    return avg


def test_get_average_of_numbers():

    assert get_average_of_numbers([1, 2, 3]) == 2
    assert get_average_of_numbers([13, 25, 2, 10]) == 12.5
    assert get_average_of_numbers([11, 62, 13, 4]) == 22.5
    assert get_average_of_numbers([4, 5, 6, 7, 8, 9]) == 6.5


def get_longest_average_below(lst: list[int], average: float) -> list[int]:

    """
    Determina cea mai lunga subsecventa care are media numerelor mai mica decat o valoare data.
    :param lst: lista de numere
    :param average: valoarea citita
    :return: secventa gasita
    """

    lista_secvente = []

    for start in range(len(lst)):
        for end in range(start, len(lst)):
            if get_average_of_numbers(lst[start: end + 1]) < average and len(lst[start: end + 1]) > len(lista_secvente):
                lista_secvente = lst[start: end + 1]
    return lista_secvente


def test_get_longest_average_below():

    assert get_longest_average_below([4, 5, 6], 4.9) == ([4, 5])
    assert get_longest_average_below([100, 25, 36, 4, 8, 75], 21) == ([25, 36, 4, 8])
    assert get_longest_average_below([100, 101, 102, 21, 14, 2, 103], 12) == ([14, 2])
    assert get_longest_average_below([98, 59, 62, 10, 36], 9.6) == ([])
    assert get_longest_average_below([40, 5, 31], 5.1) == ([5])

#proprietatea 7

def is_not_prime(n: int) -> bool:
    """
    Determina daca un numar dat nu e prim.
    :param n: numarul dat
    :return: True daca nu e prim si False daca e prim.
    """

    if n < 2:
        return True
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return True
    return False


def test_is_not_prime():

    assert is_not_prime(4) is True
    assert is_not_prime(2) is False
    assert is_not_prime(13) is False
    assert is_not_prime(24) is True
    assert is_not_prime(54) is True
    assert is_not_prime(3) is False


def get_all_not_primes(lst) -> bool:
    """
    Determina numerele neprime dintr-o lista.
    :param lst: lista de numere
    :return:  True pentru toate numerele din lista care sunt neprime si Flase in caz contrar
    """

    for num in lst:
        if not is_not_prime(num):
            return False
    return True


def get_longest_all_not_prime(lst: list[int]) -> list[int]:
    """
    Determina cea mai lunga subsecventa in care toate elementele sunt neprime.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    """

    lista_secvente = []

    for start in range(0, len(lst) + 1):
        for end in range(start + 1, len(lst) + 1):
            if get_all_not_primes(lst[start:end]):
                lista_secvente.append(lst[start:end])
    secventa_max = []
    for secventa in lista_secvente:
        if len(secventa) > len(secventa_max):
            secventa_max = secventa

    return secventa_max


def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([4, 5, 6, 8, 10, 9]) == ([6, 8, 10, 9])
    assert get_longest_all_not_prime([40, 13, 12, 27]) == [12, 27]
    assert get_longest_all_not_prime([3, 5, 7, 101]) == []
    assert get_longest_all_not_prime([24, 103, 23]) == [24]
    assert get_longest_all_not_prime([4, 8, 12, 16, 20, 24, 5, 62, 64, 66, 13]) == [4, 8, 12, 16, 20, 24]
    assert get_longest_all_not_prime([32, 36, 38]) == [32, 36, 38]


def main():
    lst = []

    test_get_average_of_numbers()
    test_get_longest_average_below()
    test_is_not_prime()
    test_get_longest_all_not_prime()
    test_digit_count_desc()
    test_get_longest_digit_count_desc()

    while True:
        show_menu()
        opt = input("Introduceti optiunea: ")
        if opt == "1":
            lst = read_list()
        elif opt == "2":
            longest_not_primes = get_longest_all_not_prime(lst)
            print("Cea mai lunga subsecventa care are toate numerele neprime este: ", longest_not_primes)
        elif opt == "3":
            average = float(input("Introduceti o valoare: "))
            print("Cea mai lunga subsecventa care are media numerelor mai mica decat o valoare data este: ", get_longest_average_below(lst, average))
        elif opt == "4":
            print("Cea mai lunga subsecventa cu proprietatea ca numarul de cifre sa fie in ordine descrescatoare este : ", get_longest_digit_count_desc(lst))
        elif opt == "x":
            break
        else:
            print("Optiune invalida!")


if __name__ == '__main__':
    main()

