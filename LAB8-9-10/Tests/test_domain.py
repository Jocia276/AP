from Domain.card import Card
from Domain.medicament import Medicament
from Domain.tranzactie import Tranzactie


def test_domain():
    def test_medicament():
        medicament = Medicament('1', 'paracetamol', 'terapia', 25, 'nu')
        assert medicament.pret == 25
        assert medicament.necesita_reteta == 'nu'
        medicament.nume = 'strepsils'
        assert medicament.nume == 'strepsils'

    def test_card():
        card = Card('1', 'Apopi', 'Ilie', '6020127281705',
                    '27.01.2002', '23.11.2021')
        assert card.nume == 'Apopi'
        assert card.cnp == '6020127281705'
        card.data_nasterii = '27.02.2002'
        assert card.data_nasterii == '27.02.2002'

    def test_tranzactie():
        tranzactie = Tranzactie('1', '1', '1', 2, '23.11.2020',
                                '16:14', 22.5, 2.5)
        assert tranzactie.pret_platit == 22.5
        assert tranzactie.id_card == '1'
        assert tranzactie.valoare_reduceri == 2.5
        tranzactie.data = '21.02.2021'
        assert tranzactie.data == '21.02.2021'

    test_medicament()
    test_card()
    test_tranzactie()
