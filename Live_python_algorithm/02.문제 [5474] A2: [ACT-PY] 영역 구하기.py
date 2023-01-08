# 문제 설명
# 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.
# 예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.
 

 
# <그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.
# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.
# * 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.
# import sys


# def Input_Data():
# 	readl = sys.stdin.readline
# 	R, C, K = map(int, readl().split())
# 	rects = [list(map(int,readl().split())) for _ in range(K)]
# 	return R, C, K, rects


# sol = [-1]
# # 입력받는 부분
# R, C, K, rects = Input_Data()
 
# # 여기서부터 작성


# # 출력하는 부분 
# print(len(sol))
# print(*sol)
# 입력 설명
# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다.
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.
# 모눈종이의 왼쪽 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.
# 출력 설명
# 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

# 입력 예시
# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2

# 출력 예시
# 3
# 1 7 13 

import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	R, C, K = map(int, readl().split())
	rects = [list(map(int,readl().split())) for _ in range(K)]
	return R, C, K, rects


sol = [-1]
# 입력받는 부분
R, C, K, rects = Input_Data()
 
# 여기서부터 작성
def Fill_Paper():
    paper = [[0] * 100 for _ in range(100)]    
    for sc, sr, ec, er in rects:
        for r in range(sr, er):
            for c in range(sc, ec):
                paper[r][c] = 1

    return paper


# BFS 방식으로 영역의 크기를 확인

def Flood_Fill(sr, sc):
    q = deque()
    #상하좌우 변위
    d = ((-1,0), (1,0), (0,-1), (0,1)) # (dr, dc)
 
    #큐에 시작위치를 저장
    q.append((sr, sc))
    size = 1 # (sr, sc) 위치를 영역으로 카운트

    # 영영으로 중복카운트가 되지 않도록 해야 함 (paper[sr][sc]에 0이 아닌 값으로 변경)
    paper[sr][sc] = 1 # 1은 직사각형의 내부, 이미 카운트된 영역


    # 주변 탐색(큐가 빌때까지)
    while q:
        r, c = q.popleft()
        # 상하좌우 탐색
        for dr, dc in d:
            nr, nc = r + dr, c + dc     

            # 1. 범위 체크    # # 
    # Fill_Paper(paper)

    # Cound_Area(paper)
            if (not 0 <= nr < R) or (not 0 <= nc < C): continue
            # 2. 직사각형의 내부, 이미 카운트된 영역
            if paper[nr][nc] == 1: continue

            # 0인 곳이고 영역으로 카운트
            size += 1
            paper[nr][nc] = 1     # 영역으로 중복 카운트되지 않도록
            q.append((nr,nc))

    return size



def solve():
    list_size = []
	#모눈종이를 순차적으로 탐색하면서 직사각형의 내부가 아닌 곳에서 영역 판단
    for r in range(R):
        for c in range(C):
            if paper[r][c] == 0:
                list_size.append(Flood_Fill(r,c)) # (r,c) 와 인접한 곳들로 구성된 영영의 크기
    
    list_size.sort()
    return list_size

# 여기서부터 작성
# 모눈종이에 직사각형의 내부를 1로 표시
paper = Fill_Paper()

sol = solve()


# 출력하는 부분 
print(len(sol))
print(*sol)
