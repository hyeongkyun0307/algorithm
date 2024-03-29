def solution(m, n, puddles):
    answer = 0
    
    lst = [[0 for _ in range(m)] for _ in range(n)]
#   initial point
    for i in range(n):
        for j in range(m):
            if(i==0 or j==0):
                lst[i][j] = 1
#   puddle
    for k in puddles:
        
        lst[k[1]-1][k[0]-1] =-1
        if((k[1]-1)==0):
            for p in range(k[0],m):
                lst[0][p] = -1
        elif(k[0]-1==0):
            for q in range(k[1],n):
                lst[q][0] = -1
#   DP algorithm
    for i in range(1,n):
        for j in range(1,m):
            if(lst[i][j]==-1):
                continue
            elif(lst[i][j-1]==-1 and lst[i-1][j]!=-1):
                lst[i][j] = lst[i-1][j]
            elif(lst[i][j-1]!=-1 and lst[i-1][j]==-1):
                lst[i][j] = lst[i][j-1]
            elif(lst[i][j-1] !=-1 and lst[i-1][j]!=-1):
                 lst[i][j] = lst[i][j-1] +lst[i-1][j]
    
                    
    return (lst[n-1][m-1]%1000000007)
