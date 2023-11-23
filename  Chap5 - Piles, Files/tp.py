from ds import Chapeau, Pile
from ds import Bonhomme, File

def init_piles():
    p1 = Pile()
    p1.empiler(Chapeau(1))
    p1.empiler(Chapeau(2))
    p1.empiler(Chapeau(3))
    p1.empiler(Chapeau(4))
    p1.empiler(Chapeau(5))
    p2 = Pile()
    p2.empiler(Chapeau(2))
    p2.empiler(Chapeau(1))
    p2.empiler(Chapeau(5))
    p2.empiler(Chapeau(3))
    p2.empiler(Chapeau(4))
    p3 = Pile()
    p3.empiler(Chapeau(4))
    p3.empiler(Chapeau(5))
    p3.empiler(Chapeau(1))
    p3.empiler(Chapeau(2))
    p3.empiler(Chapeau(3))
    p4 = Pile()
    p4.empiler(Chapeau(5))
    p4.empiler(Chapeau(4))
    p4.empiler(Chapeau(3))
    p4.empiler(Chapeau(2))
    p4.empiler(Chapeau(1))
    # ...
    # À compléter
    return p1, p2, p3, p4

def init_files():
    f1 = File()
    f1.enfiler(Bonhomme(1))
    f1.enfiler(Bonhomme(2))
    f1.enfiler(Bonhomme(3))
    f1.enfiler(Bonhomme(4))
    f1.enfiler(Bonhomme(5))
    f2 = File()
    f2.enfiler(Bonhomme(5))
    f2.enfiler(Bonhomme(4))
    f2.enfiler(Bonhomme(3))
    f2.enfiler(Bonhomme(2))
    f2.enfiler(Bonhomme(1))
    f3 = File()
    f3.enfiler(Bonhomme(4))
    f3.enfiler(Bonhomme(3))
    f3.enfiler(Bonhomme(5))
    f3.enfiler(Bonhomme(1))
    f3.enfiler(Bonhomme(2))
    f4 = File()
    f4.enfiler(Bonhomme(3))
    f4.enfiler(Bonhomme(2))
    f4.enfiler(Bonhomme(1))
    f4.enfiler(Bonhomme(5))
    f4.enfiler(Bonhomme(4))

    return f1, f2, f3, f4

def compatibles(p, f):
    """ Pile, File -> Bool
    Détermine si les chapeaux sont associés aux bon bonshommes """
    # for chap in p:
    while not p.est_vide():
        b = f.defiler()
        c = p.depiler()
        if b.content(c) == False:
            return False
    return True

# p1,p2,p3, p4 = init_piles()
# f1,f2, f3, f4 = init_files()
# p1.affiche()
# f1.affiche()
# print(compatibles(p1, f1))

def restaure_pile(p, p_aux):
    """ Pile, Pile -> Nonetype
    Restaure p à son état initial lorsque les dépilements successifs
    on été empilés dans p_aux. """
    # vide p dans p_aux
    while not p.est_vide():
        c = p.depiler()
        p_aux.empiler(c)
    # vide p_aux dans p
    while not p_aux.est_vide():
        c = p_aux.depiler()
        p.empiler(c)

def restaure_file(f, f_aux):
    """ File, File -> Nonetype
    Restaure f à son état initial lorsque les défilement successifs
    on été enfilés dans f_aux. """
    # on vide f dans f_aux
    while not f.est_vide():
        b = f.defiler()
        f_aux.enfiler(b)
    while not f_aux.est_vide():
        b = f_aux.defiler()
        f.enfiler(b)

def compatibles2(p, f):
    """ Pile, File -> Bool
    Détermine si les chapeaux sont associés aux bons bonshommes
    L'état de la pile p et la file f sera le même avant et après exécution """
    p_aux = Pile()
    f_aux = File()
    while not p.est_vide():
        b = f.defiler()
        f_aux.enfiler(b)
        c = p.depiler()
        p_aux.empiler(c)
        if b.content(c) == False:
            restaure_pile(p, p_aux)
            restaure_file(f, f_aux)
            return False
    restaure_pile(p, p_aux)
    restaure_file(f, f_aux)
    return True

p1,p2,p3, p4 = init_piles()
f1,f2, f3, f4 = init_files()
p1.affiche()
f1.affiche()
print(compatibles2(p1, f1))
p1.affiche()
f1.affiche()

def solution():
    """ () -> [(int, int)]
    Renvoie la liste des associations pile i <-> file j """
    piles = init_piles()
    files = init_files()
    sol = []
    pass

def arrivee_rampe(profondeur):
    """ [int] -> [int]
    Détermine l'ordre d'arrivée des boules numérotées de 1 à 10 """
    rampe_lancement = File()
    for b in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        ... # à compléter
    piles = [Pile(max_elt = p) for p in profondeur] # liste de piles bornées, dans l'ordre du parcours.
    rampe_finale = File() # billes dans l'ordre d'arrivée
    numero_pile = 0 # indice de la pile à remplir
    
    # on remplit les piles dans l'ordre dans lequel elles sont positionnées
    # sur le parcours tant que cela est possible (c'est à dire tant que
    # la dernière pile du parcours n'est pas vide)
    # Si la pile que l'on cherche à remplir est pleine,
    # alors il faut commencer par changer le numéro de la pile à remplir. 
    # On empile une bille prise depuis la rampe de lancement sur la pile à remplir.
    while ...:
        ... # à compléter
        
    # Toutes les billes restantes roulent directement dans la rampe d'arrivée.
    while ...:
        ... # à compléter
  
    # On retire les ressorts dans l'ordre dans lesquels ils sont positionnés
    # sur le parcours. Les billes ressortent des trous et viennent s'accumuler
    # sur la rampe de lancement.
    for p in piles:
        while ...:
            ... # à compléter

    return rampe_finale

