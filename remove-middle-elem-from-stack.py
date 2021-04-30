# Author: Umar Qureshi
# Remove the middle element from a stack
def solve(listi,k):
    if k == 1:
        listi.pop()
        return
    temp = listi[len(listi) - 1]
    listi.pop()
    solve(listi,k-1)
    listi.append(temp)
def remove_elem(listi,k):
    if len(listi) == 0:
        return listi
    solve(listi,k)
    return listi
a = [1,2,3,4,5,6,7,8]
k=len(a)>>1
remove_elem(a,k)
print(a)
