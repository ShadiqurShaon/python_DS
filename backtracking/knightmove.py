def createBord():
  n=8
  bord = [[-1 for i in range(8)]for i in range(n)]
  bord[0][0] = 1
  pos = 1
  move_x = [2,2,-2,-2,1,1,-1,-1]
  move_y = [1,-1,1,-1,2,-2,2,-2]
  nextMove(bord,0,0,move_x,move_y,pos)
  # print(move_x[0])
def nextMove(bord,current_x,current_y,move_x,move_y,pos):
  for i in range(8):
    new_x = current_x+move_x[i]
    new_y = current_y+move_y[i]
    if (new_x<8 and new_y<8) and (new_x>0 and new_y>0):
      if bord[new_x][new_y]==-1:
        pos+=1
        bord[new_x][new_y] = pos
        nextMove(bord,new_x,new_y,move_x,move_y,pos)
  return bord

createBord()