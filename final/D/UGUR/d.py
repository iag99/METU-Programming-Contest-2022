[N, K] = list( map( int, input().split(' ')))
additional_costs = []
for i in range(N-1):
    additional_costs.append(  list( map( int, input().split(' '))) );

def calculate_min_cost(start_month):
    # base case
    if( start_month == N - 1):
        return K
    elif( start_month >= N):
        return 0

    # choices
    choices = [ calculate_min_cost( start_month + 1) ]
    add_costs = additional_costs[start_month]
    for i in range(len(add_costs)):
        choices.append( add_costs[i] + calculate_min_cost( start_month + i + 2) )

    return K + min(choices);

print( calculate_min_cost(0) )
