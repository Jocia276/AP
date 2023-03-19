from Domain.vanzare2 import get_pret
from Logic.crud import create, read
from Logic.discount import add_gold_discount, add_silver_discount, add_discount


def test_add_gold_discount():
    try:
        assert add_gold_discount(50) == 45
        assert add_gold_discount(100) == 90
        assert add_gold_discount(45.5) == 40.95
        assert add_gold_discount(20) == 18
    except AssertionError:
        print('Assertion error at test_add_gold_discount!')


def test_add_silver_discount():
    try:
        assert add_silver_discount(50) == 47.5
        assert add_silver_discount(100) == 95
        assert add_silver_discount(45.5) == 43.225
        assert add_silver_discount(20) == 19
    except AssertionError:
        print('Assertion error at test_add_silver_discount!')


def test_add_discount():
    try:
        vanzari = []
        vanzari = create(vanzari, 1, 'Ion', 'roman', 50, 'silver')
        vanzari = create(vanzari, 2, 'Enigma Otiliei', 'roman', 45.5, 'gold')
        vanzari = create(vanzari, 3, 'O scrisoare pierduta', 'comedie', 12, 'none')
        vanzari = create(vanzari, 4, 'Morometii', 'roman', 120, 'gold')
        vanzari = create(vanzari, 5, 'Harap-Alb', 'basm', 63, 'silver')
        vanzari = add_discount(vanzari)

        assert get_pret(read(vanzari, 1)) == 47.5
        assert get_pret(read(vanzari, 2)) == 40.95
        assert get_pret(read(vanzari, 3)) == 12
        assert get_pret(read(vanzari, 4)) == 108
        assert get_pret(read(vanzari, 5)) == 59.85

    except AssertionError:
        print('Assertion error at test_add_discount!')


def test_discount():
    test_add_silver_discount()
    test_add_gold_discount()
    test_add_discount()
