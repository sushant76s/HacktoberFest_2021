
from collections import deque
def oranges(grid):

	if grid==None:
		return 0
	rows = len(grid)
	if rows ==0:
		return 0
	cols = len(grid[0])
	if cols == 0:
		return 0

	queue = deque()
	visited = [[0]*cols for i in range(rows)]

	oranges = 0
	for i in range(0, rows):
		for j in range(0, cols):
			if grid[i][j] in [1,2]:
				oranges +=1 
			if grid[i][j]==2:
				queue.append([i,j,0])

	direc_x = [1,-1,0,0]
	direc_y = [0,0,1,-1]

	def is_valid(x,y):
		if x<0 or x>=rows:
			return False
		if y<0 or y>=cols:
			return False
		return True

	mins = 0
	def bfs(queue):

		while(len(queue)):
			x,y,t = queue.popleft()
			mins = max(mins, t)
			for i in range(4):
				x1 = x + direc_x[i]
				y1 = y + direc_y[i]
				if is_valid(x1,y1) and grid[x1][y1] ==1:
					grid[x1][y1] = 2
					queue.append([x1,y1, t+1])


	bfs(queue)
	rotten = 0
	for i in range(rows):
		for j in range(cols):
			if grid[i][j]==2:
				rotten+=1

	return mins if rotten = oranges else -1