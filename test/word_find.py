def find(word,strat_word,mat,row,col):
    if len(word)==strat_word:
        return True
    if (col<0 or row<0 or  row>=len(mat) or col>=len(mat[0])):
        return False

    if word[strat_word]==mat[row][col]:
        temp = mat[row][col]
        mat[row][col] = 0
        fin = find(word,strat_word+1,mat,row+1,col) or find(word,strat_word+1,mat,row-1,col) or find(word,strat_word+1,mat,row,col+1) or find(word,strat_word+1,mat,row,col-1)
        mat[row][col] = temp
        return fin
    else:
        return False
        


def mainfunc():
    mat = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    word = "SEE"

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if word[0]==mat[i][j]:
                bol = find(word,0,mat,i,j)
                if bol==True:
                    return True
    return False

print(mainfunc())


        
