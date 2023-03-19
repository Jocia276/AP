from Domain.vanzare2 import get_gen, get_titlu


def nr_titluri_distincte(lst_vanzari):
    """
    Determina numarul de titluri distincte corespunzator fiecarui gen
    :param lst_vanzari: lista de vanzari (de carti)
    :return: numarul de titluri distincte corespunzator fiecarui gen
    """
    if len(lst_vanzari) == 0:
        raise ValueError("Lista nu poate fi goala!")

    result = {}
    lst_titluri = []
    for vanzare in lst_vanzari:
        gen = get_gen(vanzare)
        titlu = get_titlu(vanzare)
        if gen in result:
            if titlu not in lst_titluri:
                lst_titluri.append(titlu)
                result[gen] = result[gen] + 1
        else:
            result[gen] = 1
            lst_titluri.append(titlu)
    return result
