import random

def iterative_easy_select(A,i):
    p=0
    r=len(A)-1
    while True:
        if p==r:
            return A[p]
        pivot_idx=random.randint(p,r)
        pivot_val=A[pivot_idx]
        A[pivot_idx],A[r]=A[r].A[pivot_idx]

        q=p
        for j in range(p,r)