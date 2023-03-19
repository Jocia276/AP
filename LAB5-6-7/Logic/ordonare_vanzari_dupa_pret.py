from Domain.vanzare2 import get_pret


def pret(vanzare):
    """
    Determina pretul unei vanzari
    :param vanzare: o vanzare
    :return: pretul vanzarii
    """
    return get_pret(vanzare)


def ordonare_vanzari_dupa_pret(lst_vanzari):
    """
    Determina ordonarea vanzarilor crescator dupa pret
    :param lst_vanzari: lista de vanzari(de carti)
    :return: lista de vanzari ordonata crescator dupa pret
    """
    if len(lst_vanzari) == 0:
        raise ValueError("Lista nu poate fi goala!")

    return sorted(lst_vanzari, key=pret)
