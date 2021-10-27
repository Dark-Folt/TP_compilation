#!/usr/bin/env python3

## Table d'analyse
#                       |main(){| id  | int | float | nombre | if  | else | <  |  >  | =  | } |  ;  |  $  |
# Programme           1 |   1   |     |     |       |        |     |      |    |     |    |   |     |
# Liste_declarations  2 |       |  2  |  2  |   2   |        |     |      |    |     |    |   |     |
# Liste_declarations  3 |       |  3  |     |       |        |  3  |      |    |     |    | 3 |     |  3
# Une_declaration     4 |       |     |  4  |   4   |        |     |      |    |     |    |   |     |
# Liste instructions  5 |       |  5  |     |       |        |  5  |      |    |     |    |   |     |
# Liste instructions  6 |       |     |     |       |        |     |      |    |     |    | 6 |     |  6
# Une_instruction     7 |       |  7  |     |       |        |  7  |      |    |     |    |   |
# Une_instruction     8 |       |     |     |       |        |     |      |    |     |    |   |     |
# Type                9 |       |     |  9  |       |        |     |      |    |     |    |   |
# Type               10 |       |     |     |  10   |        |     |      |    |     |    |   |
# Affectation        11 |       |  11 |     |       |        |     |      |    |     |    |   |
# Test               12 |       |     |     |       |        | 12  |      |    |     |    |   |
# Condition          13 |       |  13 |     |       |        |     |      |    |     |    |   |
# Operateur          14 |       |     |     |       |        |     |      | 14 |     |    |   |
# Operateur          15 |       |     |     |       |        |     |      |    | 15  |    |   |
# Operateur          16 |       |     |     |       |        |     |      |    |     | 16 |   |




terminaux = {
    0 : "main()",
    1 : "id",
    2 : "int",
    3 : "float",
    4 : "nombre",
    5 : "if",
    6 : "else",
    7 : "<",
    8 : ">",
    9 : "=",
    10: "}",
    11: ";",
    12: "vide",
    13: "{"
}

grammaire = {
    0: "<Programme ::= main(){<liste_declarations><liste_instructions>}",
    1: "<liste_declarations> ::= <une_declaration><liste_declarations>",
    2: "<liste_declarations> ::= vide",
    3: "<une_declaration> ::= <type>id",
    4: "<liste_instructions> ::= <une_instruction><liste_instructions>",
    5: "<liste_instructions> ::= vide",
    6: "<une_instruction> ::= <affectation>",
    7: "<une_instruction> ::= <test>",
    8: "<type> ::= int",
    9 : "<type> ::= float",
    10: "<affectation> ::= id=nombre",
    11: "<test> ::= if<condition><instruction>else<instruction>",
    12: "<condition> ::= id<operateur>nombre",
    13: "<operateur> ::= <",
    14: "<operateur> ::= >",
    15: "<operateur> ::= =",
}

non_terminaux = {
    0: "<Programme>",
    1: "<liste_declarations>",
    2: "<liste_declarations>",
    3: "<une_declaration>",
    4: "<liste_instructions>",
    5: "<liste_instructions>",
    6: "<une_instruction>",
    7: "<une_instruction>",
    8: "<type>",
    9 : "<type>",
    10: "<affectation>",
    11: "<test>",
    12: "<condition>",
    13: "<operateur>",
    14: "<operateur>",
    15: "<operateur>",
}

class Regle:
    def __init__(self, g) -> None:
        self.partie_gauche = g
        self.partie_droite = []

    def ajouter_a_droite(self, s):
        self.partie_droite.append(s)

    def get_partie_gauche(self):
        return self.partie_gauche

    def get_partie_droite(self):
        return self.partie_droite

    def set_partie_gauche(self, g):
        self.partie_gauche = g

    def set_partie_droite(self, d):
        self.partie_droite = d

    def afficher(self):
        print('{} ::= {}'.format(self.partie_gauche, self.partie_droite))


class Grammaire:
    def __init__(self) -> None:
        self.regles = []
        pass

    def ajouter_regle(self, regle):
        self.regles.append(regle)

    def get_regles(self):
        return self.regles

    def afficher(self):
        for l in self.regles:
            l.afficher()




table_analyse = [
    [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 2, -1, -1, -1, 2, -1, -1, -1, -1,  2, -1, 2],
    [-1, -1, 3, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 4, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, 5],
    [-1, 6, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,-1],
    [-1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1,10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1,11, -1, -1, -1, -1, -1, -1, -1],
    [-1,12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1,13, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1,14, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,15, -1, -1, -1],
]



def gen_grammaire() -> Grammaire:
    # variable
    g =  Grammaire()

    # liste des regles
    # r0 ::= main(){<liste_declarations><liste_instructions>}
    r0 = Regle(non_terminaux.get(0))
    r0.ajouter_a_droite(terminaux.get(0))
    r0.ajouter_a_droite(terminaux.get(13))
    r0.ajouter_a_droite(non_terminaux.get(1))
    r0.ajouter_a_droite(non_terminaux.get(4))
    r0.ajouter_a_droite(terminaux.get(10))
    g.ajouter_regle(r0)

    # r1 ::= <une_declaration><liste_declarations>
    r1 = Regle(non_terminaux.get(1))
    r1.ajouter_a_droite(non_terminaux.get(3))
    r1.ajouter_a_droite(non_terminaux.get(1))
    g.ajouter_regle(r1)

    # r2 ::= vide
    r2 = Regle(non_terminaux.get(2))
    r2.ajouter_a_droite(terminaux.get(12))
    g.ajouter_regle(r2)

    # r3 ::= <type>id
    r3 = Regle(non_terminaux.get(3))
    r3.ajouter_a_droite(non_terminaux.get(8))
    r3.ajouter_a_droite(terminaux.get(1))
    g.ajouter_regle(r3)

    # r4 ::= <une_instruction><liste_instructions>
    r4 = Regle(non_terminaux.get(4))
    r4.ajouter_a_droite(non_terminaux.get(6))
    r4.ajouter_a_droite(non_terminaux.get(4))
    g.ajouter_regle(r4)

    # r5 ::= <liste_instructions>
    r5 = Regle(non_terminaux.get(5))
    r5.ajouter_a_droite(terminaux.get(12))
    g.ajouter_regle(r5)

    # r6 ::= <une_instruction>
    r6 = Regle(non_terminaux.get(6))
    r6.ajouter_a_droite(non_terminaux.get(10))
    g.ajouter_regle(r6)

    # r7 ::= <une_instruction>
    r7 = Regle(non_terminaux.get(7))
    r7.ajouter_a_droite(non_terminaux.get(11))
    g.ajouter_regle(r7)

    # r8 ::= <type>
    r8 = Regle(non_terminaux.get(8))
    r8.ajouter_a_droite(terminaux.get(2))
    g.ajouter_regle(r8)

    # r9 ::= <type>
    r9 = Regle(non_terminaux.get(9))
    r9.ajouter_a_droite(terminaux.get(3))
    g.ajouter_regle(r9)

    # r10 ::= id=nombre
    r10 = Regle(non_terminaux.get(10))
    r10.ajouter_a_droite(terminaux.get(1))
    r10.ajouter_a_droite(terminaux.get(9))
    r10.ajouter_a_droite(terminaux.get(4))
    g.ajouter_regle(r10)

    # r11 ::= if<condition><une_instruction>else<une_instruction>
    r11 = Regle(non_terminaux.get(11))
    r11.ajouter_a_droite(terminaux.get(5))
    r11.ajouter_a_droite(non_terminaux.get(12))
    r11.ajouter_a_droite(non_terminaux.get(6))
    r11.ajouter_a_droite(terminaux.get(6))
    r11.ajouter_a_droite(non_terminaux.get(6))
    g.ajouter_regle(r11)

    # r12 ::= id<operteur>nombre
    r12 = Regle(non_terminaux.get(12))
    r12.ajouter_a_droite(terminaux.get(1))
    r12.ajouter_a_droite(terminaux.get(13))
    r12.ajouter_a_droite(terminaux.get(4))
    g.ajouter_regle(r12)

    # r13 ::= <
    r13 = Regle(non_terminaux.get(13))
    r13.ajouter_a_droite(terminaux.get(7))
    g.ajouter_regle(r13)

    # r14 ::= >
    r14 = Regle(non_terminaux.get(14))
    r14.ajouter_a_droite(terminaux.get(8))
    g.ajouter_regle(r14)

    # r15 ::= =
    r15 = Regle(non_terminaux.get(15))
    r15.ajouter_a_droite(terminaux.get(9))
    g.ajouter_regle(r15)

    return g




def get_key_of_value(chaine):
    for key, value in terminaux.items():
        if chaine == value : return key

    for key, value in non_terminaux.items():
        if chaine == value : return key

    return None


def analyseur(chaine):
    grammaire = gen_grammaire()
    # Une pile : initialisee a l'axiome P
    print("chaine à analyser: ", end ='')
    print("".join(chaine))
    pile = ['$', non_terminaux.get(0)]
    err_s = False
    ch_ok = False
    while err_s == False and ch_ok == False:
    # sommet de pile
        x = pile[-1]
        i = get_key_of_value(chaine[0])

        if x in non_terminaux.values() and i is not None:
            indices = []
            for key, value in non_terminaux.items():
                if x == value:
                    indices.append(key)

            for c in indices: 
                if table_analyse[c][i] != -1:
                    nr = table_analyse[c][i]
                    pile.pop()
                    r = grammaire.regles[nr]
                    # ajout des regles dans la pile
                    pile.extend(r.partie_droite[::-1])
                    # emettre en sortie la rgle
                    r.afficher()
                    break
            indices.clear()
        else:
            if x == '$':
                if chaine[0] == '$':
                    print("la chaine acceptée")
                    ch_ok = True
                    break
                else:
                    print("Erreur de syntaxe 1")
                    err_s = True
                    break
            else:
                if x == chaine[0]:
                    pile.pop()
                    # on passe au symbole suivant
                    del chaine[0]
                elif x == 'vide': # on ignore la chaine vide
                    pile.remove(x)
                    continue
                else:
                    print("Erreur de syntaxe 2")
                    err_s = True
                    break
    return err_s, ch_ok



if __name__  == '__main__':


    # chaine a analyser
    chaine1 = ["main()", "{", "}", "$"]
    chaine6 = ["main()", "{","int", "id", "$"]
    chaine = ["main()", "{","int", "id","}",  "$"]
    chaine3 = ["main()", "{","if", "id", "<", "nombre", "id", "nombre", ";", "else", "id", "=", "nombre", ";", "}","$"]

    analyseur(chaine)
    print("ok")

print("ok")
