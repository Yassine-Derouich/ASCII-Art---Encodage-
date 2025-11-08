#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    



    liste_caracteres = [s[0]]
    liste_occurences = [1]

    for i in s[1:]:
        if i == liste_caracteres[-1]:
            liste_occurences[-1] += 1
        else:
            liste_caracteres.append(i)
            liste_occurences.append(1)

    resultat = list(zip(liste_caracteres,liste_occurences))

    return resultat


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    if s == "":
        return []

    premier = s[0]
    compteur = 1
    while compteur < len(s) and s[compteur] == premier:
        compteur += 1

    tuple_courant = (premier, compteur)

    reste = s[compteur:]
    return [tuple_courant] + artcode_r(reste)

    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
