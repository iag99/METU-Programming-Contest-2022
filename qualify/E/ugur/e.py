import datetime
# read variables
ROW_NUMBER, COL_NUMBER = list(map(int, input().split()))
GRID = []
for i in range(ROW_NUMBER):
    GRID.append(list(map(int, input().split())))

# 
def formGrid(GRID, row, col):
    _GRID = list(map(lambda row: row[:], GRID))
    VISITED = list(map(lambda row: list(map(lambda col: 0, row)), _GRID))
    return  _formGrid(_GRID, VISITED, row, col, _GRID[row][col])


def _formGrid(GRID, VISITED, row, col, set_value):
    if(row < 0 or row > ROW_NUMBER -1 or col < 0 or col > COL_NUMBER - 1):
        return 0
    if(isVisited(VISITED, row, col)):
        return 0;
    
    change_count = 0
    if(GRID[row][col] != set_value):
        change_count += 1
        GRID[row][col] = set_value
    
    VISITED[row][col] = 1;
    cell = GRID[row][col]

    return _formGrid(GRID, VISITED, row+1, col, cell + 1) + _formGrid(GRID, VISITED, row-1, col, cell - 1) + _formGrid(GRID, VISITED, row, col + 1, cell + 1) + _formGrid(GRID, VISITED, row, col-1, cell-1) + change_count;

def isVisited(VISITED, row, col):
    if(row < 0 or row > ROW_NUMBER -1 or col < 0 or col > COL_NUMBER - 1):
        return True; 
    return VISITED[row][col] == 1

# Lets make a memoized formGrid
cache = dict()

def find_equivalent(GRID, i, j):
    for point in cache.keys():
        if(point[0] == i):
            if (j - point[1] == GRID[i][j] - GRID[point[0]][point[1]]):
                return cache[point]
        if(point[1] == j):
            if(i - point[0] == GRID[i][j] - GRID[point[0]][point[1]]):
                return cache[point]
    return None

def memoizedFormGrid(GRID, i, j):
    equivalent = find_equivalent(GRID, i, j)
    if equivalent:
        return equivalent
    result = formGrid(GRID, i, j)
    cache[(i,j)] = result
    return result

start = datetime.datetime.now()
_min = ROW_NUMBER * COL_NUMBER - 1
for i in range(ROW_NUMBER):
    for j in range(COL_NUMBER):
        _min = min(_min, memoizedFormGrid(GRID, i, j))
print( _min );
end = datetime.datetime.now()

print((end-start).microseconds)

