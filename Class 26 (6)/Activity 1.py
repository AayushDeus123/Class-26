#TicTacToe Game using all learnt before

TheBoard = {'7':' ' , '8':' ' , '9':' ', 
            '4':' ' , '5':' ' , '6':' ',
            '1':' ' , '2':' ' , '3':' '}
Board_Keys = []

for key in TheBoard:
    Board_Keys.append(key)
    
def Print_Board(board):
    print(board['7'] , '|' , board['8'] , '|' , board['9'])
    print('- + - + -')
    print(board['4'] , '|' , board['5'] , '|' , board['6'])
    print('- + - + -')
    print(board['1'] , '|' , board['2'] , '|' , board['3'])
    
def Game():
    turn = 'X'
    count = 0
    
    for i in range(10):
        Print_Board(TheBoard)
        print("It's your turn" , turn , "Move to which place?")
        
        move = input()
        
        if TheBoard[move] == ' ':
            TheBoard[move] = turn
            count += 1
        else:
            ('The place is already filled\nChoose another square')
            continue
        
        if count >= 5:
            if TheBoard ['7'] == TheBoard['8'] == TheBoard['9'] != ' ':
                Print_Board(TheBoard)
                print('\nGame Over!\n')
                print('***' , turn , 'WON ***')
                break
            
            elif TheBoard ['4'] == TheBoard['5'] == TheBoard['6'] != ' ':
                Print_Board(TheBoard)
                print('\nGame Over!\n')
                print('***' , turn , 'WON ***')
                break
            
            elif TheBoard ['1'] == TheBoard['2'] == TheBoard['3'] != ' ':
                Print_Board(TheBoard)
                print('\nGame Over!\n')
                print('***' , turn , 'WON ***')
                break
            elif TheBoard ['7'] == TheBoard['4'] == TheBoard['1'] != ' ':
                Print_Board(TheBoard)
                print('\nGame Over!\n')
                print('***' , turn , 'WON ***')
                break
            
            elif TheBoard ['8'] == TheBoard['5'] == TheBoard['2'] != ' ':
                Print_Board(TheBoard)
                print('\nGame Over!\n')
                print('***' , turn , 'WON ***')
                break
            
            elif TheBoard ['9'] == TheBoard['6'] == TheBoard['3'] != ' ':
                Print_Board(TheBoard)
                print('\nGame Over!\n')
                print('***' , turn , 'WON ***')
                break
            
            elif TheBoard ['7'] == TheBoard['5'] == TheBoard['3'] != ' ':
                Print_Board(TheBoard)
                print('\nGame Over!\n')
                print('***' , turn , 'WON ***')
                break
            
            elif TheBoard ['9'] == TheBoard['5'] == TheBoard['1'] != ' ':
                Print_Board(TheBoard)
                print('\nGame Over!\n')
                print('***' , turn , 'WON ***')
                break
            
        if count == 9:
            print('\nGAME OVER\n')
            print("It's a Tie!")
            
        if turn == 'X':
            turn = 0
        else:
            turn = 'X'
            
    restart = input('Do you want to play again? (Y/N)')
    if restart == 'Y' or restart == 'y':
        for key in Board_Keys:
            TheBoard[key] == ' '
            
        Game()
        
if __name__ == '__main__':
    Game()     