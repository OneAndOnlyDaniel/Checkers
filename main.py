import os
import sys

from src.CheckersFunctions import *
from src.CheckersIO import *

"""
Plan from here is to list the possible moves to be selected: m45c52 ->
1. Move     (4, 5)
2. Capture  (5, 2)
b. Back
Then the user selects one of those and the corresponding function gets called
on "b" the selection gets skipped

TODO
[ ] Core Functionality
	[x] Put functions in seperate file
	[x] Move selector
		[ ] Capture Mechanic
			[ ] Capture Chains
	[x] Main Menu
	[ ] Input Sanitizing

Potential projects building on this
	[ ] I/O
		[x] Load Boards from .txt file
		[ ] Save Board to .txt
	[ ] AI opponent
	[ ] Scoring system on a Website
	[ ] User Interface
		[ ] Mouse Support
		[ ] Art
	[ ] Web Application
		[ ] Connected to Database for Scoring
		[ ] Multiplayer
"""

# The Gameboard, TODO read from file
board = [
	[0, 2, 0, 2, 0, 2, 0, 2],
	[2, 0, 2, 0, 2, 0, 2, 0],
	[0, 2, 0, 2, 0, 2, 0, 2],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[1, 0, 1, 0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 0]]

player1 = "Player1"
player2 = "Player2"

# Main Gameloop
os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=67))

# If a board is passed as an Argument then skip the homescreen
isWhiteTurn = True
isPassedArgument = False
if len(sys.argv) > 1:
	isPassedArgument = True
	[board, player1, player2, isWhiteTurn] = readBoard("src/Boards/" + sys.argv[1])

while(True):
	if not(isPassedArgument):
		print("    * / ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / *")
		print("   * / ~~~~~~~~~~~~~~~~~~~~~~  Checkers  ~~~~~~~~~~~~~~~~~~~~~ / *")
		print("  * / ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / *")
		print(" * / (C) Nekoniel Software Atelier, 2023 All rights reserved / *")
		print("* /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / *")
		print()
		print("\tWhat do you want to do?")
		print("\t1. Play")
		print("\t2. Load Board")
		print("\t3. Print current Board")
		print("\t4. Save Board")
		print("\t5. Change Name of P1 ({0})".format(player1))
		print("\t6. Change Name of P2 ({0})".format(player2))
		print("\t7. Exit")
		inp = input()

		if(inp == "1"):
			[isWhiteTurn, board] = gameManager(isWhiteTurn, board, player1, player2)
		elif(inp == "2"):
			[board, player1, player2, isWhiteTurn] = readBoard(input("Write the name to the board: ") + ".board")
			input("Successfully loaded the Board. Press ENTER to continue")
		elif(inp == "3"):
			renderBoard(board, player1, player2, isWhiteTurn)
			input("Press ENTER to continue")
		elif(inp == "4"):
			temp = input("Give the board a name : ")
			writeBoard(board, isWhiteTurn, player1, player2, temp)
			input("Successfully saved the Board as \"{0}.board\" . Press ENTER to continue".format(temp))
		elif(inp == "5"):
			player1 = input("What is the first Player's Name? ")
		elif(inp == "6"):
			player2 = input("What is the second Player's Name? ")
		elif(inp == "7"):
			os.system('cls' if os.name == 'nt' else 'clear')
			quit()
		else:
			print("Invalid input!")
			input("Press ENTER to continue")
	else:
		gameManager(isWhiteTurn, board, player1, player2)

	os.system('cls' if os.name == 'nt' else 'clear')
