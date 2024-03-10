from collections import deque
def solution(land):
    answer = 0
    
    lst = [0 for _ in range(len(land[0]))]
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(len(land)):
        for j in range(len(land[i])):
            if(visited[i][j]==0):
                visited[i][j]= 1
                dq = deque()
                
                if(land[i][j]==1):
                    dq.append([i,j])
                    cnt = 0
                    dic = {}
                    while(dq):
                        y,x=dq.popleft()
                        if x not in dic:
                            dic[x] = 1
                        cnt += 1
                        for k in range(4):
                            y_next = y+dy[k]
                            x_next = x+dx[k]
                            if(0<=y_next<len(land) and 0<=x_next<len(land[0])):
                                if(land[y_next][x_next]==1 and visited[y_next][x_next]==0):
                                    visited[y_next][x_next]=1
                                    dq.append([y_next,x_next])
                    for p in dic:
                        lst[p] += cnt
                                    
                                
                                
                                
        
    return max(lst)
