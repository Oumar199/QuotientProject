'''
  Objectif : Cette fonction demande à l'utilisateur de saisir deux nombres entiers
  Méthode : utilisation de fonction, boucles, liste et affectation de valeurs à des variables 
  Besoins : x pour le nombre et n pour la puissance 
  Sortie : x et n sous forme de liste
'''
def Saisie():
  x = int(input('saisir le nombre que vous devez élever en puissance\n\n\t\t'))
  n = int(input('saisir le nombre entier qui représente la puissance\n\n\t\t'))
  while(n<0):
    n = int(input('saisir le nombre entier qui représente la puissance\n\n\t\t'))
  return [x,n]

