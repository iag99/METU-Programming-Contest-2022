N = int(input())
prices = list( map( int, input().split(' ')))
Q = int(input())

def order1(a, b):
    ls = prices[a:N] + prices[0:b+1] if a >= b else prices[a:b+1] 
    ls.sort()
    return ls[len(ls) - 1] - ls[0]

def order2(a, b, increment):
    index = a - 1
    while( not index == b):
        index = (index + 1) % N
        prices[index] += increment

for i in range(Q):
    order_args = list( map(int, input().split(' '))); 
    [command, a, b] = order_args[0:3]
     
    if( command == 1):
        print( order1(a, b) )
    elif( command == 2):
        increment = order_args[3]
        order2(a, b, increment)
