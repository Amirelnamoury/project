class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit
    
    def affiche_arbre(r):
        def affiche_aux(r, n):
            if r is None:
                print('', end='')
            else:
                print(n*'-', str(r.etiquette))
                affiche_aux(r.gauche, n+1)
                affiche_aux(r.droit, n+1)
        affiche_aux(r, 0)

r2 = Noeud(9, None, None)
r3 = Noeud(2, Noeud(12, None, None), r2)
r1 = Noeud(1, Noeud(4, None, Noeud(3, None, None)), Noeud(5, Noeud(2, Noeud(12, None, None), Noeud(9, None, None)), Noeud(1, Noeud(7, None, None), None)))

r1.affiche_arbre()

r4 = Noeud(5, Noeud(2, Noeud(1, None, None), Noeud(7, None, None)), Noeud(1, None, None))

def affiche_arbre2(r):
    def affiche_aux(r, n):
        if r is None:
            print(*'-')
        else:
            print(n*'-', str(r.etiquette))
            affiche_aux(r.gauche, n+1)
            affiche_aux(r.droit, n+1)
    affiche_aux(r, 0)

arbre_test_affiche1 = Noeud(1, Noeud(1, None, None), None)
arbre_test_affiche2 = Noeud(1, None, Noeud(1, None, None))

print("3.1.1 : \n--- arbre_test_affiche1   affiche arbre ---")
arbre_test_affiche1.affiche_arbre()
print("--- arbre_test_affiche1   affiche arbre2 ---")
affiche_arbre2(arbre_test_affiche1)
print("--- arbre_test_affiche2   affiche arbre ---")
arbre_test_affiche2.affiche_arbre()
print("--- arbre_test_affiche2   affiche arbre2 ---")
affiche_arbre2(arbre_test_affiche2)

def creer_vide():
    return None
def est_vide(r):
    return r == None
print("\n 3.3 : est_vide")
print(est_vide(creer_vide()))
print(est_vide(r1))
print("\n 3.4 : propriétés du noeud")

def gauche(r):
    return r.gauche
def droit(r):
    return r.droit
def etiquette(r):
    return r.etiquette

affiche_arbre2(gauche(droit(r1)))

print("\n 3.5 : est_feuille")
def est_feuille(r):
    return droit(r) is None and gauche(r) is None
    #return est_vide(droit(r)) and est_vide(gauche(r))
print(est_feuille(r1))
print(est_feuille(r2))

print("\n 4.1 : Hauteur")
def hauteur(r):
    if est_vide(r):
        return 0
    else:
        h_droit = hauteur(droit(r))+1
        h_gauche = hauteur(gauche(r))+1
        if h_gauche > h_droit:
            return h_gauche
        return h_droit
print("r1(4) : ", hauteur(r1))

print("\n 4.2 : Taille")
def taille(r):
    if est_vide(r):
        return 0
    else:
        t_droit = taille(droit(r))
        t_gauche = taille(gauche(r))
        return t_droit+t_gauche +1
print("r1(9) : ", taille(r1))

print("\n 4.3 : Maximum")
def maximum_3(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
        
def maximum(r):
    if est_vide(r):
        return float("-inf")
    else:
        m_droit = maximum(droit(r))
        m_gauche = maximum(gauche(r))
        #maximum_3(r.etiquette, m_droit, m_gauche)

        if r.etiquette > m_droit and r.etiquette > m_gauche:
            return r.etiquette
        elif m_droit > r.etiquette and m_droit > m_gauche:
            return m_droit
        else:
            return m_gauche
print("r1(11) : ", maximum(r1))

print("\n 4.4 : Arbres particuliers -----")
print(" 2) est_peigne_gauche")
def est_peigne_gauche(r):
    """ determine si l'arbre de racine rest un peigne gauche"""
    if est_feuille(r):
        return True
    else:
        if est_vide(droit(r)):
            return est_peigne_gauche(r.gauche)
        else:
            return False

peigne_gauche = Noeud(1, Noeud(2, Noeud(3, None, None), None), None)
print("False :  ", est_peigne_gauche(r1))
print("True :  ", est_peigne_gauche(peigne_gauche))

print("\n 3) peigne_decroissant")
def peigne_decroissant(n):
    if n == 1:
        return Noeud(1, None, None)
    else:
        est_fils_gauche = Noeud(n, peigne_decroissant(n-1), None)
        return arbre
peigne_decroissant(5).affiche_arbre()

print("\n 4) peigne_croissant")


def peigne_croissant(n):
    def peigne_croissant2(n, i):
        if i == 0:
            return Noeud(n, None, None)
        else:
            arbre = Noeud(n-i, peigne_croissant2(n, i-1), None)
            return arbre
    return peigne_croissant2(n, n-1)


peigne_croissant(5).affiche_arbre()
print("\n 4.4.2 : arbre parfaits -----")



def arbre_parfait(n):
    if n == 1:
        return Noeud(1, None, None)
    else:
        arbre = Noeud(1, arbre_parfait(n-1), arbre_parfait(n-1))
        return arbre
arbre_parfait(3).affiche_arbre()

print("\n 4.5 : Enumeration des arbres")


def tous_arbres(n):
    if n == 1:
        liste =  [Noeud('x', None, None)]
        return liste
    else:
        tous_arbres.append(Noeud('x', tous_arbres[n-1], None))
        return tous_arbres.append(Noeud('x', tous_arbres[n-1], None))
print(len(tous_arbres(5)))