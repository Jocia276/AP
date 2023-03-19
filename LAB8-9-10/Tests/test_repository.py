from Domain.card import Card
from Domain.medicament import Medicament
from Domain.tranzactie import Tranzactie
from Repository.json_repository import JsonRepository
from utile import clear_file


def test_repository():
    def test_card_repository():
        filename = 'test_card_repo.json'
        clear_file(filename)
        card_repository = JsonRepository(filename)
        assert card_repository.read() == []

        added = Card('1', 'Popescu', 'Ioan',
                     '5020202171819', '02.02.2002', '16.11.2021')
        card_repository.create(added)
        assert card_repository.read(added.id_entity) == added

        updated = Card('1', 'Grigore', 'Vasile',
                       '5020202171817', '02.02.2000', '16.11.2021')
        card_repository.update(updated)
        assert card_repository.read('1') == updated
        assert card_repository.delete("1") is None

    def test_medicament_repository():
        filename = 'test_medicament_repo.json'
        clear_file(filename)
        medicament_repository = JsonRepository(filename)
        assert medicament_repository.read() == []

        added = Medicament('1', 'paracetamol', 'zentiva', '25', 'nu')
        medicament_repository.create(added)
        assert medicament_repository.read('1') == added

        updated = Medicament('1', 'strepsils', 'terapia', '5', 'da')
        medicament_repository.update(updated)
        assert medicament_repository.read('1') == updated
        assert medicament_repository.delete('1') is None

    def test_tranzactie_repository():
        filename = 'test_tranzactie_repo.json'
        clear_file(filename)
        tranzactie_repository = JsonRepository(filename)
        assert tranzactie_repository.read() == []

        added = Tranzactie('1', '1', '1', 5, '2020-10-23', '15:58', 22.5, 2.5)
        tranzactie_repository.create(added)
        assert tranzactie_repository.read('1') == added

        updated = Tranzactie('1', '1', '1', 5, '16.11.2021',
                             '16:35', 4.25, 0.75)
        tranzactie_repository.update(updated)
        assert tranzactie_repository.read('1') == updated
        assert tranzactie_repository.delete('1') is None

    test_tranzactie_repository()
    test_card_repository()
    test_medicament_repository()
