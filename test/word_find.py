def find(word,strat_word,mat,col,row):
    if len(word)-1==strat_word:
        return True
    if (col<0 or row<0 or  row>=len(mat) or col>=len(mat[0])):
        return False

    if word[strat_word]==mat[col][row]:
        return find(word,strat_word+1,mat,col,row+1) or find(word,strat_word+1,mat,col,row-1) or find(word,strat_word+1,mat,col+1,row) or find(word,strat_word+1,mat,col-1,row)
    else:
        return False
        


def mainfunc():
    mat = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','E','E','E']
    ]
    word = "ABCCED"

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if word[0]==mat[i][j]:
                bol = find(word,0,mat,j,i)
                if bol==True:
                    return True
    return False

print(mainfunc())


        
