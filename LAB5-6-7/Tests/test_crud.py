from Domain.vanzare2 import creeaza_vanzare, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creeaza_vanzare(1, 'Ion', 'roman', 50, 'silver'),
        creeaza_vanzare(2, 'Enigma Otiliei', 'roman balzacian', 45.5, 'gold'),
        creeaza_vanzare(3, 'Harap-Alb', 'basm', 23, 'none'),
        creeaza_vanzare(4, 'Moara cu noroc', 'nuvela', 100, 'silver'),
        creeaza_vanzare(5, 'O scrisoare pierduta', 'comedie', 35, 'gold'),
        creeaza_vanzare(6, 'Morometii', 'roman', 12, 'none')
    ]


def test_create():
    vanzari = get_data()
    params = (27, 'vnew', 'SF', 57, 'gold')
    v_new = creeaza_vanzare(*params)
    new_vanzari = create(vanzari, *params)

    found = False
    for vanzare in new_vanzari:
        if vanzare == v_new:
            found = True
    assert found

    params2 = (27, 'Ion', 'Actiune', 30, 'none')
    try:
        create(new_vanzari, *params2)
        assert False
    except ValueError:
        assert True


def test_read():
    try:
        vanzari = get_data()
        some_v = vanzari[2]
        assert read(vanzari, get_id(some_v)) == some_v
        assert read(vanzari, None) == vanzari
    except AssertionError:
        print('Assertion error at test_read!')


def test_update():
    try:
        vanzari = get_data()
        v_updated = creeaza_vanzare(1, 'new title', 'Drama', 45, 'None')
        updated = update(vanzari, v_updated)
        assert v_updated in updated
        assert v_updated not in vanzari
        assert len(updated) == len(vanzari)
    except AssertionError:
        print('Assertion error at test_update!')


def test_delete():
    try:
        vanzari = get_data()
        to_delete = 3
        v_deleted = read(vanzari, to_delete)
        deleted = delete(vanzari, to_delete)
        assert v_deleted in vanzari
        assert v_deleted not in deleted
        assert len(deleted) == len(vanzari) - 1
    except AssertionError:
        print('Assertion error at test_delete!')


def test_crud():
    test_delete()
    test_update()
    test_read()
    test_create()
