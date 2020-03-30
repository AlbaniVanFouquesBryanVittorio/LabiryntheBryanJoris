# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""

from matrice import *
from carte import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """

    nouveauPlateau=Matrice(7,7)
    setVal(nouveauPlateau,0,0,Carte(True,False,False,True,0,[1]))
    setVal(nouveauPlateau,0,2,Carte(True,False,False,False,0,[1,2,3,4]))
    setVal(nouveauPlateau,0,4,Carte(True,False,False,False,0,[3]))
    setVal(nouveauPlateau,0,6,Carte(True,True,False,False))
    setVal(nouveauPlateau,2,0,Carte(False,False,False,True))
    setVal(nouveauPlateau,2,2,Carte(False,False,False,True))
    setVal(nouveauPlateau,2,4,Carte(True,False,False,False))
    setVal(nouveauPlateau,2,6,Carte(False,True,False,False))
    setVal(nouveauPlateau,4,0,Carte(False,False,False,True))
    setVal(nouveauPlateau,4,2,Carte(False,False,True,False))
    setVal(nouveauPlateau,4,4,Carte(False,True,False,False))
    setVal(nouveauPlateau,4,6,Carte(False,True,False,False))
    setVal(nouveauPlateau,6,0,Carte(False,False,True,True))
    setVal(nouveauPlateau,6,2,Carte(False,False,True,False))
    setVal(nouveauPlateau,6,4,Carte(False,False,True,False))
    setVal(nouveauPlateau,6,6,Carte(False,True,True,False))
  
    L=creerCartesAmovibles(1,nbTresors) 

    #Ajoute chaque carte une à une dans le plateau où il y a un zero
    for x in range(getNbLignes(nouveauPlateau)):
      for y in range(getNbColonnes(nouveauPlateau)):
         if nouveauPlateau[x][y]==0:
           setVal(nouveauPlateau,x,y,L[0])
           L.pop(0)
    
    #réparti les trésors aléatoirement sur les cartes 
    ListeTrésor=[]
    
    for i in range(1,nbTresors):
      ListeTrésor.append(i)

    while len(ListeTrésor)!=0:
      
      ListeTrésor.pop(0)

    
    print('ListeTre',ListeTrésor)     
    
    return nouveauPlateau


def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    Dcarte={'Angle':16,'Jonction':6,'Droit':12}
    ListeCarteA=[]
    i=0
    x=random.randint(0,2)

    while i<34:
      if x==0:
        c=Carte(True,False,False,True)
        tourneAleatoire(c)
        ListeCarteA.append(c)
        y=Dcarte['Angle']
        Dcarte['Angle']=y-1
        if Dcarte['Angle']==0:
          if Dcarte['Jonction']==0:
            x=2
          elif Dcarte['Droit']==0:
            x=1
          else:
            x=random.randint(1,2)
        i=i+1

      elif x==1:
        c=Carte(True,False,False,False)
        tourneAleatoire(c)
        ListeCarteA.append(c)
        y=Dcarte['Jonction']
        Dcarte['Jonction']=y-1
        if Dcarte['Jonction']==0:
          if Dcarte['Angle']==0:
            x=2
          elif Dcarte['Droit']==0:
            x=0
          else:
            x=random.randrange(0,1,2)
        i=i+1

      elif x==2:
        c=Carte(True,False,True,False)
        tourneAleatoire(c)
        ListeCarteA.append(c)
        y=Dcarte['Droit']
        Dcarte['Droit']=y-1
        if Dcarte['Droit']==0:
          if Dcarte['Angle']==0:
            x=1
          elif Dcarte['Jonction']==0:
            x=0
          else:
            x=random.randint(0,1)
        i=i+1
      
    return ListeCarteA


def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """

    carte=getVal(plateau,lig,col)
    if numTresor==getTresor(carte):
        prendreTresor(carte)


def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    for lig in range(getNbLignes(plateau)):
      for col in range(getNbColonnes(plateau)):
        if getTresor(plateau[lig][col])==numTresor:
          return (lig,col)
    return None

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    for lig in range(getNbLignes(plateau)):
      for col in range(getNbColonnes(plateau)):
        if possedePion(plateau[lig][col],numJoueur):
          return (lig,col)
    return None

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    carte=getVal(plateau,lin,col)
    if possedePion(carte,numJoueur):
      prendrePion(carte,numJoueur)
      

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    carte=getVal(plateau,lin,col)
    poserPion(carte,numJoueur)
    pass


def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """

      
    carte1=(plateau[ligD][colD])
    carte2=(plateau[ligA][colA])

    while carte1!=carte2:
      carte3=(plateau[ligD][colD+1])
      if passageNord(carte1,carte3):        
        carte1=(plateau[ligD][colD+1])
      else:
        carte3=(plateau[ligD][colD-1])

        carte3=(plateau[ligD][colD-1])
        if passageSud(carte1,carte3):        
          carte1=(plateau[ligD][colD-1])
        else:
          carte3=(plateau[ligD][colD+1])
      
          carte3=(plateau[ligD+1][colD])
          if passageOuest(carte1,carte3):        
            carte1=(plateau[ligD+1][colD])
          else:
            carte3=(plateau[ligD-1][colD])
      
            carte3=(plateau[ligD-1][colD])
            if passageEst(carte1,carte3):        
              carte1=(plateau[ligD-1][colD])
            else:
              carte3=(plateau[ligD+1][colD])
      
      
      pass

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass

if __name__=="__main__" :
  p=Plateau(2,20)
  #print(creerCartesAmovibles(1,5))
  print(p[0][2+1])
  prendreTresorPlateau(p,0,0,1)

  print(getCoordonneesTresor(p,2))

  print(getCoordonneesJoueur(p,3))

  prendrePionPlateau(p,0,2,5)
  print(p[0][2])

  poserPionPlateau(p,0,2,3)
  print(p[0][2])