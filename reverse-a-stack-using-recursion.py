# Author: Umar Qureshi
# Reverse a Stack using Recursion
def reverse_the_stack(listi,temp):
    if len(listi) == 0:
        listi.append(temp)
        return
    elem = listi.pop()
    reverse_the_stack(listi,temp)
    listi.append(elem)
    return
def stack_init(listi):
    if len(listi) == 1:
        return
    temp = listi.pop()
    stack_init(listi)
    reverse_the_stack(listi,temp)
a = [1,2,3,4,5]
stack_init(a)
print(*a,sep=" ")
    
    