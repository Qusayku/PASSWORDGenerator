import random
import string
import time

def generate_random_letters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_and_save_numbers_as_letters(path):
    # Liste mit 100 zufälligen Buchstaben-Zahlen generieren
    random_numbers = [generate_random_letters(6) for _ in range(100)]

    # Zahlen in die Datei schreiben
    with open(path, 'w') as file:
        for number in random_numbers:
            file.write(number + '\n')

    print(" Sie HABEN nun 97 neu generierte PASSWÖRTER ! ")

# Timer-Funktion
def loading_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Ladezeit: {i} Sekunden", end='\r')
        time.sleep(1)
    print("Ladezeit: ERFOLGREICH       ")

# "Made by Qusay" anzeigen
def display_made_by():
    print("Made by Qusay\n")

# Beispielanwendung
if __name__ == "__main__":
    display_made_by()
    loading_timer(5)  # Timer für 5 Sekunden
    file_path = "random_letters_numbers.txt"
    generate_and_save_numbers_as_letters(file_path)

