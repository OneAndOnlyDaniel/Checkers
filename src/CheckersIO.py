def writeBoard(board, isWhiteTurn, player1, player2, name):
	f = open(name + ".board", "w")
	turnStr = "1" if isWhiteTurn else "2"
	s = "{0},{1},{2}\n".format(turnStr,player1,player2)
	for r in board:
		temp = ""
		for c in r:
			temp = temp + str(c) + ", "

		temp = temp[:-2]
		s = s + temp + "\n"

	s = s[:-1]

	f.write(s)
	f.close()

def readBoard(directory):
	s = open(directory, "r").read()
	
	board = [
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0]]

	ssplit = s.split("\n")[:-1]

	rsplit = ssplit[0].split(",")

	isWhiteTurn = (rsplit[0] == "1")

	player1 = rsplit[1]
	player2 = rsplit[2]

	for i in range(1, len(ssplit)):
		rsplit = ssplit[i].split(", ")
		for j in range(len(rsplit)):
			board[i-1][j] = int(rsplit[j])

	return [board, player1, player2, isWhiteTurn]