#!/usr/bin/env python 


class Regle:
    def __init__(self, terme_gauche, valeur) -> None:
        self.contenu = {terme_gauche : valeur}
    
    def get_valeur(self):
        return self.valeur

    def get_terme_gauche(self):
        return self.terme_gauche
    
    def to_string(self):
        print("{} ::= {}".format(self.terme_gauche, self.valeur))