from Domain.card_validator import CardValidator
from Domain.medicament_generator import MedicamentGenerator
from Domain.medicament_validator import MedicamentValidator
from Repository.json_repository import JsonRepository
from Service.card_service import CardService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Service.undo_redo_service import UndoRedoService
from utile import clear_file


def test_undo_redo():

    filename = 'test_medicament_service.json'
    clear_file(filename)

    medicament_repository = JsonRepository(filename)
    medicament_validator = MedicamentValidator()
    medicament_generator = MedicamentGenerator()
    undo_redo_service = UndoRedoService()
    medicament_service = MedicamentService(medicament_repository,
                                           medicament_validator,
                                           medicament_generator,
                                           undo_redo_service)

    filename = 'test_card_service.json'
    clear_file(filename)
    card_repository = JsonRepository(filename)
    card_validator = CardValidator()
    card_service = CardService(card_repository,
                               card_validator,
                               undo_redo_service)

    filename = 'test_tranzactie_service.json'
    clear_file(filename)
    tranzactie_repository = JsonRepository(filename)
    tranzactie_service = TranzactieService(medicament_repository,
                                           card_repository,
                                           tranzactie_repository,
                                           undo_redo_service)

    medicament_service.add_med('1', 'paracetamol', 'zentiva', 2.5, 'nu')
    medicament_service.add_med('2', 'decasept', 'terapia', 50, 'nu')
    medicament_service.add_med('3', 'strepsils', 'terapia', 35, 'nu')

    undo_redo_service.do_undo()
    assert len(medicament_repository.read()) == 2

    undo_redo_service.do_undo()
    assert len(medicament_repository.read()) == 1

    undo_redo_service.do_redo()
    assert len(medicament_repository.read()) == 2

    medicament_service.delete_med('1')
    assert len(medicament_repository.read()) == 1
    undo_redo_service.do_undo()
    assert len(medicament_repository.read()) == 2

    medicament_service.update_med('1', 'paracetamol', 'zentiva', 250, 'da')
    assert len(medicament_repository.read()) == 2

    card_service.add_card('1', 'Ion', 'Vasile', '6020627271819', '22.02.2020',
                          '22.02.2023')
    card_service.add_card('2', 'Popa', 'Vasile', '6020627271829',
                          '22.02.2020', '22.02.2023')
    card_service.add_card('3', 'Mihaiasa', 'Vasile', '6020627279999',
                          '22.02.2020', '22.02.2023')

    assert len(card_repository.read()) == 3
    undo_redo_service.do_undo()
    undo_redo_service.do_undo()
    undo_redo_service.do_undo()
    assert len(card_repository.read()) == 0
    undo_redo_service.do_redo()
    undo_redo_service.do_redo()
    assert len(card_repository.read()) == 2

    card_service.delete_card('1')
    assert len(card_repository.read()) == 1
    undo_redo_service.do_undo()
    assert len(card_repository.read()) == 2
    undo_redo_service.do_redo()
    assert len(card_repository.read()) == 1

    card_service.update_card('2', 'Ion', 'Vasile', '6020627271819',
                             '22.02.2020', '22.02.2024')
    assert len(card_repository.read()) == 1

    medicament_service.delete_med('1')
    medicament_service.delete_med('2')
    assert len(medicament_repository.read()) == 0

    card_service.delete_card('2')
    assert len(card_repository.read()) == 0

    card_service.add_card('1', 'Popica', 'Mihai', '6020728291823',
                          '28.07.2002', '23.11.2021')
    card_service.add_card('2', 'Mihaila', 'Ion', '6020728291824',
                          '28.07.2004', '23.11.2011')

    medicament_service.add_med('1', 'paracetamol', 'zentiva', 2, 'nu')
    medicament_service.add_med('2', 'decasept', 'terapia', 5.2, 'da')

    tranzactie_service.add_tranzactie('1', '2', '1', 1, '23.11.2021', '19:34')
    tranzactie_service.add_tranzactie('2', '1', '2', 3, '23.11.2000', '19:34')

    undo_redo_service.do_undo()
    assert len(tranzactie_repository.read()) == 1
    undo_redo_service.do_redo()
    assert len(tranzactie_repository.read()) == 2
