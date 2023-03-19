from typing import List

from Domain.add_operation import AddOperation
from Domain.card import Card
from Domain.card_validator import CardValidator, CardValidationError
from Domain.delete_operation import DeleteOperation
from Domain.update_operation import UpdateOperation
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService


class CardService:
    def __init__(self,
                 card_repository: Repository,
                 card_validator: CardValidator,
                 undo_redo_service: UndoRedoService):
        self.card_repository = card_repository
        self.card_validator = card_validator
        self.undo_redo_service = undo_redo_service

    def add_card(self,
                 id_card: str,
                 nume: str,
                 prenume: str,
                 cnp: str,
                 data_nasterii: str,
                 data_inregistrarii: str):
        card = Card(id_card, nume, prenume, cnp,
                    data_nasterii, data_inregistrarii)

        CNP = card.cnp
        carduri = self.card_repository.read()
        for c in carduri:
            if c.cnp == CNP:
                raise CardValidationError("CNP trebuie sa fie unic!")

        self.card_validator.validate(card)
        self.card_repository.create(card)

        self.undo_redo_service.add_to_undo(AddOperation(
            self.card_repository, card))

    def update_card(self,
                    id_card: str,
                    nume: str,
                    prenume: str,
                    cnp: str,
                    data_nasterii: str,
                    data_inregistrarii: str):
        old_card = self.card_repository.read(id_card)
        card = Card(id_card, nume, prenume,
                    cnp, data_nasterii, data_inregistrarii)

        CNP = card.cnp
        carduri = self.card_repository.read()
        for c in carduri:
            if c.cnp == CNP:
                raise CardValidationError("CNP trebuie sa fie unic!")

        self.card_validator.validate(card)
        self.card_repository.update(card)

        self.undo_redo_service.add_to_undo(
            UpdateOperation(self.card_repository,
                            old_card,
                            card))

    def delete_card(self, id_card: str):
        card = self.card_repository.read(id_card)

        self.card_repository.delete(id_card)

        self.undo_redo_service.add_to_undo(
            DeleteOperation(self.card_repository, card))

    def get_all_card(self) -> List[Card]:
        return self.card_repository.read()

    def get_full_text(self, string_search) -> List:
        """
        :param string_search: stringul citit de la tastatura
        :return: toate cardurile care contin stringul citit
        """
        carduri = self.card_repository.read()

        def find(text, string):
            if len(text) <= 0:
                return None
            elif text[0:len(string)] == string:
                return string
            else:
                return find(text[1:], string)

        lst = []
        for card in carduri:
            if find(str(card).lower(), string_search.lower()):
                lst.append(card)
        return lst
