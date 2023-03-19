from Domain.card_validator import CardValidator
from Repository.json_repository import JsonRepository
from Service.card_service import CardService
from Service.undo_redo_service import UndoRedoService
from utile import clear_file


def test_card_service():
    filename = 'test_card_service.json'
    clear_file(filename)
    card_repository = JsonRepository(filename)
    card_validator = CardValidator()
    undo_redo_service = UndoRedoService()
    card_service = CardService(card_repository,
                               card_validator,
                               undo_redo_service)

    card_service.add_card('1', 'Ion', 'Vasile', '6020627271819', '22.02.2020',
                          '22.02.2023')
    card_service.add_card('2', 'Popa', 'Vasile', '6020627271829',
                          '22.02.2020', '22.02.2023')
    card_service.add_card('3', 'Mihaiasa', 'Vasile', '6020627279999',
                          '22.02.2020', '22.02.2023')

    assert len(card_repository.read()) == 3

    card_service.delete_card('3')
    assert len(card_repository.read()) == 2

    card_service.update_card('2', 'Aanei', 'Bogdan', '5020203271829',
                             '01.01.2002', '01.02.2023')
    assert len(card_repository.read()) == 2
