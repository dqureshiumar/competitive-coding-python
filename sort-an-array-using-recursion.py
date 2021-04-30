# Author : Umar Qureshi
# Sort an Array using recursion in Python3
def inserti(listi,temp):
    if(len(listi) == 0 or listi[len(listi) - 1] <= temp):
        listi.append(temp)
        return
    val  = listi[len(listi) - 1]
    listi.pop()
    inserti(listi,temp)
    listi.append(val)
    return
def sorti(listi):
    if len(listi) == 1:
        return
    temp = listi[len(listi) - 1]
    listi.pop()
    sorti(listi)
    inserti(listi,temp)
    return
a = [5,2,3,4,1]
sorti(a)
print(*a,sep=" ")