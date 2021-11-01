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
   def __init__(self, valeur):
      self.valeur = valeur
      self.enfant = []
      self.parent = None

   def insert(self, valeur):
      if self.enfant != None:
         self.enfant.append(Arbre_contrainte(valeur))

   def get_valeur(self):
      return self.valeur
      

   def get_enfant(self, index):
      return self.enfant[index]

   def get_nb_enfant(self):
      return len(self.enfant)

   def return_enfant_value(self):
       tab = []
       for i in range (len(self.enfant)):
           tab.append(self.get_enfant(i).get_valeur())
       return tab
       
   def construct_fils(self):
       j = (int) (self.valeur / 10)
       i = self.valeur % 10
       carrex = i // 3
       carrey = j // 3

       for oui in range(carrex*3, carrex*3 + 3):
            for non in range(carrey * 3, carrey*3 + 3):
                if ((i, j) != (oui, non)):
                    self.insert(non * 10 + oui)

       mem = self.return_enfant_value()

       for increment in range(9):
            if (increment != j and (increment * 10 + i) not in mem):
                self.insert(increment * 10 + i)
            if (increment != i and (j * 10 + increment) not in mem):
                self.insert(j * 10 + increment)

def affiche(T):
   if T != None:
      return (T.get_valeur(),affiche(T.get_enfant()))
  


racine = Arbre_contrainte(15)

racine.construct_fils()
    


test = 0
for test in range(racine.get_nb_enfant()):
    print(racine.get_enfant(test).get_valeur())

