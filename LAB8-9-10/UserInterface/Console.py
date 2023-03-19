import datetime

from Domain.card_validator import CardValidationError
from Domain.medicament_generator import MedicamentGenerator
from Domain.medicament_validator import MedicamentValidationError
from Repository.exceptions import DuplicateIdError, NoSuchIdError
from Service.card_service import CardService
from Service.exceptions_service import ServiceValidationError, \
    NoMedError, NoCardError, NoTranzError
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Service.undo_redo_service import UndoRedoService


class Console:
    def __init__(self,
                 medicament_service: MedicamentService,
                 card_service: CardService,
                 tranzactie_service: TranzactieService,
                 medicament_generator: MedicamentGenerator,
                 undo_redo_service: UndoRedoService):
        self.medicament_service = medicament_service
        self.card_service = card_service
        self.tranzactie_service = tranzactie_service
        self.medicament_generator = medicament_generator
        self.undo_redo_service = undo_redo_service

    def showmenu(self):
        print(" ")
        print('a + med/card/tranz. Adauga medicament sau'
              ' card client sau tranzactie.')
        print('u + med/card/tranz. Update medicament sau'
              ' card client sau tranzactie.')
        print('d + med/card/tranz. Delete medicament sau'
              ' card client sau tranzactie.')
        print('s + med/card/tranz. Show all medicament sau'
              ' card client sau tranzactie.')
        print('lab8. Generare random.')
        print('1. Afisarea tuturor tranzactiilor '
              'dintr-un interval de zile dat.')
        print('2. Stergerea tuturor tranzactiilor '
              'dintr-un interval de zile dat.')
        print('3. Scumpirea cu un procentaj dat a '
              'tuturor medicamentelor cu pretul mai'
              ' mic decat o valoare data')
        print('4. Afisarea medicamentelor ordonate descrescator '
              'după numarul de vanzari')
        print('5. Afisarea cardurilor client ordonate descrescator '
              'dupa valoarea reducerilor obtinute.')
        print("s. Search full text.")
        print("u. Undo")
        print("r. Redo")
        print('c. stergere cascada')
        print('x. Iesire')
        print(" ")

    def run_console(self):
        while True:
            self.showmenu()
            opt = input("Alegeti optiunea: ")

            if opt == "amed":
                self.handle_add_medicament()
            elif opt == "acard":
                self.handle_add_card()
            elif opt == "atranz":
                self.handle_add_tranzactie()
            elif opt == 'dmed':
                self.handle_delete_medicament()
            elif opt == 'dcard':
                self.handle_delete_card()
            elif opt == 'dtranz':
                self.handle_delete_tranzactie()
            elif opt == 'umed':
                self.handle_update_medicament()
            elif opt == 'ucard':
                self.handle_update_card()
            elif opt == 'utranz':
                self.handle_update_tranzactie()
            elif opt == 'smed':
                self.handle_show_all(
                    self.medicament_service.get_all_med())
            elif opt == 'scard':
                self.handle_show_all(
                    self.card_service.get_all_card())
            elif opt == "stranz":
                self.handle_show_all(
                    self.tranzactie_service.get_all_tranzactie())
            elif opt == '1':
                self.handle_afisare_tranz_dupa_data()
            elif opt == 'lab8':
                self.handle_generare_random()
            elif opt == '2':
                self.handle_stergere_tranz_dupa_data()
            elif opt == '3':
                self.handle_scumpire_medicament()
            elif opt == '4':
                try:
                    ordered = self.tranzactie_service.\
                        medicamente_ordonate_dupa_nr_vanzari()
                    self.handle_show_all(ordered)
                except NoMedError as nme:
                    print("Eroare medicament: ", nme)
                except NoTranzError as nte:
                    print("Eroare tranzactie: ", nte)
                except Exception as e:
                    print("Eroare: ", e)
            elif opt == '5':
                try:
                    ordered = self.tranzactie_service.\
                        carduri_ordonate_desc_dupa_valoare_reduceri()
                    self.handle_show_all(ordered)
                except NoCardError as nce:
                    print("Eroare card: ", nce)
                except NoMedError as nme:
                    print("Eroare medicament: ", nme)
                except NoTranzError as nte:
                    print("Eroare tranzactie: ", nte)
                except Exception as e:
                    print("Eroare: ", e)
            elif opt == 's':
                self.handle_search_full_text()
            elif opt == 'u':
                self.undo_redo_service.do_undo()
            elif opt == 'r':
                self.undo_redo_service.do_redo()
            elif opt == 'c':
                self.handle_delete_cascada_medicament()
            elif opt == 'x':
                break
            else:
                print("Optiune invalida! Reincearca!")

    def handle_add_medicament(self):
        try:
            id_medicament = input(
                "Dati id-ul medicamentului: ")
            nume = input("Dati numele medicamentului: ")
            producator = input(
                "Dati producatorul medicamentului: ")
            pret = float(input("Dati pretul medicamentului: "))
            necesita_reteta = input(
                "Spuneti daca necesita reteta sau nu: ")
            self.medicament_service.add_med(
                id_medicament, nume, producator,
                pret, necesita_reteta)
        except MedicamentValidationError as mve:
            print("Eroare de validare : ", mve)
        except DuplicateIdError as de:
            print("ID duplicat: ", de)
        except Exception as ex:
            print("Eroare: ", ex)

    def handle_show_all(self, objects):
        for obj in objects:
            print(obj)

    def handle_add_card(self):
        try:
            id_card = input("Dati id-ul cardului: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            cnp = input("Dati CNP-ul clientului: ")
            data_nasterii = datetime.datetime.strptime(input(
                "Dati data nasterii clientului (dd.mm.yyyy): "), '%d.%m.%Y')
            data_inregistrarii = datetime.datetime.strptime(input(
                "Dati data inregistrarii clientului"
                " (dd.mm.yyyy): "), '%d.%m.%Y')
            self.card_service.add_card(id_card, nume, prenume, cnp,
                                       str(data_nasterii.date()),
                                       str(data_inregistrarii.date()))
        except CardValidationError as cve:
            print("Eroare de validare: ", cve)
        except DuplicateIdError as de:
            print("ID duplicat: ", de)
        except Exception as ex:
            print("Eroare: ", ex)

    def handle_add_tranzactie(self):
        try:
            id_tranzactie = input("Dati id-ul tranzactiei: ")
            id_medicament = input("Dati id-un medicamentului: ")
            id_card = input("Dati id-ul cardului: ")
            nr_bucati = int(input("Dati numarul de tranzactii: "))
            data = datetime.datetime.strptime(input(
                "Dati data tranzactiei (dd.mm.yyyy): "), '%d.%m.%Y')
            ora = datetime.datetime.strptime(input(
                "Dati ora tranzactiei (hh:mm): "), '%H:%M')
            self.tranzactie_service.add_tranzactie(
                id_tranzactie, id_medicament,
                id_card, nr_bucati, str(data.date()), str(ora.time()))

        except NoSuchIdError as nse:
            print("Eroare de ID : ", nse)
        except DuplicateIdError as de:
            print("ID duplicat: ", de)
        except Exception as ex:
            print("Eroare: ", ex)

    def handle_delete_medicament(self):
        try:
            id_medicament = input(
                "Dati id-ul medicamentului care se va sterge: ")
            self.medicament_service.delete_med(id_medicament)
        except NoSuchIdError as nie:
            print("Eroare de ID: ", nie)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_delete_cascada_medicament(self):
        try:
            id_medicament = input(
                "Dati id-ul medicamentului care se va sterge: ")
            self.tranzactie_service.delete_cascada(id_medicament)
        except NoSuchIdError as nie:
            print("Eroare de ID: ", nie)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_delete_card(self):
        try:
            id_card = input(
                "Dati id-ul medicamentului care se va sterge: ")
            self.card_service.delete_card(id_card)
            return "Cardul a fost sters cu succes! "
        except NoSuchIdError as nie:
            print("Eroare de ID: ", nie)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_delete_tranzactie(self):
        try:
            id_tranzactie = input(
                "Dati id-ul medicamentului care se va sterge: ")
            self.tranzactie_service.delete_tranzactie(id_tranzactie)
        except NoSuchIdError as nie:
            print("Eroare de ID: ", nie)
        except Exception as ex:
            print('Eroare: ', ex)

    def handle_update_medicament(self):
        try:
            id_medicament = input("Dati id-ul"
                                  " medicamentului care se va actualiza: ")
            nume = input("Dati numele medicamentului: ")
            producator = input("Dati producatorul medicamentului: ")
            pret = float(input("Dati pretul medicamentului: "))
            necesita_reteta = input("Spuneti daca necesita reteta sau nu: ")
            self.medicament_service.update_med(
                id_medicament, nume, producator, pret, necesita_reteta)
            print("Actualizarea a fost realizata cu succes! ")
        except NoSuchIdError as nie:
            print("Eroare de ID: ", nie)
        except Exception as ex:
            print("Eroare: ", ex)

    def handle_update_card(self):
        try:
            id_card = input("Dati id-ul cardului care se va actualiza: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            cnp = input("Dati CNP-ul clientului: ")
            data_nasterii = datetime.datetime.strptime(input(
                "Dati data nasterii clientului (dd.mm.yyyy): "), '%d.%m.%Y')
            data_inregistrarii = datetime.datetime.strptime(input(
                "Dati data inregistrarii clientului"
                " (dd.mm.yyyy): "), '%d.%m.%Y')
            self.card_service.update_card(
                id_card, nume, prenume, cnp,
                str(data_nasterii.date()),
                str(data_inregistrarii.date()))
            print("Actualizarea a fost realizata cu succes! ")
        except CardValidationError as cve:
            print("Eroare de validare: ", cve)
        except NoSuchIdError as nie:
            print("Eroare de ID: ", nie)
        except Exception as ex:
            print("Eroare: ", ex)

    def handle_update_tranzactie(self):
        try:
            id_tranzactie = input("Dati id-ul "
                                  "tranzactiei care se va actualiza: ")
            id_medicament = input("Dati id-un "
                                  "medicamentului: ")
            id_card = input("Dati id-ul cardului: ")
            nr_bucati = int(input("Dati numarul de tranzactii: "))

            data = datetime.datetime.strptime(input(
                "Dati data tranzactiei (dd.mm.yyyy): "), '%d.%m.%Y')
            ora = datetime.datetime.strptime(input(
                "Dati ora tranzactiei (hh:mm): "), '%H:%M')
            self.tranzactie_service.update_tranzactie(
                id_tranzactie, id_medicament, id_card, nr_bucati,
                str(data.date()), str(ora.time()))
            print("Actualizarea a fost realizata cu succes! ")
        except NoSuchIdError as nie:
            print("Eroare de ID: ", nie)
        except Exception as ex:
            print("Eroare: ", ex)

    def handle_afisare_tranz_dupa_data(self):
        try:
            data_initiala = datetime.datetime.strptime(input(
                "Dati data intiala (dd.mm.yyyy): "), '%d.%m.%Y')
            data_finala = datetime.datetime.strptime(input(
                "Dati data finala (dd.mm.yyyy): "), '%d.%m.%Y')
            print(self.tranzactie_service.afisare_tranzactii_dupa_data(
                str(data_initiala), str(data_finala)))
        except NoTranzError as nte:
            print("Eroare tranzactie: ", nte)
        except ServiceValidationError as sve:
            print("Eroare de validare: ", sve)
        except Exception as e:
            print('Eroare: ', e)

    def handle_generare_random(self):
        try:
            n = int(input("Dati un numar de generari random: "))
            for i in range(n):
                self.medicament_service.add_med(
                    self.medicament_generator.generare_id(),
                    self.medicament_generator.generare_nume(),
                    self.medicament_generator.generare_producator(),
                    self.medicament_generator.generare_pret(),
                    self.medicament_generator.generare_reteta())
            print("S-au generat medicamentele!")
        except Exception as e:
            print('Eroare: ', e)

    def handle_stergere_tranz_dupa_data(self):
        try:
            data_initiala = datetime.datetime.strptime(input(
                "Dati data intiala (dd.mm.yyyy): "), '%d.%m.%Y')
            data_finala = datetime.datetime.strptime(input(
                "Dati data finala (dd.mm.yyyy): "), '%d.%m.%Y')
            print(self.tranzactie_service.sterge_tranzactii_dupa_data(
                str(data_initiala), str(data_finala)))
        except NoTranzError as nte:
            print("Eroare tranzactie: ", nte)
        except ServiceValidationError as sve:
            print("Eroare de validare: ", sve)
        except Exception as e:
            print('Eroare: ', e)

    def handle_scumpire_medicament(self):
        try:
            pret_dat = float(input('Dati un pret: '))
            procent = int(input('Dati un procent: '))
            med = self.medicament_service.scumpire_medicament(
                procent, pret_dat)
            self.handle_show_all(med)
        except ServiceValidationError as sve:
            print('Eroare de validare: ', sve)
        except NoMedError as nme:
            print("Eroare medicament: ", nme)
        except Exception as e:
            print('Eroare: ', e)

    def handle_search_full_text(self):
        string_search = input("Dati stringul de cautare: ")
        print(" ")
        self.handle_show_all(self.card_service.get_full_text
                             (string_search))
        print(" ")
        self.handle_show_all(self.medicament_service.get_full_text
                             (string_search))
        print(" ")
        self.handle_show_all(self.tranzactie_service.get_full_text
                             (string_search))
