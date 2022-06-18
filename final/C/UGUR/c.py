N = int(input())
array = list(map(int, input().split(' ')))

def count_unique_elements(arr):
    return len(set(arr))

counter = {}
for i in range(N):
    for j in range( len(array) - i ):
        count = count_unique_elements(array[j:j+i+1] )
        if count in counter.keys():
            counter[count] += 1
        else:
            counter[count] = 1

print( len(counter.keys()));
print( " ".join(list(map( lambda x: str(counter[x]), counter.keys())) ))
