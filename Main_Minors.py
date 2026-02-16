'''
Created on February 15, 2026
@author: P. Proutiere - R. Alexis - L. Adan
'''
import random as r

def matrice(x,y):
    tab = [[0 for _ in range(y)] for _ in range(x)]
    return tab

def level(choix_user):
    if choix_user == 1:
        x, y=9, 9
    elif choix_user == 2:
        x, y=16, 16
    elif choix_user == 3:
        x, y=16, 32
    return matrice(x,y)

def placement_bombe(matrice):
    if len(matrice[0])==9:
        for _ in range(10):
            matrice[r.randint(0,8)][r.randint(0,8)] = 'X'
    elif len(matrice[0])==16:
        for _ in range(40):
            matrice[r.randint(0, 15)][r.randint(0, 15)] = 'X'
    elif len(matrice[0])==32:
        for _ in range(100):
            matrice[r.randint(0, 15)][r.randint(0, 31)] = 'X'
    return matrice

def num_bombes(matrice):
    for i in range(1,len(matrice)-1):  #tout faire, sauf la première et la dernière ligne
        for j in range(1,len(matrice[i])-1):  #tout faire, suaf le début et la fin de chaque ligne
            if matrice[i][j] == 'X':  #si la case est une bombe faire
                for k in range(3):
                    if matrice[i-1][j-1+k] == 'X':  #si la case du dessu est une bombe, passer
                        pass
                    else :  #sinon, ajouter 1 à la valeure à côté
                        matrice[i-1][j-1+k] += 1
                if matrice[i][j-1] == 'X':  #idem pour la case gauche sur la même ligne
                    pass
                else:
                    matrice[i][j-1] += 1
                if matrice[i][j + 1] == 'X':  #et pour la case à droite
                    pass
                else:
                    matrice[i][j + 1] += 1
                for k in range(3):
                    if matrice[i + 1][j - 1 + k] == 'X':  #et pour finir, la ligne du dessous
                        pass
                    else:
                        matrice[i + 1][j - 1 + k] += 1

    return matrice

print(*num_bombes(placement_bombe(level(3))),sep='\n')