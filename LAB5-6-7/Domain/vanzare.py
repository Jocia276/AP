def creeaza_vanzare(id_vanzare: int, titlu_carte: str, gen_carte: str, pret: float, tip_reducere_client: str):
    """
    Creeaza o vanzare(dictionar).
    :param id_vanzare: id-ul vanzarii, trebuie sa fie unic.
    :param titlu_carte: titlul cartii, nenul
    :param gen_carte: genul cartii, nenul
    :param pret: pretul cartii
    :param tip_reducere_client: reducerea oferita clientilor, ce poate fi none, silver sau gold
    :return: o vanzare
    """
    return {
        'id': id_vanzare,
        'titlu': titlu_carte,
        'gen': gen_carte,
        'pret': pret,
        'reducere': tip_reducere_client,
    }


def get_id(vanzare):
    """
    Getter pentru id-ul vanzarii.
    :param vanzare: vanzarea
    :return: id-ul vanzarii
    """
    return vanzare['id']


def get_titlu(vanzare):
    """
    Getter pentru titlul cartii.
    :param vanzare: vanzarea
    :return: titlul cartii date spre vanzare
    """
    return vanzare['titlu']


def get_gen(vanzare):
    """
    Getter pentru genul cartii.
    :param vanzare: vanzarea
    :return: genul cartii date spre vanzare
    """
    return vanzare['gen']


def get_pret(vanzare):
    """
    Getter pentru pretul cartii.
    :param vanzare: vanzarea
    :return: pretul cartii date spre vanzare
    """
    return vanzare['pret']


def get_reducere(vanzare):
    """
    Getter pentru tipul reducerii pentru clienti.
    :param vanzare: vanzarea
    :return: tipul reducerii pentru clienti aferent vanzarii
    """
    return vanzare['reducere']


def get_str(vanzare):
    return f'Vanzarea cu id-ul {get_id(vanzare)} are titlul cartii {get_titlu(vanzare)},' \
           f' genul cartii {get_gen(vanzare)}, pretul {get_pret(vanzare)} si tipul de reducere acordata clientului' \
           f' {get_reducere(vanzare)}. '
