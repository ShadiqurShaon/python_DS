def knight():
    bord = [[ -1 for i in range(8)] for i in range(8)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    pos = 1
    bord[0][0]=pos
    if nextmove(bord,0,0,move_x,move_y,pos+1) == True:
        printBord(bord)

def printBord(bord):
    for i in range(8):
        for j in range(8):
            print(bord[i][j],end=' ')
        print()

def nextmove(bord,curr_x,curr_y,move_x,move_y,pos):
    if(pos == 65):
        return True
      
    # Try all next moves from the current coordinate x, y 
    for i in range(8): 
        new_x = curr_x + move_x[i] 
        new_y = curr_y + move_y[i] 
        if(new_x>=0 and new_x<8 and new_y>=0 and new_y<8 and bord[new_x][new_y] == -1):
            bord[new_x][new_y] = pos
            if(nextmove(bord,new_x,new_y,move_x,move_y,pos+1)): 
                return True
              
            # Backtracking 
            bord[new_x][new_y] = -1
    return False

                    
                

print(knight())