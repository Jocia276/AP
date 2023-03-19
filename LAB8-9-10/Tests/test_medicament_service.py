from Domain.medicament_generator import MedicamentGenerator
from Domain.medicament_validator import MedicamentValidator
from Repository.json_repository import JsonRepository
from Service.medicament_service import MedicamentService
from Service.undo_redo_service import UndoRedoService
from utile import clear_file


def test_medicament_service():
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

    medicament_service.add_med('1', 'paracetamol', 'zentiva', 2.55, 'nu')
    medicament_service.add_med('2', 'decasept', 'terapia', 50, 'nu')
    medicament_service.add_med('3', 'strepsils', 'terapia', 35, 'nu')

    assert len(medicament_repository.read()) == 3

    medicament_service.delete_med('3')
    assert len(medicament_repository.read()) == 2

    medicament_service.add_med('3', 'strepsils', 'terapia', 35, 'nu')
    medicament_service.delete_med('3')
    medicament_service.delete_med('2')
    assert len(medicament_repository.read()) == 1
