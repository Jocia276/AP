def main():
    while True:
        print("1. Ani bisecti.")
        print("2. Patrate perfecte.")
        print("3. Transforma temperatura.")
        print("x. Iesire din program - exit.")
        optiune = input("Alege optiunea: ")

        if optiune == "1":
            start = int(input("Dati primul an: "))
            end = int(input("Dati ultimul an: "))
            leap_year = get_leap_years(start, end)
            if leap_year == []:
                print("Pentru a se putea rula programul, primul an introdus trebuie sa fie mai mic decat al doilea!")
            else:
                print("Anii bisecti intre " + str(start) + " si " + str(end) + " sunt:", leap_year)

        elif optiune == "2":
            start = int(input("Introduceti primul numar: "))
            end = int(input("Introduceti al doilea numar: "))

            perfect_squares = get_perfect_squares(start, end)

            if perfect_squares == []:
                print("Nu exista patrate perfecte intre numerele date")
            else:
                print("Patratele perfecte sunt:",perfect_squares)

        elif optiune == "3":
            temp = float(input("Introduceti temperatura pe care doriti sa o transformati: "))
            From = str(input("Introduceti scara initiala: "))
            to = str(input("Introducti scara in care doriti sa transformati temperatura: "))
            print("Valoarea temperaturii dupa transformare este: ", "{:.2f}".format(get_temp(temp, From, to)))

        elif optiune == "x":
                break
        else:
            print("Optiune invalida!")


def get_leap_years(start, end):
        """
        Afiseaza toti anii bisecti intre doi ani dati(inclusiv anii dati)
        input : start, end -> int
        output : anii bisecti dintre start si end -> list[int]
        """
        list = []

        if (start > end) or (start == 0) and (end == 0):
            return list

        while start <= end:
            if (start % 4 == 0) and (start % 100 != 0) or (start % 100 == 0) and (start % 400 == 0):
                list.append(int(start))
            start = start + 1

        return list


def get_perfect_squares(start, end):
    """
      Afiseaza toate patratele perfecte intr-un interval inchis dat.
        input : start, end -> int
        output : numerele patrate perfecte intre start si end -> list[int]
    """

    list = []
    for i in range(start, end + 1):
        j = 1
        while j * j <= i:
            if j * j == i:
                list.append(i)
            j = j + 1
        i = i + 1
    return list


def get_temp(temp, From, to):
    """
    Transformă o temperatură dată într-o scară dată (`K`, `F` sau `C`) într-o altă scară dată.
    :param temp: Valoarea temperaturii care va fi transformata
    :param From: Scara in care este temperatura
    :param to: Scara in care se va transforma temperatura
    :return: Valoarea temperaturii dupa transformare
    """

    if (From == 'C') and (to == 'K'):
        return temp + 273.15
    if (From == 'C') and (to == 'F'):
        return temp*(9/5)+32

    if (From == 'K') and (to == 'C'):
        return temp - 273.15
    if (From == 'K') and (to == 'F'):
        return (temp - 273.15) * (9/5) + 32

    if (From == 'F') and (to == 'C'):
        return (temp - 32) * (5/9)
    if (From == 'F') and (to == 'K'):
        return (temp - 32) * (5/9) + 273.15



def test_get_leap_years():


    assert get_leap_years(2000, 2008) == [2000, 2004, 2008]
    assert get_leap_years(2001, 2021) == [2004, 2008, 2012, 2016, 2020]
    assert get_leap_years(1990, 2005) == [1992, 1996, 2000, 2004]
    assert get_leap_years(2005, 2005) == []
    assert get_leap_years(2009, 2008) == []


test_get_leap_years()

def test_get_perfect_squares():


    assert get_perfect_squares(3, 9) == [4, 9]
    assert get_perfect_squares(3, 3) == []
    assert get_perfect_squares(12, 36) == [16, 25, 36]
    assert get_perfect_squares(10, 9) == []
    assert get_perfect_squares(2, 100) == [4, 9, 16, 25, 36, 49, 64, 81, 100]

test_get_perfect_squares()


def test_get_temp():

    assert "{:.2f}".format(get_temp(100, 'C', 'K')) == '373.15'
    assert "{:.2f}".format(get_temp(56, 'C', 'F')) == '132.80'
    assert "{:.2f}".format(get_temp(629, 'K', 'C')) == '355.85'
    assert "{:.2f}".format(get_temp(120, 'K', 'F')) == '-243.67'
    assert "{:.2f}".format(get_temp(566, 'F', 'C')) == '296.67'
    assert "{:.2f}".format(get_temp(120, 'F', 'K')) == '322.04'

test_get_temp()


main()