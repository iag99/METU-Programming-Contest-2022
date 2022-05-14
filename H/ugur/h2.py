(A, B, C) = tuple(map(lambda x: int(x), input().split()))

def chemicalReactions(A, B, C):
    if( (A,B) == (0,0) or (B,C) == (0,0) or (A,C) == (0,0)):
        return 0;

def reduce(situation, reduce_to):
    input_elements = situation[:]
    del input_elements[reduce_to]
    reduce_number = min(input_elements)
    diff1 = abs(situation[reduce_to] - input_elements[0]) // 2
    diff2 = abs(situation[reduce_to] - input_elements[1]) // 2
    
    reduce_number = min(reduce_number, diff1, diff2)

    res_situation = []
    for i in range(len(situation)):
        if(i == reduce_to):
            res_situation.append(situation[i] + reduce_number)  
        else:
            res_situation.append(situation[i] - reduce_number)
    return res_situation, reduce_number

print(reduce([60,80,40], 2))
