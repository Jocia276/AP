from Logic.crud import create
from Tests.test_crud import test_crud
from Tests.test_discount import test_discount
from Tests.test_modificare_gen import test_modificare_gen
from Tests.test_nr_titluri_distincte import test_nr_titluri_distincte
from Tests.test_ordonare_vanzari_dupa_pret import test_ordonare_vanzari_dupa_pret
from Tests.test_pret_minim import test_pret_minim
from Tests.test_undo_redo import test_undo_redo
from Userinterface.console import run_ui


def main():

    vanzari = []
    vanzari = create(vanzari, 1, 'Ion', 'roman', 50, 'silver')
    vanzari = create(vanzari, 2, 'Enigma Otiliei', 'roman', 45.5, 'gold')
    vanzari = create(vanzari, 3, 'O scrisoare pierduta', 'comedie', 12, 'none')
    vanzari = create(vanzari, 4, 'Morometii', 'roman', 120, 'gold')
    vanzari = create(vanzari, 5, 'Harap-Alb', 'basm', 63, 'silver')

    run_ui(vanzari)


if __name__ == '__main__':
    test_undo_redo()
    test_pret_minim()
    test_nr_titluri_distincte()
    test_ordonare_vanzari_dupa_pret()
    test_crud()
    test_discount()
    test_modificare_gen()
    main()
