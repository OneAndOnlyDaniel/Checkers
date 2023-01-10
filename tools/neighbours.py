# Precomputes all the neighbors for the main program
def getNeighbours(n):
	if (n in range(5, 26 + 1)): # Interior
		if(n // 4 % 2 == 0):
			return [n - 4, n - 3, n + 4, n + 5]
		if(n // 4 % 2 == 1):
			return [n - 5, n - 4, n + 3, n + 4]
	elif (n + 1 in {5, 13, 21, 12, 20, 28}): # Left or Right End
		return [n - 4, n + 4]
	elif (n + 1 in {1, 2, 3}):
		return [n + 4, n + 5]
	elif (n + 1 in {30, 31, 32}):
		return [n - 4, n - 5]
	elif (n + 1 == 4):
		return [8 - 1]
	elif (n + 1 == 29):
		return [25 - 1]

s = "neighboursDict = {\n"
for n in range(32):
	s = s + "\t{0} : {1},\n".format(n, getNeighbours(n))
s = s + "}\n"

f = open("neighboursDict.txt", "w")
f.write(s)
f.close()
