# read variables
ROW_NUMBER, COL_NUMBER = list(map(int, input().split()))
GRID = []
for i in range(ROW_NUMBER):
    GRID.append(list(map(int, input().split())))

cache = dict()
min_change = ROW_NUMBER * COL_NUMBER - 1
for i in range(ROW_NUMBER):
    for j in range(COL_NUMBER):
        normalized_value = GRID[i][j] - (i + j + 1)
        if( normalized_value in cache.keys() ):
            cache[normalized_value] += 1
        else:
            cache[normalized_value] = 1
        min_change = min(ROW_NUMBER * COL_NUMBER - cache[normalized_value], min_change)

print(min_change)
