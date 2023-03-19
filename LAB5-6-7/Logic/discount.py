from Domain.vanzare2 import get_id, get_titlu, get_gen, get_pret, get_reducere, creeaza_vanzare
from Logic.crud import update

# 4.2
# Aplicarea unui discount de `5%` pentru toate reducerile silver si `10%` pentru toate reducerile gold.


def add_silver_discount(pret: float) -> float:
    """
    Returneaza pretul dupa ce a fost aplicat un dicount de 5% (discount de tip silver)
    :param pret:pret initial
    :return: pretul dupa ce a fost aplicat un dicount de 5% (discount de tip silver)
    """
    if pret <= 0:
        raise ValueError('Cartea trebuie sa aiba un pret pozitiv!')

    discount = 5 * pret / 100
    return pret - discount


def add_gold_discount(pret: float) -> float:
    """
    Returneaza pretul dupa ce a fost aplicat un discount de 10% (discount de tip gold)
    :param pret:pret initial
    :return: pretul dupa ce a fost aplicat un discount de 10% (discount de tip gold)
    """
    if pret <= 0:
        raise ValueError('Cartea trebuie sa aiba un pret pozitiv!')

    discount = 10 * pret / 100
    return pret - discount


def add_discount(vanzari: list):
    """
    Adauga un discount de 5% reduccerilor de tip silver, si unul de 10% reducerilor de tip gold,
    returnand o lista cu noile preturi dupa aplicarea discountului.
    :param vanzari: lista de vanzari, ce contine preturile initiale ale cartilor, precum si restul datelor acestora
    :return: o noua lista, ce contine preturile modificate dupa reducere ale cartilor, cat si restul datelor
            ale acestora
    """
    if len(vanzari) == 0:
        raise ValueError("Lista nu poate fi goala!")

    for vanzare in vanzari:

        id_vanzare = get_id(vanzare)
        titlu_carte = get_titlu(vanzare)
        gen_carte = get_gen(vanzare)
        pret_nou = get_pret(vanzare)
        tip_reducere_client = get_reducere(vanzare)

        if tip_reducere_client == 'silver':
            pret_nou = add_silver_discount(pret_nou)
            creeaza_vanzare1 = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret_nou, tip_reducere_client)
            vanzari = update(vanzari, creeaza_vanzare1)

        elif tip_reducere_client == 'gold':
            pret_nou = add_gold_discount(pret_nou)
            creeaza_vanzare1 = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret_nou, tip_reducere_client)
            vanzari = update(vanzari, creeaza_vanzare1)

    return vanzari
