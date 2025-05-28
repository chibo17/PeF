
def permutations(lst):
    if len(lst)==0:
        return [[]]  
    result = []
    for i in range(len(lst)):
        rest = lst[:i]+lst[i+1:]
        rest_perms = permutations(rest)
        for p in rest_perms:
            result.append([lst[i]]+p)
    return result

def perms_backtrack(lst, current=[]):
    if len(lst)==0:
        print(current)
        return
    for i in range(len(lst)):
        rest = lst[:i]+lst[i+1:]
        perms_backtrack(rest, current+[lst[i]])
    return


def check_queens(perm):
    positions = list(enumerate(perm))  
    for i, j in positions:
        for k, l in positions:
            if i<k and (i+j == k+l or i-j == k-l):
                return False
    return True

def nQueens(n):
    count_solutions = 0
    pos = list(range(n))
    for p in permutations(pos):
        if check_queens(p):
            count_solutions+=1
    return count_solutions

# ----------- preverjanje nazaj -------------

def nQueens_backtrack(lst, current=[]):
    if len(lst)==0:
        if check_queens(current):
            return 1
        return 0
    
    num_solutions = 0
    for i in range(len(lst)):
        rest = lst[:i]+lst[i+1:]
        if check_queens(current):
            num_solutions+= nQueens_backtrack(rest, current+[lst[i]])
    return num_solutions

#------------------ preverjanje naprej ---------

def set_non_comp(compatibility, i, j):
    n = len(compatibility)
    for k in range(n):
        compatibility[i][k] = False
        compatibility[k][j] = False
    for d in range(-n+1, n):
        if 0 <= i + d < n and 0 <= j + d < n:
            compatibility[i + d][j + d] = False
        if 0 <= i + d < n and 0 <= j - d < n:
            compatibility[i + d][j - d] = False

# samo pomožna funkcija za lažjo uporabo Nqueens_fc
def nQueens_aux(n):
    compatibility = [[True]*n for i in range(n)]
    return Nqueens_fc(0, n, compatibility)

def Nqueens_fc(i,n,compatibility):
    if i>= n:
        return 1
    else:
        num_solution = 0
        for j in range(n):
            if compatibility[i][j]:
                # kopiramo matriko
                new_compatibility = [row[:] for row in compatibility]  
                set_non_comp(new_compatibility, i, j)
                new_compatibility[i][j] = True
                num_solution+= Nqueens_fc(i + 1, n, new_compatibility)
        return num_solution