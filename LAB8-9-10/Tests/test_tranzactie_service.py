from Domain.card_validator import CardValidator
from Domain.medicament_generator import MedicamentGenerator
from Domain.medicament_validator import MedicamentValidator
from Repository.json_repository import JsonRepository
from Service.card_service import CardService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Service.undo_redo_service import UndoRedoService
from utile import clear_file


def test_tranzactie_service():
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
    undo_redo_service = UndoRedoService()
    card_service = CardService(card_repository,
                               card_validator,
                               undo_redo_service)

    filename = 'test_tranzactie_service.json'
    clear_file(filename)
    tranzactie_repository = JsonRepository(filename)
    undo_redo_service = UndoRedoService()
    tranzactie_service = TranzactieService(medicament_repository,
                                           card_repository,
                                           tranzactie_repository,
                                           undo_redo_service)

    card_service.add_card('1', 'Popica', 'Mihai', '6020728291823',
                          '28.07.2002', '23.11.2021')
    card_service.add_card('2', 'Mihaila', 'Ion', '6020728291824',
                          '28.07.2004', '23.11.2011')

    medicament_service.add_med('1', 'paracetamol', 'zentiva', 2, 'nu')
    medicament_service.add_med('2', 'decasept', 'terapia', 5.2, 'da')

    tranzactie_service.add_tranzactie('1', '2', '1', 1, '23.11.2021', '19:34')
    tranzactie_service.add_tranzactie('2', '1', '2', 3, '23.11.2000', '19:34')
    assert len(tranzactie_repository.read()) == 2

    tranzactie_service.update_tranzactie('2', '1', '1', 2, '23.11.2018',
                                         '20:09')
    assert len(tranzactie_repository.read()) == 2

    tranzactie_service.delete_tranzactie('2')
    assert len(tranzactie_repository.read()) == 1

    tranzactie_service.add_tranzactie('2pk', '1', '1', 3, '23.11.2002',
                                      '19:34')
    tranzactie_service.add_tranzactie('3', '2', '1', 2, '23.11.2008',
                                      '19:34')
    assert len(tranzactie_repository.read()) == 3

    # search full text
    assert len(tranzactie_service.get_full_text('3')) == 3
    assert len(tranzactie_service.get_full_text('pk')) == 1
    assert len(tranzactie_service.get_full_text('2008')) == 1

    # afisare respectiv stergere tranzactii dupa doua date citite
    # de la tastatura
    tranzactie_service.sterge_tranzactii_dupa_data('22.11.2017', '22.11.2019')
    assert len(tranzactie_repository.read()) == 3
    lista = tranzactie_service.afisare_tranzactii_dupa_data('23.11.2004',
                                                            '23.11.2009')
    assert len(lista) == 1
    lista = tranzactie_service.afisare_tranzactii_dupa_data('23.11.2023',
                                                            '23.11.2040')
    assert len(lista) == 0

    # ordonarea medicamentelor descrescator in functie de numarul de vanzari
    lst = tranzactie_service.medicamente_ordonate_dupa_nr_vanzari()
    assert len(lst) == 3
    assert lst[0].nume == 'paracetamol'
    assert lst[1].nr_bucati == 2

    # ordonarea cardurilor descrescator dupa valoarea reducerilor
    lista = tranzactie_service.carduri_ordonate_desc_dupa_valoare_reduceri()
    assert len(lista) == 3
    assert lista[0].id_entity == '1'
    assert lista[2].reduceri == 0.6000000000000001

    # stergea medicament + tranzactie in cascada

    assert len(tranzactie_repository.read()) == 3
    tranzactie_service.delete_cascada('1')
    assert len(tranzactie_repository.read()) == 2
    assert len(medicament_repository.read()) == 1
    tranzactie_service.delete_cascada('2')
    assert len(tranzactie_repository.read()) == 0
    assert len(medicament_repository.read()) == 0
