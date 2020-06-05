import random

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,'4': ' ' , '5': ' ' , '6': ' ' ,'7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    
def printResult(turn):
  print("\nGame Over.\n")                
  print("**** Player "+turn+" won****")
  

def game():
  turn = random.choice(['X','O'])
  count = 0

  for i in range(10):
    printBoard(theBoard)
    print ("\nIts your turn: "+ turn +"\nGive a Move [1-9] : ")

    move = input()
    if theBoard[move] == ' ':
        theBoard[move] = turn
        count += 1
    else:
        print("That place is already filled.\nChoose Another Place: ")
        continue

    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            printResult(turn)                
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
            printBoard(theBoard)
            printResult(turn)
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            printResult(turn)
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
            printBoard(theBoard)
            printResult(turn)
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
            printBoard(theBoard)
            printResult(turn)
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            printResult(turn)
            break 
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            printResult(turn)
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            printResult(turn)
            break 
        if count == 9:
            print("\nGame Over.\n")                
            print("*****It's a Tie*****")
            break

    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'        
    
  restart = input("Do want to play Again?(y/n):\n ")
  if restart.lower()=='y':  
      for key in board_keys:
          theBoard[key] = " "
      game()
  else:
    print("**Thanks for playing**")

if __name__ == "__main__":
    game()
