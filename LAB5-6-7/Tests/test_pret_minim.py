from Logic.pret_minim import get_pret_minim
from Tests.test_crud import get_data


def test_pret_minim():
    try:
        vanzari = get_data()
        pret_min = get_pret_minim(vanzari)

        assert len(pret_min) == 5
        assert pret_min[0][1] == 12
        assert pret_min[2][1] == 23

    except AssertionError:
        print("Assertion error at test_pret_min")

    pret_min2 = []

    try:
        get_pret_minim(pret_min2)
        assert False
    except ValueError:
        assert True
