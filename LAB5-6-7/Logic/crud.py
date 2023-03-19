from Domain.vanzare2 import creeaza_vanzare, get_id


def create(lst_vanzari, id_vanzare: int, titlu_carte: str, gen_carte: str, pret: float, tip_reducere_client):
    """
    Creeaza o vanzare.
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii, trebuie sa fie unic.
    :param titlu_carte: titlul cartii, nenul
    :param gen_carte: genul cartii, nenul
    :param pret: pretul cartii
    :param tip_reducere_client: reducerea oferita clientilor, ce poate fi none, silver sau gold
    :return: o noua lista formata din lst_vanzari si noua vanzare adaugata
    """
    if read(lst_vanzari, id_vanzare) is not None:
        raise ValueError(f'Exista deja o vanzare cu id-ul {id_vanzare} ')

    vanzare = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere_client)

    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare: int = None):
    """
    Citeste o vanzare din "baza de date"/lista de vanzari
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii dorite
    :return: - vanzarea cu id-ul id_vanzare, daca exista
             - lista cu toate vanzarile, daca id_vanzare=None
             - None, daca nu exista o vanzare cu id_vanzare
    """

    if not id_vanzare:
        return lst_vanzari

    vanzare_cu_id = None
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            vanzare_cu_id = vanzare

    if vanzare_cu_id:
        return vanzare_cu_id
    return None


def update(lst_vanzari, new_vanzare: int):
    """
    Actualizeaza/modifica o vanzare
    :param lst_vanzari: lista de vanzari
    :param new_vanzare: vanzarea care se va actualiza - id-ul trebuie sa fie unul existent
    :return: o lista cu vanzarea actualizata
    """
    if read(lst_vanzari, get_id(new_vanzare)) is None:
        raise ValueError(f'Nu exista o vanzare cu id-ul {get_id(new_vanzare)} pe care sa o actualizam.')

    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(vanzare)
        else:
            new_vanzari.append(new_vanzare)

    return new_vanzari


def delete(lst_vanzari, id_vanzare: int):
    """
    Sterge o vanzare din "baza de date"/lista de vanzari
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii
    :return: o lista de vanzari fara vanzarea cu id-ul id_vanzare
    """

    if read(lst_vanzari, id_vanzare) is None:
        raise ValueError(f'Nu exista o vanzare cu id-ul {id_vanzare} pe care sa o stergem.')

    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)
    return new_vanzari
