from Domain.card_validator import CardValidator
from Domain.medicament_generator import MedicamentGenerator
from Domain.medicament_validator import MedicamentValidator
from Repository.json_repository import JsonRepository
from Service.card_service import CardService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Service.undo_redo_service import UndoRedoService
from Tests.test_card_service import test_card_service
from Tests.test_domain import test_domain
from Tests.test_medicament_service import test_medicament_service
from Tests.test_repository import test_repository
from Tests.test_tranzactie_service import test_tranzactie_service
from Tests.test_undo_redo import test_undo_redo
from UserInterface.Console import Console


def main():
    undo_redo_service = UndoRedoService()

    medicament_repository = JsonRepository("medicamente.json")
    medicament_validator = MedicamentValidator()
    medicament_generator = MedicamentGenerator()
    medicament_service = MedicamentService(medicament_repository,
                                           medicament_validator,
                                           medicament_generator,
                                           undo_redo_service)

    card_repository = JsonRepository("card_client.json")
    card_validator = CardValidator()
    card_service = CardService(card_repository,
                               card_validator,
                               undo_redo_service)

    tranzactie_repository = JsonRepository("tranzactie.json")
    tranzactie_service = TranzactieService(medicament_repository,
                                           card_repository,
                                           tranzactie_repository,
                                           undo_redo_service)

    console = Console(medicament_service,
                      card_service,
                      tranzactie_service,
                      medicament_generator,
                      undo_redo_service)
    console.run_console()


if __name__ == '__main__':
    test_undo_redo()
    test_tranzactie_service()
    test_medicament_service()
    test_card_service()
    test_repository()
    test_domain()
    main()
