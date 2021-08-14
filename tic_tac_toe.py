# Python Version of Classic Tic Tac Toe Game --- Jayen Lare

# Displays Current Board
def displayBoard(b):
  x = 0
  y = 0
  print("")
  print("Current Board: ")
  for i in range(1,12):
    if i % 4 == 0:
      print("-------|-------|-------")
    elif i % 2 == 0:
      y = 0
      print("   " + b[x][y] + "   |   ", end = "")
      y += 1
      print(b[x][y] + "   |   ", end = "")
      y += 1
      print(b[x][y] + "   ")
      x += 1
    else:
      print("       |       |")
  print("")


# Displays Menu
def menu():
  print("")
  print("---------MENU--------")
  print("1: Top Left")
  print("2: Top Middle")
  print("3: Top Right")
  print("4: Middle Left")
  print("5: Center")
  print("6: Middle Right")
  print("7: Bottom Left")
  print("8: Bottom Middle")
  print("9: Bottom Right")

# Returns true if there is a winner
def winner(moves):
  if set(['1', '2', '3']).issubset(moves):
    return True
  elif set(['4', '5', '6']).issubset(moves):
    return True
  elif set(['7', '8', '9']).issubset(moves):
    return True
  elif set(['1', '4', '7']).issubset(moves):
    return True
  elif set(['2', '5', '8']).issubset(moves):
    return True
  elif set(['3', '6', '9']).issubset(moves):
    return True
  elif set(['1', '5', '9']).issubset(moves):
    return True
  elif set(['3', '5', '7']).issubset(moves):
    return True
  else:
    return False

# Converts position into an index
def index(pos):
  if pos == '1':
    return (0,0)
  elif pos == '2':
    return (0,1)
  elif pos == '3':
    return (0,2)
  elif pos == '4':
    return (1,0)
  elif pos == '5':
    return (1,1)
  elif pos == '6':
    return (1,2)
  elif pos == '7':
    return (2,0)
  elif pos == '8':
    return (2,1)
  elif pos == '9':
    return (2,2)
  
# Initialize variables and lists to track the game
draw = True
xoFlag = True
prevMoves = []
xMoves = []
oMoves = []
rows, cols = (3, 3)
board = [[' ' for i in range(cols)] for j in range(rows)]


# Starting the game - Selecting amount of players 
print("Welcome to Tic Tac Toe")
print("-----------------------")
players = input("Enter the amount of players(1 or 2): ")

if players == '1':
  # Single Player
  print("Player 1 vs Computer")
  # Selecting X or O
  while xoFlag == True:
    xo = input("Pick 'X' or 'O': ")
    if xo == 'X':
      xoFlag = False
      print("You picked X")
      print("Your move first...")
    elif xo == 'O':
      xoFlag = False
      print("You picked O")
      print("You'll go second'...")
    else:
      print("Invalid choice, pick again...")

  # Player picked X
  if xo == 'X':
    # Displays initial empty board
    displayBoard(board)
    # Read in and display the moves starting with X
    for i in range(9):
      if i % 2 == 0:
        # Display menu
        menu()
        # Check that entered position is valid
        posFlag = True
        while posFlag == True:
          position = input("Enter your choice: ")
          posFlag = False
          intPos = int(position)
          if intPos < 1 or intPos > 9:
            print("Invalid position...")
            print("Please pick again")
            posFlag = True
          if position in prevMoves:
            print("This position has already been taken...")
            print("Please pick again")
            posFlag = True
        prevMoves.append(position)
        xMoves.append(position)
        print("Placed X at position: " + position)
        # Places X on the board
        board[index(position)[0]][index(position)[1]] = 'X'
        displayBoard(board)
      # Computer selects postion
      else:
        posFlag = True
        while posFlag == True:
          from random import randrange
          position = str(randrange(1,9))
          posFlag = False
          if position in prevMoves:
            posFlag = True
        prevMoves.append(position)
        oMoves.append(position)
        print("Computer placed O at position: " + position)
        # Places X on the board
        board[index(position)[0]][index(position)[1]] = 'O'
        displayBoard(board)
      # Check for a winner
      if winner(xMoves) == True:
        print("Game Over... Player X wins!")
        draw = False
        break
      elif winner(oMoves) == True:
        print("Game Over... The Computer wins!")
        draw = False
        break
    # Game has no winner
    if draw == True:
      print("Game Over... It is a draw!")
  # Player picked O
  else:
    # Displays initial empty board
    displayBoard(board)
    # Read in and display the moves starting with the computer
    for i in range(9):
      if i % 2 == 0:
        # Display menu
        menu()
        # Computer selects position
        posFlag = True
        while posFlag == True:
          from random import randrange
          position = str(randrange(1,9))
          posFlag = False
          if position in prevMoves:
            posFlag = True
        prevMoves.append(position)
        xMoves.append(position)
        print("Placed X at position: " + position)
        # Places X on the board
        board[index(position)[0]][index(position)[1]] = 'X'
        displayBoard(board)
      # Player selects a postion
      else:
        # Check that entered position is valid
        posFlag = True
        while posFlag == True:
          position = input("Enter your choice: ")
          posFlag = False
          intPos = int(position)
          if intPos < 1 or intPos > 9:
            print("Invalid position...")
            print("Please pick again")
            posFlag = True
          if position in prevMoves:
            print("This position has already been taken...")
            print("Please pick again")
            posFlag = True
        prevMoves.append(position)
        oMoves.append(position)
        print("You Placed O at position: " + position)
        # Places X on the board
        board[index(position)[0]][index(position)[1]] = 'O'
        displayBoard(board)

      # Check for a winner
      if winner(xMoves) == True:
        print("Game Over... The computer wins!")
        draw = False
        break
      elif winner(oMoves) == True:
        print("Game Over... You win!")
        draw = False
        break
    # Game has no winner
    if draw == True:
      print("Game Over... It is a draw!")
else:
  # Multiplayer
  print("Player 1 vs Player 2")
  print("Player 1 is 'X'")
  print("Player 2 is '0'")
  print("Player 1 goes first...")

  # Displays initial empty board
  displayBoard(board)

  # Read in and display the moves starting with X
  for i in range(9):
    # Display menu
    menu()
    # X's turn
    if i % 2 == 0:
      # Check that entered position is valid
      posFlag = True
      while posFlag == True:
        position = input("Enter your choice: ")
        posFlag = False
        intPos = int(position)
        if intPos < 1 or intPos > 9:
          print("Invalid position...")
          print("Please pick again")
          posFlag = True
        if position in prevMoves:
          print("This position has already been taken...")
          print("Please pick again")
          posFlag = True
      prevMoves.append(position)
      xMoves.append(position)
      print("Placed X at position: " + position)
      # Places X on the board
      board[index(position)[0]][index(position)[1]] = 'X'
      displayBoard(board)
    # O's turn
    else:
      # Check that entered position is valid
      posFlag = True
      while posFlag == True:
        position = input("Enter your choice: ")
        posFlag = False
        intPos = int(position)
        if intPos < 1 or intPos > 9:
          print("Invalid position...")
          print("Please pick again")
          posFlag = True
        if position in prevMoves:
          print("This position has already been taken...")
          print("Please pick again")
          posFlag = True
      prevMoves.append(position)
      oMoves.append(position)
      print("Placed O at position: " + position)
      # Places X on the board
      board[index(position)[0]][index(position)[1]] = 'O'
      displayBoard(board)
    # Check for a winner
    if winner(xMoves) == True:
      print("Game Over... Player X wins!")
      draw = False
      break
    elif winner(oMoves) == True:
      print("Game Over... Player O wins!")
      draw = False
      break
  # Game has no winner
  if draw == True:
    print("Game Over... It is a draw!")