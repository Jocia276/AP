from Domain.vanzare2 import get_id
from Logic.ordonare_vanzari_dupa_pret import ordonare_vanzari_dupa_pret
from Tests.test_crud import get_data


def test_ordonare_vanzari_dupa_pret():
    try:
        vanzari = get_data()
        lst_ordonata = ordonare_vanzari_dupa_pret(vanzari)

        assert len(lst_ordonata) == 6
        assert get_id(lst_ordonata[0]) == 6
        assert get_id(lst_ordonata[3]) == 2
        assert get_id(lst_ordonata[5]) == 4

    except AssertionError:
        print("Assertion Error at test_ordonare_vanzari_dupa_pret")