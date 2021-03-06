# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""

def Joueur(nom):
    joueur={"nomjoueur" : nom , "listetresors" : []}

    return joueur
    """
      creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
      paramètre: nom une chaine de caractères
      retourne le joueur ainsi créé
    """


def ajouterTresor(joueur,tresor):
    if tresor not in joueur["listetresors"]:
      joueur["listetresors"].append(tresor)

    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
    joueur le joueur à modifier
    tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur
    """


def prochainTresor(joueur):
    try:
      return joueur["listetresors"][0]
    except:
      return None

    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
      joueur le joueur
    résultat un entier représentant le trésor ou None
    """


def tresorTrouve(joueur):
    del joueur["listetresors"][0]
    """ 
    enlève le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
    """


def getNbTresorsRestants(joueur):
    return len(joueur["listetresors"])
    """
    retourne le nombre de trésors qu'il reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """


def getNom(joueur):
    return joueur["nomjoueur"]
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur 
    """


if __name__=="__main__" :

  Michel=Joueur("Michel")
  print(Michel)
  
  ajouterTresor(Michel,"4")
  ajouterTresor(Michel,"5")
  ajouterTresor(Michel,"6")
  print(Michel["listetresors"])

  print(prochainTresor(Michel))

  tresorTrouve(Michel)
  print(Michel)

  print(getNbTresorsRestants(Michel))

  print(getNom(Michel))