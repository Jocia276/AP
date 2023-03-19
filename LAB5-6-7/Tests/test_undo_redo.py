from Logic.crud import create
from Userinterface.console import handle_new_list, handle_undo, handle_redo


def test_undo_redo():
    lst_vanzari = []
    list_version = [lst_vanzari]
    current_version = 0
    lst_vanzari = create(lst_vanzari, 1, 'Ion', 'roman', 56, 'gold')
    list_version, current_version = handle_new_list(list_version, current_version, lst_vanzari)
    lst_vanzari = create(lst_vanzari, 2, 'Moara cu noroc', 'nuvela', 33, 'silver')
    list_version, current_version = handle_new_list(list_version, current_version, lst_vanzari)
    lst_vanzari = create(lst_vanzari, 3, 'O scrisoare pierduta', 'comedie', 100, 'none')
    list_version, current_version = handle_new_list(list_version, current_version, lst_vanzari)

    lst_vanzari, current_version = handle_undo(list_version, current_version)
    assert len(lst_vanzari) == 2

    lst_vanzari, current_version = handle_undo(list_version, current_version)
    assert len(lst_vanzari) == 1

    lst_vanzari, current_version = handle_undo(list_version, current_version)
    assert len(lst_vanzari) == 0

    lst_vanzari, current_version = handle_undo(list_version, current_version)
    assert len(lst_vanzari) == 0

    lst_vanzari = create(lst_vanzari, 1, 'morometii', 'roman', 150, 'gold')
    list_version, current_version = handle_new_list(list_version, current_version, lst_vanzari)
    lst_vanzari = create(lst_vanzari, 2, 'enigma otiliei', 'roman', 10.5, 'none')
    list_version, current_version = handle_new_list(list_version, current_version, lst_vanzari)
    lst_vanzari = create(lst_vanzari, 3, 'ABC', 'documentar', 99.99, 'none')
    list_version, current_version = handle_new_list(list_version, current_version, lst_vanzari)

    lst_vanzari, current_version = handle_redo(list_version, current_version)
    assert len(lst_vanzari) == 3

    lst_vanzari, current_version = handle_undo(list_version, current_version)
    lst_vanzari, current_version = handle_undo(list_version, current_version)
    assert len(lst_vanzari) == 1

    lst_vanzari, current_version = handle_redo(list_version, current_version)
    assert len(lst_vanzari) == 2

    lst_vanzari, current_version = handle_redo(list_version, current_version)
    assert len(lst_vanzari) == 3

    lst_vanzari, current_version = handle_undo(list_version, current_version)
    lst_vanzari, current_version = handle_undo(list_version, current_version)
    assert len(lst_vanzari) == 1

    lst_vanzari = create(lst_vanzari, 4, 'Book', 'gen', 23, 'gold')
    list_version, current_version = handle_new_list(list_version, current_version, lst_vanzari)

    lst_vanzari, current_version = handle_redo(list_version, current_version)
    assert len(lst_vanzari) == 2

    lst_vanzari, current_version = handle_undo(list_version, current_version)
    assert len(lst_vanzari) == 1

    lst_vanzari, current_version = handle_undo(list_version, current_version)
    assert len(lst_vanzari) == 0

    lst_vanzari, current_version = handle_redo(list_version, current_version)
    lst_vanzari, current_version = handle_redo(list_version, current_version)
    assert len(lst_vanzari) == 2

    lst_vanzari, current_version = handle_redo(list_version, current_version)
    assert len(lst_vanzari) == 2
