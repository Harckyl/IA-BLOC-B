class CSP():
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