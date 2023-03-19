from Domain.vanzare2 import get_str, creeaza_vanzare
from Logic.crud import create, update, read, delete
from Logic.discount import add_discount
from Logic.modificare_gen import modificare_gen


def show_all(lista_vanzari):
    for vanzare in lista_vanzari:
        print(get_str(vanzare))


def adauga_vanzare(lista_vanzari, id_vanzare, titlu_carte, gen_carte, pret, tip_discount_client):
    try:
        return create(lista_vanzari, id_vanzare, titlu_carte, gen_carte, pret, tip_discount_client)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista_vanzari

def modifica_vanzare(lista_vanzari, id_vanzare, titlu_carte, gen_carte, pret, tip_discount_client):
    try:
        return update(lista_vanzari, creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_discount_client))
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista_vanzari

def citeste_vanzare(lista_vanzari, id_vanzare):
    try:
        return read(lista_vanzari, id_vanzare)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista_vanzari

def sterge_vanzare(lista_vanzari, id_vanzare):
    try:
        return delete(lista_vanzari, id_vanzare)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista_vanzari

def aplica_discount(lista_vanzari):
    try:
        return add_discount(lista_vanzari)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista_vanzari

def modificare_gen1(lista_vanzari, titlu, gen_nou):
    try:
        return modificare_gen(lista_vanzari, titlu, gen_nou)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista_vanzari

def help():
    print("add ID nume clasa pret checkin facut -> adauga vanzare")
    print("delete id -> sterge vanzare")
    print("update id nume clasa pret checkin facut -> modifica vanzare")
    print("showall -> afiseaza toate vanzarile")
    print("discount -> aplicarea unui discount de 5% pentru toate reducerile silver si "
          "10% pentru toate reducerile gold.")
    print("modificare_gen -> modificarea genului pentru un titlu dat")
    print("x -> opreste programul")


def run_ui2(lista_vanzari):

    done = False
    while not done:
        mesaj = input('Introduceti comanda: ')
        comanda = mesaj.split(";")
        for i in range(len(comanda)):
            optiuni = comanda[i].split(" ")
            if optiuni[0] == 'exit':
                done = True
            elif optiuni[0] == "add":
                    lista_vanzari = adauga_vanzare(lista_vanzari, optiuni[1], optiuni[2], optiuni[3], optiuni[4], optiuni[5])
            elif optiuni[0] == "showall":
                show_all(lista_vanzari)
            elif optiuni[0] == "update":
                lista_vanzari = modifica_vanzare(lista_vanzari, optiuni[1], optiuni[2], optiuni[3], optiuni[4], optiuni[5])
            elif optiuni[0] == "delete":
                    lista_vanzari = sterge_vanzare(lista_vanzari, optiuni[1])
            elif optiuni[0] == "discount":
                lista_vanzari = aplica_discount(lista_vanzari)
            elif optiuni[0] == "gen":
                lista_vanzari = modificare_gen1(lista_vanzari, optiuni[1], optiuni[2])
            elif optiuni[0] == 'help':
                help()
            else:
                print("Optiune gresita! Acceseaza comanda 'help'!")
    return lista_vanzari

