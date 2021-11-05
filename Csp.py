from typing import Dict
import numpy as np
import arbre_constraint as arb
class CSP():
    Domain = [1,2,3,4,5,6,7,8,9]
    def __init__(self,mode_voulu,board):
        self.mode_voulu = mode_voulu
        self.base_sudoku = board
        self.assignement = board
        self.unassigned_variable = [[board[i][j] == 0 for i in range(9)] for j in range(9)]
        self.print_board(self.base_sudoku)
        self.compteur = 0
        self.finish = 0
        self.contrainte = []
        self.update_contrainte()

        #self.arbre_constraint
        #self.dictionnary_constraint

    def launch_csp(self):
        if (self.mode_voulu == 0):
            #backtracking search
            dosomething = 0
        elif (self.mode_voulu == 1):
            #MRV
            dosomething = 0
        elif (self.mode_voulu == 2):
            #degree heuristic
            dosomething = 0
        elif (self.mode_voulu == 3):
            #leastconstrainingvalue
            dosomething = 0
        elif (self.mode_voulu == 4):
            #AC3
            dosoemthing = 0

        return 0
    
    def update_contrainte(self):
        self.contrainte.clear()
        for x in range(9):
            for y in range(9):
                if (self.assignement[x][y] == 0):
                    node = arb.Arbre_contrainte(y + 10 * x)
                    node.construct_fils_reverse(self.assignement, y, x)
                    variable_domain = self.Domain.copy()
                    #print(" Position : ", x , y)
                    for enfant in node.get_all_enfant():
                        #print(enfant.get_valeur(), ' / ')
                        i = enfant.get_valeur() % 10
                        j = (int) (enfant.get_valeur() / 10)
                        valeur_contrainte = self.assignement[j][i]
                        if (valeur_contrainte in variable_domain):
                            variable_domain.remove(valeur_contrainte)
                    tuple = (x, y, variable_domain)
                    self.contrainte.append(tuple) 
        self.contrainte = sorted(self.contrainte, key=lambda tup: len(tup[2]))

    def print_board(self, bo):
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
        print()



    def check(self,x,y,value):
        for i in range(0,9):
            if self.assignement[x][i] == value:
                return False
        for j in range(0,9):
            if self.assignement[j][y] == value:
                return False
        xx = (x//3)*3
        yy = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if self.assignement[xx+i][yy+j] == value:
                    return False
        return True

    def resolve(self):
        if (self.mode_voulu == 0): ##if we use only the backtracking search
            self.compteur += 1
            for x in range(9):
                for y in range(9):
                    if self.assignement[x][y] == 0:
                        for value in self.Domain:
                            if self.check(x,y,value):
                                self.assignement[x][y] = value
                                self.resolve()
                                self.assignement[x][y] = 0
                        return
        if(self.mode_voulu == 3): ##if we use the least constraining value
            self.compteur += 1
            for x in range(9):
                for y in range(9):
                    if self.assignement[x][y] == 0: ##doit trier les valeurs des variables possibles pour pouvoir loop dessus dans le bon ordre
                        Dictionnaire = self.DictLCV(x,y)
                        while Dictionnaire != {}:
                            val = min(Dictionnaire, key=Dictionnaire.get)
                            self.assignement[x][y] = int(val)
                            del Dictionnaire[val]
                            self.resolve()
                            self.assignement[x][y] = 0
                        return
        if (self.mode_voulu == 1): ##if we use only the backtracking search
            self.compteur += 1
            variables = self.Dictionnaire_degree_heuristic()
            if(variables != []):
                for variable in variables:
                    y = variable[0] % 10
                    x = (int) (variable[0] / 10)
                    for value in self.Domain:
                        if self.check(x,y,value):
                            self.assignement[x][y] = value
                            self.resolve()
                            if (self.finish == 1):
                                return
                            self.assignement[x][y] = 0
                    return
        if (self.mode_voulu == 2): ##if we use only the backtracking search
            self.compteur += 1
            for x in range(9):
                for y in range(9):

                    if self.assignement[x][y] == 0:
                        self.update_contrainte()                    
                        if (len(self.contrainte[0][2]) == 1):
                            
                            col = self.contrainte[0][0]
                            ligne = self.contrainte[0][1]
                            self.assignement[col][ligne] = self.contrainte[0][2][0]
                            
                        if (self.contrainte[0][2] == []):
                            return
                        for value in self.contrainte[0][2]:
                                self.assignement[col][ligne] = value
                                self.resolve()
                                self.assignement[col][ligne] = 0
                        return
        self.print_board(self.assignement)
        print(self.compteur)
        self.finish = 1

     


    def DictLCV(self,x,y): ##pour passer les valeurs dans un dictionnaire avec en valeur leurs nombres d'occurence
        dictionnaire = {}
        for val in self.Domain:
            
            if self.check(x,y,val):
                compteur = 0
                for i in range(0,9):
                    if self.assignement[x][i] == 0 and self.check(x,i,val):
                        compteur += 1
                for j in range(0,9):
                    if self.assignement[j][y] == 0 and self.check(j,y,val):
                        compteur += 1
                xx = (x//3)*3
                yy = (y//3)*3
                for i in range(0,3):
                    for j in range(0,3):
                        if self.assignement[xx+i][yy+j] == 0 and self.check(xx+i,yy+j,val):
                            compteur += 1
                
                dictionnaire[str(val)] = compteur
                

        return dictionnaire



    def Dictionnaire_degree_heuristic(self):
      tab = []
      for x in range(9):
         for y in range(9):
            if(self.assignement[x][y] == 0):
               variable = arb.Arbre_contrainte(y + 10 * x)
               variable.construct_fils(self.assignement,variable.valeur % 10, (int) (variable.valeur / 10))
               tab.append(tuple([variable.valeur, variable.get_nb_enfant()]))
      tab = sorted(tab, key=lambda tup: tup[1])
      if (tab != []):
        return tab
      else:
        return []
