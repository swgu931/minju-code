import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    R, C, K = map(int, readl().split())
    rects = [list(map(int,readl().split())) for _ in range(K)]
    return R, C, K, rects
 
def Fill_Paper():
        paper = [[0] * 100 for _ in range(100)]
        for sc, sr, ec, er in rects:
                for r in range(sr, er):
                        for c in range(sc, ec):
                                paper[r][c] = 1
        return paper
 
# BFS방식으로 영역의 크기를 확인
def Flood_Fill(sr, sc):
        q = deque()
        #상하좌우 변위
        d = ((-1,0), (1,0), (0,-1), (0,1)) # (dr, dc)
 
        #큐에 시작위치를 저장
        q.append((sr, sc))
        size = 1 # (sr, sc) 위치를 영역으로 카운트
 
        # 영역으로 중복카운트가 되지 않도록 해야 함(paper[sr][sc]에 0이 아닌 값으로 변경)
        paper[sr][sc] = 1 # 1은 직사각형의 내부, 이미 카운트된 영역
 
        # 주변 탐색(큐가 빌때까지)
        while q:
                r, c = q.popleft()
                # 상하좌우 탐색
                for dr, dc in d:
                        nr, nc = r + dr, c + dc
 
                        # 1. 범위체크
                        if ( not 0 <= nr < R) or ( not 0 <= nc < C) : continue
                        # 2. 직사각형의 내부, 이미 카운트된 영역
                        if paper[nr][nc] == 1: continue
 
                        # 새로운 0인 곳이고 영역으로 카운트
                        size += 1
                        paper[nr][nc] = 1 # 영역으로 중복 카운트되지 않도록
                        q.append((nr,nc))
        return size
         
 
def solve():
        list_size = []
        #모눈종이를 순차적으로 탐색하면서 직사각형의 내부가 아닌 곳에서 영역 판단
        for r in range(R):
                for c in range(C):
                        if paper[r][c] == 0: # 영역의 시작점
                                list_size.append(Flood_Fill(r,c)) # (r,c)와 인접한 곳들로 구성된 영역의 크기
        list_size.sort()
        return list_size
 
         
 
sol = [-1]
# 입력받는 부분
R, C, K, rects = Input_Data()
  
# 여기서부터 작성
# 모눈종이에 직사각형의 내부를 1로 표시
paper = Fill_Paper()
 
sol = solve()
 
# 출력하는 부분 
print(len(sol))
print(*sol)
