#   fonction permettant de saisir deux nombres
def Saisie():
  x = int(input('saisir le nombre que vous devez élever en puissance\n\n\t\t'))
  n = int(input('saisir le nombre entier qui représente la puissance\n\n\t\t'))
  while(n<0):
    n = int(input('saisir le nombre entier qui représente la puissance\n\n\t\t'))
  return [x,n]

