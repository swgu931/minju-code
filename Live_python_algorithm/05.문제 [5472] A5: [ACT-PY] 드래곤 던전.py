# 문제 [5472] A5: [ACT-PY] 드래곤 던전

# 문제 설명
# 당신은 드래곤 던전에 갇히고 말았다. 여기서 탈출하는 가장 빠른 길은 무엇일까?
# 드래곤 던전은 각 변의 길이가 1인 정육면체(3차원 공간)로 이루어져있다.
# 각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있다.
# 당신은 각 칸에서 인접한 6개의 칸(동, 서, 남, 북, 상, 하)으로 1분의 시간을 들여 이동할 수 있다. 즉, 대각선으로 이동하는 것은 불가능하다.
# 그리고 드래곤 던전의 바깥면도 모두 금으로 막혀있어서 출구를 통해서만 탈출할 수 있다.
# 당신은 드래곤 던전을 탈출할 수 있을까? 그렇다면 시간은 얼마나 걸릴까? 
# * 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.
# import sys
 
# def Input_Data():
# 	readl = sys.stdin.readline
# 	L, R, C = map(int, readl().split())
# 	map_dungeon = [[list(readl().strip())for r in range(R+1)] for l in range(L)]
# 	return L, R, C, map_dungeon

# sol_list = []
# while 1:  
# 	# 입력 받는 부분  
# 	L, R, C, map_dungeon = Input_Data()
# 	if L == 0 and R == 0 and C == 0: break
# 	# 여기서부터 작성    

# print(*sol_list, sep='\n') 
# 입력 설명
# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 테스트 케이스는 세개의 정수 L, R, C로 시작한다.
# L(1 ≤ L ≤ 30)은 드래곤 던전의 층 수이다. R(1 ≤ R ≤ 30)과 C(1 ≤ C ≤ 30)는 드래곤 던전의 한 층의 행과 열의 개수를 나타낸다.
# 그 다음 각 줄이 C개의 문자로 이루어진 R개의 행이 L번 주어진다. 각 문자는 드래곤 던전의 한 칸을 나타낸다.
# 금으로 막혀있어 지나갈 수 없는 칸은 '#'으로 표현되고, 비어있는 칸은 '.'으로 표현된다.
# 당신의 시작 지점은 'S'로 표현되고, 탈출할 수 있는 출구는 'E'로 표현된다.
# 각 층 사이에는 빈 줄이 있으며, 입력의 끝은 L, R, C가 모두 0으로 표현된다.
# 출력 설명
# 각 드래곤 던전에 대해 한 줄씩 답을 출력한다. 만약 당신이 탈출할 수 있다면 다음과 같이 출력한다.
# Escaped in x minute(s).
# 여기서 x는 드래곤 던전을 탈출하는 데에 필요한 최단 시간이다.
# 만일 탈출이 불가능하다면, 다음과 같이 출력한다.
# Trapped!
# 입력 예시
# 3 4 5
# S....
# .###.
# .##..
# ###.#

# #####
# #####
# ##.##
# ##...

# #####
# #####
# #.###
# ####E

# 1 3 3
# S##
# #E#
# ###

# 0 0 0
# 출력 예시
# Escaped in 11 minute(s).
# Trapped!

import sys
from collections import deque
  
def Input_Data():
    readl = sys.stdin.readline
    L, R, C = map(int, readl().split())
    map_dungeon = [[list(readl().strip())for r in range(R+1)] for l in range(L)]
    return L, R, C, map_dungeon
 
def BFS():
        # 상하동서남북 변위
        d = ((-1,0,0), (1,0,0), (0,0,1), \
             (0,0,-1), (0,1,0), (0,-1,0)) # (dl, dr, dc) => (층변위, 행변위, 열변위) L-1 -> 0 : 상 방향으로 가정
        q = deque()
        # 1. 필요시 초기화(큐, 방문(탐색)정보, ...)
        # 2. 큐에 초기값 저장(시작위치)
        start_pos = [(l,r,c) for l in range(L) for r in range(R) for c in range(C) if map_dungeon[l][r][c] == 'S']
        q.append((start_pos[0][0], start_pos[0][1], start_pos[0][2], 0)) # (층, 행, 열, 시간)
        # 중복 탐색을 배제
        # 1) 방문(탐색)정보 리스트에 표시(1: 탐색된 곳, 0: 탐색되지 않은 곳)
        # 2) map_dungeon에 표시('S'나 '.'이 아닌 값으로 변경)
        # '#'은 막힌 곳 또는 이미 탐색된 곳('#' 대신에 '@', '$' 등 '.'이 아닌 값으로 가능)
        map_dungeon[ start_pos[0][0] ][ start_pos[0][1] ][ start_pos[0][2] ]  = '#'
         
        # 3. 주변탐색 반복(큐가 빌때까지)
        while q:
                l, r, c, t = q.popleft()
 
                # 6방향 탐색
                for dl, dr, dc in d:
                        nl, nr, nc = l + dl, r + dr, c + dc
 
                        # 범위체크 먼저!
                        if not 0 <= nl < L: continue
                        if not 0 <= nr < R: continue
                        if not 0 <= nc < C: continue
                         
                        # 막힌 곳, 이미 탐색한 곳 체크
                        if map_dungeon[nl][nr][nc] == '#': continue
 
                        # 'E' 즉 출구에 도착한 경우
                        if map_dungeon[nl][nr][nc] == 'E': return t+1
 
                        # '.'인 경우
                        q.append((nl,nr,nc,t+1))
                        map_dungeon[nl][nr][nc] = '#' # 중복탐색 배제
                 
        # 4. 탐색 완료 처리
        # 'E' 출구에 도착할 수 없음
        return -1
 
sol_list = []
while 1:  
    # 입력 받는 부분  
    L, R, C, map_dungeon = Input_Data()
    if L == 0 and R == 0 and C == 0: break
    # 여기서부터 작성
    sol = BFS() # BFS는 출구에 도착할수 있는 최단 시간을 리턴(만약 도착할수 없는 상태였다면 -1을 리턴)
    if sol == -1 :sol_list.append("Trapped!")
    else : sol_list.append("Escaped in {} minute(s).". format(sol))
 
print(*sol_list, sep='\n')

