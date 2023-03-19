from Domain.card import Card


class CardValidationError(Exception):
    pass


class CardValidator:

    def validate(self, card: Card):
        erori = []
        if len(card.cnp) != 13 or not card.cnp.isdecimal():
            erori.append("CNP-ul trebuie sa fie format din fix 13 cifre!")
        if erori:
            raise CardValidationError(erori)
