'''
Created on February 15, 2026
@author: P. Proutiere - R. Alexis - L. Adan
'''
import random as r


def matrice(x,y):
    grille = [[0 for _  in range(y)] for _ in range(x)]
    return grille

def level(choix_user):
    if choix_user == 1:
        grille = matrice(9,9)
    elif choix_user == 2:
        grille = matrice(16,16)
    elif choix_user == 3:
        grille = matrice(16,32)
    else:
        return 'error during level selector'
    return grille

def place(grille,choix_user):
    if choix_user == 1:
        for _ in range(10):
            grille[r.randint(0,8)][r.randint(0,8)]='X'
    if choix_user == 2:
        for _ in range(40):
            grille[r.randint(0,15)][r.randint(0,15)]='X'
    if choix_user == 3:
        for _ in range(100):
            grille[r.randint(0,15)][r.randint(0,31)]='X'
    return grille

print(*place(level(2),2),sep='\n')