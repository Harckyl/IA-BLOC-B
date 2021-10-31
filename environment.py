import Csp
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]




#fonctionnement = variable = 1 ==> tableau[0][1]
#variable = 10 ==> tableau[1][0]
variable = 87

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])


            else:
                print(str(bo[i][j]) + " ", end="")

print_board(board)

 

class Arbre_contrainte:
   def __init__(self, valeurx, valeury):
      self.valeurx = valeurx 
      self.valeury = valeury
      self.enfant = []
      self.parent = None

   def insert(self, valeurx, valeury):
      if self.enfant != None:
         self.enfant.append(Arbre_contrainte(valeurx, valeury))

   def get_valeurx(self):
      return self.valeurx
      
   def get_valeury(self):
      return self.valeury

   def get_enfant(self, index):
      return self.enfant[index]

   def get_nb_enfant(self):
      return len(self.enfant)


def affiche(T):
   if T != None:
      return (T.get_valeur(),affiche(T.get_enfant()))
  
i = 5
j = 1

tmp = j * 10

racine = Arbre_contrainte(i, j)


carrex = i // 3
carrey = j // 3


for oui in range(carrex*3, carrex*3 + 3):
    for non in range(carrey * 3, carrey*3 + 3):
        if ((i, j) != (oui, non)):
            racine.insert(non, oui)

for increment in range(9):
    if (increment != j):
        racine.insert(increment, i)
    if (increment != i):
        racine.insert(j, increment)
    


test = 0
for test in range(racine.get_nb_enfant()):
    print(racine.get_enfant(test).get_valeurx(), racine.get_enfant(test).get_valeury())

