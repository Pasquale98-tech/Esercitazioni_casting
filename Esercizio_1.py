# Esercizio 1: 
# - Chiedi all' utente di inserire un numero intero
# - Converti questo numero in numero decimale e stampalo
# - Converti lo stesso numero in stringa e lo stampalo insieme ad un messaggio

num_int = int(input("Inserisci un numero intero: "))
num_dec = float(num_int)
print("Numero in formato decimale:", num_dec)
num_str = str(num_int)
print("Il numero che hai inserito è: " + num_str)