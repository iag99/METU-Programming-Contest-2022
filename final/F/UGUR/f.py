T = int( input())

# counts # of (x,y) each x,y positive for X*x + Y*y = M
def count_pos_solutions(X, Y, M):
    count = 0;
    y = 1;
    while( M - Y*y > 0):
        if( (M - Y*y) % X == 0):
            count += 1
        y += 1
    return count

for i in range(T):
    args = list( map( int, input().split(' ')))
    cum_x, cum_y = 0, 0
    for j in range(4):
        cum_x += args[2*j] 
        cum_y += args[2*j + 1] 

    [X, Y] = list( map(lambda x: x/4, [cum_x, cum_y]) )
    M = args.pop()
    print( count_pos_solutions(X, Y, M) )

