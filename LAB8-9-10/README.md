**Online pharmacy**

1. CRUD drug: id, name, manufacturer, price, requires prescription. The price must be strictly positive.
2. CRUD customer card: id, name, surname, CNP, date of birth (`dd.mm.yyyy`), date of registration (`dd.mm.yyyy`). The CNP must be unique.
3. CRUD transaction: id, drug_id, client_card_id (may be null), piece_nr, date and time. If there is a customer card, then apply a discount of `10%` if the drug does not require a prescription and `15%` if it does. The price paid and discounts given are printed.
4. Search for drugs and customers. Full text search.
5. Display all transactions in a given range of days.
6. Display of drugs in descending order by number of sales.
7. Display of customer cards in descending order according to the amount of discounts obtained.
8. Delete all transactions in a certain range of days.
9. Increasing the price by a given percentage of all drugs priced below a given value.