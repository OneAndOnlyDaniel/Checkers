class Board:
	def __init__(self, board, turnNumber, player1="Player1", player2="Player2", moves = []):
		self.board = board
		self.turnNumber = turnNumber
		self.player1 = player1
		self.player2 = player2
		self.moves = moves

	def __str__(self):
		s = "{0},{1},{2}\n".format(self.turnNumber, self.player1, self.player2)
		for y in range(8):
			for x in range(4):
				s = s + self.board[4 * y + x]
			s = s + "\n"
		
		s = s + self.moves
		return s

	def renderBoard(self):
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

		return s[:-1]

def coordinateToIndex(coord):
		# The order is : (xy) where x is either a number or a letter
		# and y is a always a number
		# If the first char is a letter then convert it to a number
		# Low.cs.lttrs. start w/ ASCII index 97, we index from 1 so the + 1
		if(coord[0].isalpha()):
			x = ord(coord[0]) - 97 + 1
		else:
			x = int(coord[0])

		y = int(coord[1])

		if (x < 1 or x > 8 or y < 1 or y > 8):
			raise Exception("Out of bounds")

		if ((x % 2) + (y % 2)) >= 1:
			raise Exception("Need to have odd incides")

