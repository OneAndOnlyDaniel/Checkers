from Board import *

def ReadBoard():
	# Returning (board, isWhiteTurn, player1, player2, moves)
	f = open("src/Boards/startingPosition.txt", "r")
	s = f.read()
	f.close()

	splitFile = s.split('\n')

	# Extracts the first row. The first row is of the form "1,Player1,Player2"
	firstRow = splitFile[0].split(',')

	# Determines whose turn it is, starts with 1
	isWhiteTurn = (int(firstRow[0]) % 2 == 1)
	player1 = firstRow[1]
	player2 = firstRow[2]

	# The actual board
	sboard = splitFile[1:9]
	# The moves that were played, might be empty
	smoves = splitFile[9]

	# Writes the board into a 32 element list
	board = []
	for r in sboard:
		for c in r:
			board.append(c)

	print(board)

	return [board, isWhiteTurn, player1, player2, smoves)