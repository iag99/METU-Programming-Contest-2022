import datetime
import functools

N, K = list(map(int, input().split()))
decks  = list(map(int, input().split()))

def get_id_tuple(f, args, kwargs, mark=object()):
    l = [id(f)]
    for arg in args:
        if(isinstance(arg, list)):
            for el in arg:
                l.append(id(el))
        else:
            l.append(id(arg))
    l.append(id(mark))
    for k, v in kwargs:
        l.append(k)
        l.append(id(v))
    return tuple(l)

_memoized = {}
def memoize(f):
    def memoized(*args, **kwargs):
        key = get_id_tuple(f, args, kwargs)
        if key not in _memoized:
            _memoized[key] = f(*args, **kwargs)
        return _memoized[key]
    return memoized

def counter(decks, chosen_decks, current_index, K, k):
    if(current_index >= len(decks)):
        # print(chosen_decks)
        return len(chosen_decks)

    last_deck = chosen_decks[len(chosen_decks) - 1] if len(chosen_decks) > 0 else decks[current_index]
    
    index = current_index;
    while(index < len(decks) and decks[index] < last_deck):
       index += 1;
    
    unchoosed_situation = counter(decks, chosen_decks, index + 1, K, k)
    choosed_situation = 0
    if(index < len(decks)):
        k = k + 1 if (last_deck == decks[index]) else 1;
        if(k <= K):
            _chosen_decks = chosen_decks[:];   
            _chosen_decks.append( decks[index] )
            choosed_situation = counter(decks, _chosen_decks, index + 1, K, k)

    return max( unchoosed_situation, choosed_situation);

counter = memoize(counter)

a = datetime.datetime.now()
print( counter(decks, [], 0, K, 0) )
b = datetime.datetime.now()

# print((b-a).microseconds)
