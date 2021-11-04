import numpy as np
import math

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


Domain = [1,2,3,4,5,6,7,8,9]
assignement = board
unassigned_variable = [[board[i][j] == 0 for i in range(9)] for j in range(9)]



def mrv_domains(assignement):
    domains = {}
    for i in range(len(assignement)):
        for j in range(len(assignement)):
            if assignement[i][j] == 0:
                domains[i, j] = set(range(1, len(assignement) + 1))

    squareRoot = int(math.sqrt(len(assignement)))

    for i in range(len(assignement)):
        for j in range(len(assignement)):
            if type(assignement[i][j]) is not set:
                qs = range(squareRoot)
                grid_i = int(i / squareRoot)
                grid_i_set = {grid_i * squareRoot + q for q in qs}
                grid_j = int(j / squareRoot)
                grid_j_set = {grid_j * squareRoot + q for q in qs}

                for k in domains.keys():
                    # Are in same row or in same column or in same block
                    if k[0] == i or k[1] == j or (k[0] in grid_i_set and k[1] in grid_j_set):
                        domains[k].discard(assignement[i][j])

    min_val = None;
    for domain in domains.values():
        if min_val is not None:
            min_val = min(min_val, len(domain))
        else:
            min_val = len(domain)

    # Sudoku can't be solved
    if min_val == 0:
        return None

    mins = {k: domains[k]
                   for k in domains.keys()
                   if len(domains[k]) == min_val}

    return mins


def var_finder(assignement):
    mins = mrv_domains(assignement)

    if not mins:
        return None, None, None

    variable = mins.popitem()
    return variable[0][0], variable[0][1], variable[1]



def value_is_consistent(assignement, var_i, var_j, val):
    # Check row
    for var in assignement[var_i]:
        if var != 0 and var == val:
            return False

    # Check column
    for row in assignement:
        if row[var_j] != 0 and row[var_j] == val:
            return False

    # Check block
    sqrt_n = int(math.sqrt(len(assignement)))
    grid_i = int(var_i / sqrt_n)
    grid_j = int(var_j / sqrt_n)
    qs = range(sqrt_n)
    for i in [grid_i * sqrt_n + q for q in qs]:
        for j in [grid_j * sqrt_n + q for q in qs]:
            if (i, j) != (var_i, var_j) and assignement[i][j] != 0 and sudoku[i][j] == val:
                return False

    return True

def assignement_done(assignement):
    for line in assignement:
        for digit in line:
            if digit == 0:
                return False
    return True

def backtracking_search(assignement):
    if assignement_done(assignement):
        return assignement

    var_i, var_j, domain = var_finder(assignement)

    for val in domain:
        assignement[var_i][var_j] = val
        res = backtracking_search(assignement)
        if res:
            return res
        assignement[var_i][var_j] = 0



print(np.matrix(assignement))
print("")
backtracking_search(assignement)
print(np.matrix(assignement))
