#! /usr/bin/env python
import hashlib

#sha256 Hash des zu knackenden Passworts
hashed_password: str = "614c3ccccf099995532a824b769bf62d5f818606f4b50d8eca6f58f7b83d96dc"

# Diese Funktion vergleicht zwei Variablen und gibt True zurück, wenn sie gleich sind ansonsten gibt sie False zurück
def compare_hashes(h1, h2) -> bool:
    if(h1 == h2):
        return True
    else:
        return False

# Diese Funktion generiert einen Hashwert mit dem sha256-Algortihmus
def generate_hash(unhashed) -> str:
    hashed = hashlib.sha256(unhashed.encode('utf-8')).hexdigest()
    return hashed

# Aufgabe:
# Knacke das Passwort mit einem Bruteforce-Angriff
# Das gesuchte Passwort wurde in Form eines SHA256-Hashes ergattert.
# Um es zu erraten können kannst Du für jeden Versuch einen Hashwert generieren und diesen mit dem vorligenden Hash vergleichen.

# Das Passwort hat 4 Zeichen
# Mögliche Zeichen sind A-Z und a-z
# Dies solltest Du mithilfe verschachtelter Schleifen hinbekommen ;)

# Hier ein paar Hints, wie die oberen Funktionen zu benutzen sind
#test_password = "Test"
#hashed_test_password=generate_hash(test_password)
#print(hashed_test_password)
#print(compare_hashes(hashed_test_password, hashed_password))

possible_chars: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"