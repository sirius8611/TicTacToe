
board = {'top_l':" ", 'top_m':" ", 'top_r':" ",
          'l':" ", 'm':" ",'r':" ",
          'low_l':" ",'low_m':" ",'low_r':" "}
row =[['top_l', 'top_m', 'top_r']
       ,['l', 'm','r']
       ,['low_l', 'low_m', 'low_r']]
col =[ ['top_l', 'l', 'low_l']
      , ['top_m', 'm', 'low_m']
      , ['top_r', 'r', 'low_r']]
cros =[  ['top_l', 'm', 'low_r']
       , ['top_r', 'm', 'low_r']]
def printboard(): # print the board
  print(board['top_l'] + " | " + board['top_m'] + " | " + board['top_r'])
  print("----------")
  print(board['l'] + " | " + board['m'] + " | " + board['r'])
  print("----------")
  print(board['low_l'] + " | " + board['low_m'] + " | " + board['low_r'])
def checkrow(x): #check if the row is a winning row
  for i in range(3):
    if x in row[i]:
      for j in row[i]:
        if board[x] != board[j]:
          return False
  return True
def checkcol(x): # check if the column is a winning column
  for i in range(3):
    if x in col[i]:
      for j in col[i]:
        if board[x] != board[j]:
          return False
  return True
def checkcros(x):#check the two crossing 
  for i in range(2):
    if x in cros[i]:
      for j in cros[i]:
        if board[x] != board[j]:
          return False
      return True
  return False
 
def check(x):
  if checkrow(x) == True or checkcol(x) == True or checkcros(x) == True:
    return True
  return False
def startgame():#start the game
  print("Welcome to Hieu Tic Tac Toe")
  print("X moves first")
  play()
def play(): #the main play 
  fill = 1
  won = False
  turn = 'X'
  while fill <= 9:
    print("This is " + turn + " turn!")
    playermove = input("Place at ")
    if playermove not in board or board[playermove] != " ":
      while playermove not in board or board[playermove] != " ":
        playermove = input("Error. Please choose other place: ")
    board[playermove] = turn
    if check(playermove) == True:
      won = True
      break
    if turn == 'X':
      turn = 'O'
    else:
      turn = 'X'
    fill += 1
    printboard()
  if won == True:
    printboard()
    print(turn + " won!")
  else:
    print("No one win!")
  exit()
   
def driver():
  printboard()
  startgame()
  play()
driver()
#print(row)
