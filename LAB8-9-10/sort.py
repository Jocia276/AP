class Sortare:

    def __init__(self, ceva):
        '''
            Functie de initializare a clasei sort
            ceva - ceva de sortat dupa altceva

        '''

        self.ceva = ceva

    def my_sort(self, key=lambda x: x.getID(), reverse=True):
        '''
            Functie de sortare ceva
            self - ceva de sortat
            Functia returneaza o lista ce reprezinta lista initiala sortata
        '''

        lista = self.ceva

        i = 0
        while i < len(lista):
            if i == 0 or key(lista[i]) >= key(lista[i - 1]):
                i = i + 1
            else:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                i = i - 1

        if reverse is False:
            return lista
        return reversed(lista)
