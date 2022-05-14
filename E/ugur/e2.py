import datetime
# read variables
ROW_NUMBER, COL_NUMBER = list(map(int, input().split()))
GRID = []
for i in range(ROW_NUMBER):
    GRID.append(list(map(int, input().split())))

# 
def formGrid(GRID, row, col):
    change_number = 0;
    for i in range(ROW_NUMBER):
        for j in range(COL_NUMBER):
            if((i-row) + (j - col) !=  GRID[i][j] - GRID[row][col]):
                change_number += 1;
    return change_number;

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
