#Author Umar Qureshi
# KTH Symbol in Grammar
def solve(N,K):
    if N == 1 and K == 1:
        return 0
    mid = 2 ** (N - 1)
    mid= mid // 2
    if K <= mid:
        return solve(N-1,K)
    else:
        return not solve(N-1,K-mid)
ans = solve(1,1)
if ans == True:
    print("1")
else:
    print("0")