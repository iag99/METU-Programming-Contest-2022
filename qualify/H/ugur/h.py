(A, B, C) = tuple(map(lambda x: int(x), input().split()))

def chemicalReactions(A,B,C):
    #base case
    print(A,B,C)
    if( (A,B) == (0,0) or (B,C) == (0,0) or (A,C) == (0,0)):
        print("Already solved")
        return 0;
    
    changes = []
    if(A != 0 and B != 0):
        print("A-B -> C")
        (r_sit, r_number) = reduce([A,B,C], 2)
        changes.append(r_number + chemicalReactions(*r_sit))
    if(A != 0 and C != 0):
        print("A-C -> B")
        (r_sit, r_number) = reduce([A,B,C], 1)
        changes.append(r_number + chemicalReactions(*r_sit))
    if(B != 0 and C != 0):
        print("B-C -> A")
        (r_sit, r_number) = reduce([A,B,C], 0)
        changes.append(r_number + chemicalReactions(*r_sit))

    print(changes)
    return min(changes) 
            

def reduce(situation, reduce_to):
    input_elements = situation[:]
    del input_elements[reduce_to]
    reduce_number = min(input_elements)
    print("reduce_number", reduce_number)

    res_situation = []
    for i in range(len(situation)):
        if(i == reduce_to):
            res_situation.append(situation[i] + reduce_number)  
        else:
            res_situation.append(situation[i] - reduce_number)
    return res_situation, reduce_number

print(chemicalReactions(A,B,C))
# print(reduce([3,2,0], 2))

