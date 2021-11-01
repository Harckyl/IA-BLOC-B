import Csp
import arbre_constraint
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

 
  


racine = arbre_constraint.Arbre_contrainte(35)

racine.construct_fils()
    


test = 0
for test in range(racine.get_nb_enfant()):
    print(racine.get_enfant(test).get_valeur())

