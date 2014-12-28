import random

# main body
def main():

    print "Size of tic-tac-toe board: "
    size = int(raw_input())

    if (size < 1):
        return

    print "Enter board information, X, O, and N."
    board = [[None] * size] * size

    for i in range(size):
        A = map(str, raw_input().split())
        assert (len(A) == size)
        board[i] = A

    if (isSolution(board)[0]):
        print "There is a winner."
    else:
        print "No winner."

# recursive, given a nxn board, return a tuple
# first value = boolean, true if a solution exists
# second value = array of solutions that might be part of the n+1 solution
# each solution includes which player (X/O), row/column number wrt array or diagonal
# note - you still have to check the last row/colum or right to left diagonal without recursion
def isSolution(arr):
    n = len(arr)
    assert (n == len(arr[0]))

    if (n < 1):
        return (False, [None])
    elif (len(arr) == 1):
        if (arr[0][0] == 'N'):
            return (False, [None])
        elif (arr[0][0] == 'X'):
            return (True, ['Xr0', 'Xc0', 'Xd0'])
        else:
            return (True, ['Or0', 'Oc0', 'Od0'])
    else:
        sol = isSolution(truncate(arr, len(arr)-1)) # solution for subboard
        sollist = []; #list of solutions for this board
        if (sol[0]): #if there is a solution for the subboards, iterate through them
            for i in sol[1]:
                if (i[1] == 'r'):
                    if (arr[int(i[2])][len(arr)-1] == i[0]):
                        sollist.append(i);
                elif (i[1] == 'c'):
                    if (arr[len(arr)-1][int(i[2])] == i[0]):
                        sollist.append(i);
                elif (i[1:3] == 'd0'):
                    if (arr[len(arr)-1][len(arr)-1] == i[0]):
                        sollist.append(i);

        # check last row for solution
        isSame = True
        count = 0
        while (isSame and (count < n-1)):
            isSame = arr[n-1][count] == arr[n-1][count+1]
            if (arr[n-1][count] == 'N'):
                isSame = False
            count += 1
        if (isSame):
            newSol = arr[n-1][0] + 'r' + str(n-1)
            sollist.append(newSol)

        # check last column for solution
        isSame = True
        count = 0
        while (isSame and (count < n-1)):
            isSame = arr[count][n-1] == arr[count+1][n-1]
            if (arr[count][n-1] == 'N'):
                isSame = False
            count += 1
        if (isSame):
            newSol = arr[0][n-1] + 'c' + str(n-1)
            sollist.append(newSol)

        # check right to left diagonal
        isSame = True
        count = 0
        while (isSame and (count < n-1)):
            isSame = arr[count][n-1-count] == arr[count+1][n-2-count]
            if (arr[count][n-1-count] == 'N'):
                isSame = False
            count += 1
        if (isSame):
            newSol = arr[0][n-1] + "d1"
            sollist.append(newSol)

        if (len(sollist) > 0):
            return (True, sollist)
        else:
            return (False, [None]);

# given a mxm array, return the top left nxn values
def truncate(arr, n):
    res = [[None] * n] * n
    m = len(arr)
    if (n < m):
        for i in range(n):
            res[i] = arr[i][0:n]
    else:
        res = arr
    return res

if __name__ == "__main__":
    main()

# creates a random nxn board
def makeBoard(n):
    board = [None] * n

    for i in range(n):
        row = [None] * n
        for j in range(n):
            entry = ''
            rand = random.randrange(0,3)
            if (rand == 0):
                entry = 'X'
            elif (rand == 1):
                entry = 'O'
            else:
                entry = 'N'
            row[j] = entry
        board[i] = row
    
    return board

# given nxn board, print
def printBoard(board):
    n = len(board)
    for i in range(n):
        row = ''
        for j in range(n):
            row += board[i][j] + ' '
        print row
    return
