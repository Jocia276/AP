from Logic.nr_titluri_distincte import nr_titluri_distincte
from Tests.test_crud import get_data


def test_nr_titluri_distincte():
    try:
        vanzari = get_data()
        nr_titluri = nr_titluri_distincte(vanzari)

        assert nr_titluri['roman'] == 2
        assert nr_titluri['nuvela'] == 1
        assert len(nr_titluri) == 5

    except AssertionError:
        print("Assertion error at test_nr_titluri_distincte!")
