import os
import sys
from colorama import Fore, Back, Style

def gameManager(isWhiteTurn, board, player1, player2):
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=28, cols=67))
	isRunning = True
	while(isRunning):
		os.system('cls' if os.name == 'nt' else 'clear')
		renderBoard(board, player1, player2, isWhiteTurn)

		getInput = True
		while(getInput):
			getInput = False
			s = input("Enter a position like [c6] to select a piece\n")
			x = ord(s[0]) - 97
			y = int(s[1]) - 1

			if(0 <= y and y <= 7 and x >= 0 and x <= 7):
				selected = board[y][x]
				if selected == 0:
					print("Empty Selection!")
					getInput = True
				if selected == 1 and not(isWhiteTurn) or selected == 2 and isWhiteTurn:
					print("Wrong Color Selected!")
					getInput = True
			else:
				getInput = True

		tempStr = "White" if selected == 1 else "Black"

		board[y][x] = 3
		os.system('cls' if os.name == 'nt' else 'clear')
		renderBoard(board, player1, player2, isWhiteTurn)
		board[y][x] = 0

		lm = getLegalMoves(y, x, selected, isWhiteTurn, board)

		legMovesSplit = lm.split(" ")
		# Removes the last element b.c. "a b c" gets split into 4 parts
		del legMovesSplit[-1]

		legMoves = []
		legCaptures = []

		for s in legMovesSplit:
			if(s[0] == "m"):
				legMoves.append(s[2:])
			elif(s[0] == "c"):
				legCaptures.append(s[2:])

		i = 0
		print("Legal Moves:")
		for j in legMoves:
			print("\t{0}. {1}".format(i + 1, j))
			i += 1
		print("Legal Captures:")
		for j in legCaptures:
			print("\t{0}. {1}".format(i + 1, j))
			i += 1

		s = input("What do you choose?")
		inp = int(s) - 1
		print("\n\tinp = {0}".format(inp))
		if(inp < len(legMoves)):
			print("Legal move {0} selected".format(inp + 1))
			move(y, x, legMoves[inp], selected, board)
		else:
			print("Legal capture {0} selected".format(inp + 1))

		print("Press ENTER to continue")

		isWhiteTurn = not(isWhiteTurn)

def userInput(query):
	while(getInput):
		getInput = False
		# TODO: Input sanitizing in a seperate function
		s = input(query)
		if(len(s) == 2):
			x = ord(s[0]) - 97
			y = int(s[1]) - 1

			if(0 <= y and y <= 7 and x >= 0 and x <= 7):
				temp = board[y][x]
				if temp == 0:
					print("Empty Selection!")
					getInput = True
				if (temp == 1 or temp == 4) and not(isWhiteTurn) or (temp == 2 or temp == 4) and isWhiteTurn:
					print("Wrong Color Selected!")
					getInput = True
			else:
				print("Out of Bounds")
				getInput = True
		else:
			print("Input has to be 2 Elements")
			getInput = True
	return [y, x]

def renderRow(row, index, player1, player2):
	s = "\t\t\t{0}   ".format(index)
	for r in row: # I should use an enum for this, in case I want to swap later
		if r == 1: # White Pawn
			s = s + Fore.GREEN + "w" + Style.RESET_ALL
		elif r == 2: # Black Pawn
			s = s + Fore.RED + "b" + Style.RESET_ALL
		elif r == 3: # Selector
			s = s + Fore.CYAN + "*" + Style.RESET_ALL
		elif r == 4: # White Queen
			s = s + "W"
		elif r == 5: # Black Queen
			s = s + "B"
		else: # This should only occur of r = 0
			s = s + "."
	s = s + "   " + str(index)
	print(s)

def renderBoard(board, player1, player2, isWhiteTurn):
	if isWhiteTurn:
		print("\t\t{0}      vs.\t{1}".format(Back.WHITE + Fore.GREEN + player1 + Style.RESET_ALL, Fore.RED + player2 + Style.RESET_ALL))
	else:
		print("\t\t{0}      vs.\t{1}".format(Fore.GREEN + player1 + Style.RESET_ALL, Back.WHITE + Fore.RED + player2 + Style.RESET_ALL))
	
	print("\t\t\t    abcdefgh\n")

	for i in range(8):
		renderRow(board[i], i + 1, player1, player2)

	print("\n\t\t\t    abcdefgh")

def getLegalMoves(y, x, f, isWhiteTurn,board):
	# y, x are the positions of marked piece
	# isWhiteTurn gives us color information
	# board gives us the global boardstate
	s = ""

	# TODO: Put logic for White and Black Queens
	if f == 1: # White Pawn
		if y == 0:
			board[y][x] = 4 # Promotes to a White Queen
			return getLegalMoves(y, x, 4, board) # Rechecks possible moves
		else:
			if x != 7:
				sel = board[y - 1][x + 1]
				if sel == 0: # Empty Square
					s = s + "m_" + chr(x + 1 + 97) + str(y - 1 + 1) + " "
				elif sel == 2 or sel == 5:
					if y >= 2: # If there is a black pawn or queen check if you can jump over
						if board[y - 2][x + 2] == 0:
							s = s + "c_" + chr(x + 2 + 97) + str(y - 2 + 1) + " "
			if x != 0:
				sel = board[y - 1][x - 1]
				if sel == 0: # Empty Square
					s = s + "m_" + chr(x - 1 + 97) + str(y - 1 + 1) + " "
				elif sel == 2 or sel == 5:
					if y >= 2: # If there is a black pawn or queen check if you can jump over
						if board[y - 2][x - 2] == 0:
							s = s + "c_" + chr(x - 2 + 97) + str(y - 2 + 1) + " "
	elif f == 2: # Black Pawn
		if y == 7:
			board[y][x] = 5 # Promotes to a Black Queen
			return getLegalMoves(y, x, 5, board) # Rechecks possible moves
		else:
			if x != 7: 
				sel = board[y + 1][x + 1]
				if sel == 0: # Empty Square
					s = s + "m_" + chr(x + 1 + 97) + str(y + 1 + 1) + " "
				elif sel == 1 or sel == 4:
					if y <= 6: # If there is a white pawn or queen check if you can jump over
						if board[y + 2][x + 2] == 0:
							s = s + "c_" + chr(x + 2 + 97) + str(y + 2 + 1) + " "
			if x != 0:
				sel = board[y + 1][x - 1]
				if sel == 0: # Empty Square
					s = s + "m_" + chr(x - 1 + 97) + str(y + 1 + 1) + " "
				elif sel == 1 or sel == 4:
					if y <= 6: # If there is a white pawn or queen check if you can jump over
						if board[y + 2][x - 2] == 0:
							s = s + "c_" + chr(x - 2 + 97) + str(y + 2 + 1) + " "
	return s

def move(y, x, pos, selected, board):
	print("Calling move({0}, {1}, {2}, board)".format(y, x, pos))
	# Converts pos into coords
	a = ord(pos[0]) - 97
	b = int(pos[1]) - 1

	# Swaps Board[y][x] with Board[b][a]
	# w/ assumption that the move is valid, i.e.
	# board[b][a] = 0, i.e. " "
	board[y][x] = 0
	board[b][a] = selected

def capture(y, x, b, a, board):
	temp = board[y][x]
	board[(y + b) // 2][(x + a) // 2] = 0
	board[y][x] = 0
	board[b][a] = temp