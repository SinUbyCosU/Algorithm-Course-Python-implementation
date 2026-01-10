import random

def easy_select(A,i):
    if len(A) ==1:
        return A[0]
    pivot=random.choice(A)
    left=[x for x in A if x<pivot]
    mid=[x for x in A if x==pivot]
    right=[x for x in A if x>pivot]

    if len(left)>=i:
        return easy_select(left,i)
    elif len(left) + len(mid) >= i:
        return mid[0]
    else:
        return easy_select(right, i-len(left)-len(mid))

# Call the function and print the result
print(easy_select([3,4,5,6,7,8,9],4))




