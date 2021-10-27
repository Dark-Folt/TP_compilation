#! /usr/bin/env python3



data = []
with open("chaine.txt") as fichier:
    data = fichier.read().split(" ")
    print(data)
