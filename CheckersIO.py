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