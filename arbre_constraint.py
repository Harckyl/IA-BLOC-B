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

   def get_all_enfant(self):
      return self.enfant

   def get_nb_enfant(self):
      return len(self.enfant)

   def return_enfant_value(self):
       tab = []
       for i in range (len(self.enfant)):
           tab.append(self.get_enfant(i).get_valeur())
       return tab
       
   def construct_fils(self, board, i, j):
       carrex = i // 3
       carrey = j // 3

       for oui in range(carrex*3, carrex*3 + 3):
            for non in range(carrey * 3, carrey*3 + 3):
                if ((i, j) != (oui, non) and board[non][oui] == 0):
                    self.insert(non * 10 + oui)

      

       for increment in range(9):
            mem = self.return_enfant_value()
            if (increment != j and (increment * 10 + i) not in mem and board[increment][i] == 0):
               self.insert(increment * 10 + i)
            if (increment != i and (j * 10 + increment) not in mem and board[j][increment] == 0):
               self.insert(j * 10 + increment)
               
   def construct_fils_reverse(self, board, i, j):
       carrex = i // 3
       carrey = j // 3

       for oui in range(carrex*3, carrex*3 + 3):
            for non in range(carrey * 3, carrey*3 + 3):
                if ((i, j) != (oui, non) and board[non][oui] != 0):
                    self.insert(non * 10 + oui)

      

       for increment in range(9):
            mem = self.return_enfant_value()
            if (increment != j and (increment * 10 + i) not in mem and board[increment][i] != 0):
               self.insert(increment * 10 + i)
            if (increment != i and (j * 10 + increment) not in mem and board[j][increment] != 0):
               self.insert(j * 10 + increment)

def affiche(T):
   if T != None:
      return (T.get_valeur(),affiche(T.get_enfant()))