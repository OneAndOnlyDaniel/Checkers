class Board:
	def __init__(self, board, isWhiteTurn, player1="Player1", player2="Player2", smoves = []):
		self.board = board
		self.isWhiteTurn = isWhiteTurn
		self.player1 = player1
		self.player2 = player2
		self.moves = moves

	def __str__(self):
		s = ""
		for y in range(8):
			for x in range(8):
				if y % 2 == 0:
					if x % 2 == 0:
						s = s + "."
					else:
						s = s + self.board[4 * y + (x - 1) // 2]
				else:
					if x % 2 == 0:
						s = s + self.board[4 * y + x // 2]
					else:
						s = s + "."

			s = s + "\n"
		return s

	def IORead(boardName):
		# Returning (board, isWhiteTurn, player1, player2, moves)
		f = open("src/Boards/{0}.txt".format(boardName), "r")
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

		return [board, isWhiteTurn, player1, player2, smoves]