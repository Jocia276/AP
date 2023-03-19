from Domain.vanzare2 import get_gen, get_pret


def get_pret_minim(lst_vanzari):
    """
    Determina pretul minim pentru fiecare gen de carti
    :param lst_vanzari: lista de vanzari(de carti)
    :return: pretul minim pentru fiecare gen de carti
    """
    if len(lst_vanzari) == 0:
        raise ValueError("Lista nu poate fi goala!")

    lst_gen = []
    for vanzare in lst_vanzari:
        gen1 = get_gen(vanzare)
        if gen1 not in lst_gen:
            lst_gen.append(gen1)

    lst_pret_minim = []

    for gen in lst_gen:
        for vanzare in lst_vanzari:
            if get_gen(vanzare) == gen:
                pret_minim = get_pret(vanzare)
                break
        for vanzare in lst_vanzari:
            if get_gen(vanzare) == gen and get_pret(vanzare) < pret_minim:
                pret_minim = get_pret(vanzare)

        lst_pret_minim.append((gen, pret_minim))

    return lst_pret_minim
