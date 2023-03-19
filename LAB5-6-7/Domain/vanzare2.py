def creeaza_vanzare(id_vanzare: int, titlu_carte: str, gen_carte: str, pret: float, tip_reducere_client: str):
    """
    Creeaza o lista de vanzari.
    :param id_vanzare: int : id-ul vanzarii, trebuie sa fie unic
    :param titlu_carte: str : titlul cartii, nenul
    :param gen_carte: str : genul cartii, nenul
    :param pret: float : pretul cartii
    :param tip_reducere_client: str : reducerea oferita clientilor, ce poate fi none, silver sau gold
    :return: o lista de vanzari
    """
    return [id_vanzare, titlu_carte, gen_carte, pret, tip_reducere_client]


def get_id(vanzare):
    """
    Getter pentru id-ul vanzarii.
    :param vanzare: vanzarea
    :return: id-ul vanzarii
    """
    return vanzare[0]


def get_titlu(vanzare):
    """
    Getter pentru titlul cartii.
    :param vanzare: vanzarea
    :return: titlul cartii date spre vanzare
    """
    return vanzare[1]


def get_gen(vanzare):
    """
    Getter pentru genul cartii.
    :param vanzare: vanzarea
    :return: genul cartii date spre vanzare
    """
    return vanzare[2]


def get_pret(vanzare):
    """
    Getter pentru pretul cartii.
    :param vanzare: vanzarea
    :return: pretul cartii date spre vanzare
    """
    return vanzare[3]


def get_reducere(vanzare):
    """
    Getter pentru tipul reducerii pentru clienti.
    :param vanzare: vanzarea
    :return: tipul reducerii pentru clienti aferent vanzarii
    """
    return vanzare[4]


def get_str(vanzare):
    return f'Vanzarea cu id-ul {get_id(vanzare)} are titlul cartii {get_titlu(vanzare)},' \
           f' genul cartii {get_gen(vanzare)}, pretul {get_pret(vanzare)} si tipul de reducere acordata clientului' \
           f' {get_reducere(vanzare)}. '
