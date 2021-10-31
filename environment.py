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

assignement = board 

unassigned_variables = [[0 for i in range(9)] for i in range(9)]

Domain = [1,2,3,4,5,6,7,8,9]

#fonctionnement = variable = 1 ==> tableau[0][1]
#variable = 10 ==> tableau[1][0]
variable = 77

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
                if bo[i][j] == 0:
                    unassigned_variables[i][j] = 1 
                else:
                    unassigned_variables[i][j] = 0

            else:
                print(str(bo[i][j]) + " ", end="")
                if bo[i][j] == 0:
                    unassigned_variables[i][j] = 1 
                else:
                    unassigned_variables[i][j] = 0

print_board(assignement)
print("")
print_board(unassigned_variables)

def check_constraint(assignement, value, variable):
    i = (int) (variable / 10)
    j = variable % 10
    for test in range(len(assignement)):
        #check ligne
        if (assignement[i][test] == value and i != test):
            return False
        #check colonne
        if (assignement[test][j] == value and i != test):
            return False
        #check boite 
        carre_x = i // 3
        carre_y = j // 3
        for oui in range(carre_y*3, carre_y*3 + 3):
            for non in range(carre_x * 3, carre_x*3 + 3):
                 if assignement[oui][non] == value and (oui, non) != (i, j):
                     return False
    return True
 

test = check_constraint(assignement, 9, variable)
print(test)