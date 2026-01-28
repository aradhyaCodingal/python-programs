theboard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' ',}
board_key=[]
for key in theboard:
    board_key.append(key)
def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print(board['1']+'|'+board['2']+'|'+board['3'])
def game():
        turn='x'
        count=0
        for i in range (10):
            printBoard(theboard)
            print("its your turn"+ turn +". move to which place")
            move=input()
            if theboard[move]==' ':
                theboard[move]=turn
                count +=1
            else:
                print("the place is aldredy filled.\n move to which place")
                continue
            if count>=5:
                if theboard['7']==theboard ['8']==theboard['9']!=' ':
                    printBoard(theboard)
                    print("\n game over")
                    print("****"+turn+"won. ******")
                    break
                      
                elif theboard['4']==theboard ['5']==theboard['6']!=' ':
                    printBoard(theboard)
                    print("\n game over")
                    print("****"+turn+"won. ******")
                    break
                        
            
                elif theboard['1']==theboard ['2']==theboard['3']!=' ':
                    printBoard(theboard)
                    print("\n game over")
                    print("****"+turn+"won. ******")
                    break

                elif theboard['1']==theboard ['4']==theboard['7']!=' ':
                    printBoard(theboard)
                    print("\n game over")
                    print("****"+turn+"won. ******")
                    break

                elif theboard['2']==theboard ['5']==theboard['8']!=' ':
                    printBoard(theboard)
                    print("\n game over")
                    print("****"+turn+"won. ******")
                    break

                elif theboard['3']==theboard ['6']==theboard['9']!=' ':
                    printBoard(theboard)
                    print("\n game over")
                    print("****"+turn+"won. ******")
                    break
                
                elif theboard['3']==theboard ['5']==theboard['7']!=' ':
                    printBoard(theboard)
                    print("\n game over")
                    print("****"+turn+"won. ******")
                    break

                elif theboard['1']==theboard ['5']==theboard['9']!=' ':
                    printBoard(theboard)
                    print("\n game over")
                    print("****"+turn+"won. ******")
                    break
            if count==9:
                print("\n game over")
                print("its a tie")
            if turn=='x':
                turn=0
            else:
                turn='x'
        restart=input("\n do you wanna continue")
        if restart=='y'or restart=='Y':
            for key in board_key:
                theboard[key]=" "
            game()
if __name__ =="__main__":
    game()
   



