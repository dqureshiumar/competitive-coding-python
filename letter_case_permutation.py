# Author: Umar Qureshi
# Letter Case Permutation using Recursion in python3
def solve(ip,op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op
    op2 = op
    if ip[0].isdigit():
        op1 += ip[0]
        ip = ip[1::]
        solve(ip,op1)
        return
    else:
        op1 += ip[0].upper()
        op2 += ip[0].lower()
        #op2 += ip[0].upper()
        ip = ip[1::]
        solve(ip,op1)
        solve(ip,op2)
        return
    
a = "a1b"
op = ""
solve(a,op)