from Domain.vanzare2 import get_gen
from Logic.crud import create, read
from Logic.modificare_gen import modificare_gen


def test_modificare_gen():
    try:
        vanzari = []
        vanzari = create(vanzari, 1, 'Ion', 'schita', 50, 'silver')
        vanzari = create(vanzari, 2, 'Moara cu noroc', 'nuvela', 50, 'silver')
        vanzari = create(vanzari, 3, 'Enigma Otiliei', 'roman balzacian', 50, 'silver')
        vanzari = create(vanzari, 4, 'Ion', 'povestire', 50, 'silver')
        vanzari = create(vanzari, 5, 'Ion', 'comedie', 50, 'silver')
        vanzari = modificare_gen(vanzari, 'Ion', 'roman obiectiv')

        assert get_gen(read(vanzari, 1)) == 'roman obiectiv'
        assert get_gen(read(vanzari, 2)) == 'nuvela'
        assert get_gen(read(vanzari, 3)) == 'roman balzacian'
        assert get_gen(read(vanzari, 4)) == 'roman obiectiv'
        assert get_gen(read(vanzari, 5)) == 'roman obiectiv'

    except AssertionError:
        print('Assertion error at test_modificare_gen!')
