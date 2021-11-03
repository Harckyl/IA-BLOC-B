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





  


racine = arbre_constraint.Arbre_contrainte(35)

racine.construct_fils()
    


test = 0
for test in range(racine.get_nb_enfant()):
    print(racine.get_enfant(test).get_valeur())

csp = Csp.CSP(3, board)
csp.resolve()