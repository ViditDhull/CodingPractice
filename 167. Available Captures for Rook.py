class Solution(object):
    def numRookCaptures(self, board):
        co=0
        for i in range(8):
            for j in range(8):
                if board[i][j]=="R":
                    left=j-1
                    while(left>-1):
                        if board[i][left]=="p":
                            co+=1
                            break
                        elif board[i][left]=="B":
                            break
                        else:
                            left-=1
                    right=j+1
                    while(right<8):
                   
                        if board[i][right]=="p":
                            co+=1
                            break
                        elif board[i][right]=="B":
                            break
                        else:
                            right+=1
                    top=i-1
                    while(top>-1):
                        if board[top][j]=="p":
                            co+=1
                            break
                        elif board[top][j]=="B":
                            break
                        else:
                            top-=1
                    bot=i+1
                    while(bot<8):
                        if board[bot][j]=="p":
                            co+=1
                            break
                        elif board[bot][j]=="B":
                            break
                        else:
                            bot+=1
                    return co
        return co