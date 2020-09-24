# Hier importeert je de os module
import os

# De huidige directory opvragen en opslaan in de variabele: werkmap
werkmap = os.getcwd()

# De letters cwd staan voor: current working directory (de huidige map!)

bestand = open("test.txt", "w")

bestand.write("Test 123!");

bestand.close()

bestand2 = open("test.txt", "r")

bestand2.write("Lekker alles overschijven")

