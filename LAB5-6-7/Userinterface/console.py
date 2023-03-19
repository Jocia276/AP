from Domain.vanzare2 import get_str, creeaza_vanzare
from Logic.crud import create, update, delete
from Logic.discount import add_discount
from Logic.modificare_gen import modificare_gen
from Logic.nr_titluri_distincte import nr_titluri_distincte
from Logic.ordonare_vanzari_dupa_pret import ordonare_vanzari_dupa_pret
from Logic.pret_minim import get_pret_minim


def show_menu():
    print('1. Adaugare')
    print('2. Modificare')
    print('3. Stergere')
    print('4. Aplicare discount de 5% pentru toate reducerile silver, si 10% pentru toate reducerile gold.')
    print('5. Modificarea genului cartii in functie de un titlu dat.')
    print('6. Determinarea pretului minim pentru fiecare gen.')
    print('7. Ordonarea vanzarilor crescator dupa pret.')
    print('8. Afisarea numarului de titluri distincte pentru fiecare gen.')
    print('u. Undo')
    print('r. Redo')
    print('s. Showall')
    print('x. Exit')
    print(' ')


def handle_add(vanzari):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii: "))
        titlu_carte = input("Dati titlul cartii: ")
        gen_carte = input("Dati genul cartii: ")
        pret = float(input("Dati pretul vanzarii: "))
        tip_reducere_client = input("Dati tipul de reducere acordata clientului. Aceasta poate fi none, silver sau "
                                    "gold: ")
        return create(vanzari, id_vanzare, titlu_carte, gen_carte, pret, tip_reducere_client)
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_update(vanzari):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii care se actualizeaza: "))
        titlu_carte = input("Dati noul titlu al cartii: ")
        gen_carte = input("Dati noul gen al cartii: ")
        pret = float(input("Dati noul pret al vanzarii: "))
        tip_reducere_client = input("Dati noul tip de reducere acordata clientului. Aceasta poate fi none, silver sau "
                                    "gold: ")
        print('Modificarea a fost efectuata cu succes!')
        updated = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere_client)
        return update(vanzari, updated)
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_delete(vanzari):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii care se va sterge: "))
        vanzari = delete(vanzari, id_vanzare)
        print('Stergerea a fost efectuata cu succes!')
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_show_all(vanzari):
    try:
        for vanzare in vanzari:
            print(get_str(vanzare))
    except ValueError as ve:
        print('Eroare', ve)


def handle_discount(vanzari):
    try:
        print("Reducerea a fost aplicata cu succes!")
        vanzari = add_discount(vanzari)
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_modificare_gen(vanzari):
    try:
        titlul = input('Dati titlul cartii pentru care se va modifica genul: ')
        gen_nou = input('Dati noul gen al cartii: ')
        vanzari = modificare_gen(vanzari, titlul, gen_nou)
        print('Genul cartii a fost modificat cu succes!  ')
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_ordonare_vanzari_dupa_pret(vanzari):
    try:
        ordonate = ordonare_vanzari_dupa_pret(vanzari)
        return ordonate
    except ValueError as ve:
        print('Eroare: ', ve)

    return vanzari


def handle_pret_minim(vanzari):
    try:
        lst_pret_min = get_pret_minim(vanzari)

        for pret in lst_pret_min:
            print(f"Pretul minim pentru genul {pret[0]} este {pret[1]}")
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_nr_titluri_distincte(vanzari):
    try:
        rezultat = nr_titluri_distincte(vanzari)
        for gen in rezultat:
            print("Pentru genul {} exista {} titluri distincte".format(gen, rezultat[gen]))
    except ValueError as ve:
        print("Eroare: ", ve)
    return vanzari


def handle_new_list(list_versions, current_version, vanzari):
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(vanzari)
    current_version += 1
    return list_versions, current_version


def handle_undo(list_versions, current_version):
    if current_version < 1:
        print("Nu se mai poate face undo.")
        return [], 0
    current_version -= 1
    return list_versions[current_version], current_version


def handle_redo(list_versions, current_version):
    if current_version == len(list_versions) - 1:
        print("Nu se mai poate face redo.")
        return list_versions[current_version], current_version
    current_version += 1
    return list_versions[current_version], current_version


def run_ui(vanzari):

    list_versions = [vanzari]
    current_version = 0

    while True:
        print(" ")
        show_menu()
        optiune = input("Alege optiunea: ")
        if optiune == '1':
            vanzari = handle_add(vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
        elif optiune == '2':
            vanzari = handle_update(vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
        elif optiune == '3':
            vanzari = handle_delete(vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
        elif optiune == '4':
            vanzari = handle_discount(vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
        elif optiune == '5':
            vanzari = handle_modificare_gen(vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
        elif optiune == '6':
            vanzari = handle_pret_minim(vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
        elif optiune == '7':
            vanzari = handle_ordonare_vanzari_dupa_pret(vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
        elif optiune == '8':
            vanzari = handle_nr_titluri_distincte(vanzari)
            list_versions, current_version = handle_new_list(list_versions, current_version, vanzari)
        elif optiune == 'u':
            vanzari, current_version = handle_undo(list_versions, current_version)
        elif optiune == 'r':
            vanzari, current_version = handle_redo(list_versions, current_version)
        elif optiune == 's':
            handle_show_all(vanzari)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')
    return vanzari
