#2024 sujet 37

#exercice 1
def moyenne(tab):
    if len(tab) == 0:
        return "Le tableau est vide"
    else:
        somme = 0
        for element in tab:
            somme += element
        return somme / len(tab)


#exercice 2
def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0  # premier indice de la zone non triée
    j = len(tab) - 1  # dernier indice de la zone non triée
    while i < j:
        if tab[i] == 0:
            i += 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j -= 1

