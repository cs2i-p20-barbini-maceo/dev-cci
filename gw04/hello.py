import requests

print("Hello, World!")

with open("/output/demo.txt", "w", encoding="utf-8") as fichier:
    fichier.write("alpha")
    fichier.write("bravo")
    fichier.write("charlie")
