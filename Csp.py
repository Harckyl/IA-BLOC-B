class CSP():
    Domain = [1,2,3,4,5,6,7,8,9]
    def __init__(self,mode_voulu,board):
        self.mode_voulu = mode_voulu
        self.base_sudoku = board
        self.assignement = board
        self.unassigned_variable = [[board[i][j] == 0 for i in range(9)] for j in range(9)]
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