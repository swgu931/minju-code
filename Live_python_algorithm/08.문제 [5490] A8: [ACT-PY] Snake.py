# 문제 [5490] A8: [ACT-PY] Snake

# 문제 설명
# “Snake” 라는 도스 게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 과일을 먹으면 뱀의 길이가 늘어난다. 뱀이 상하좌우로 기어다니다가 벽 또는 자기자신과 부딪히면 게임이 끝난다.
 
# 게임은 N*N 정사각형 격자에서 진행되며, 몇 개의 칸에는 과일이 놓여있다. 격자 상하좌우 가장자리 끝은 벽이다. 게임 시작 시 뱀 위치는 좌상단, 즉 (1, 1)에서 시작하며 뱀 길이는 1이고 오른쪽을 향해 있다.
 
# 매 초마다 이동을 하는데 다음과 같은 규칙이 있다
# 1.    먼저 뱀은 몸길이를 늘려 머리를 다음 칸으로 이동한다.
# 2.    만약 이동한 칸에 과일이 있다면 이 상태가 유지된다. 즉, 몸길이가 1 증가한 것이다.
# 3.    만약 이동한 칸에 과일이 없다면 몸길이가 원상태로 돌아와야 한다. 이때 꼬리가 위치한 칸을 비우게 된다.
 
# 정사각형 격자의 크기 N과 과일의 위치, 뱀의 이동경로가 주어졌을 때, 이 게임이 몇 초 후에 끝나는지 구하시오
# * 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.
# import sys


# def Input_Data():
# 	readl = sys.stdin.readline
# 	N = int(readl())
# 	K = int(readl())
# 	pos = [tuple(map(int, readl().split())) for _ in range(K)]
# 	L = int(readl())
# 	cmd_list = [list(readl().split()) for _ in range(L)]
# 	cmd_list = [[int(c[0]),c[1]] for c in cmd_list]

# 	return N, K, pos, L, cmd_list


# sol = -1
# # 입력받는 부분
# N, K, pos, L, cmd_list = Input_Data()

# # 여기서부터 작성


# # 출력하는 부분
# print(sol)
# 입력 설명
# 첫 번째 줄에는 정사각형 격자의 크기 N(2≤N≤100)이 입력된다.
# 두 번째 줄에는 과일의 개수 K(0≤K≤100)가 입력된다.
# 다음 줄부터 K줄에 걸쳐 과일 정보가 r(세로), c(가로) 순으로 공백으로 구분되어 입력된다. 시작위치인 (1, 1) 위치에는 과일이 없다.
# 다음 줄에 뱀 이동경로 개수 L(1≤L≤100)이 입력된다.
# 다음 줄부터 L줄에 걸쳐 뱀 이동 경로가 정수 X(1≤X≤10,000), 문자 C(‘L’ or ‘D’)가 공백으로 구분되어 입력된다. 게임 시작 시간으로부터 X초 후에 C 방향으로 전환한다는 의미이다. ‘L’은 왼쪽으로 90도, ‘D’는 오른쪽 90 전환을 의미한다.
# 출력 설명
# 몇 초 후에 이 게임이 끝나는지 출력한다.
# 입력 예시
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
# 출력 예시
# 9

import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    K = int(readl())
    pos = [tuple(map(int, readl().split())) for _ in range(K)]
    L = int(readl())
    cmd_list = [list(readl().split()) for _ in range(L)]
    cmd_list = [[int(c[0]),c[1]] for c in cmd_list]
 
    return N, K, pos, L, cmd_list
 
def solve():
        # 게임 격자
        stage = [[0] * (N+1) for _ in range(N+1)] # 뱀: 1, 과일: 2
 
        # 격자에 과일표시
        for r, c in pos:
                stage[r][c] = 2
 
        # 방향 순서에 따른 변위('D' : 오른쪽으로 90도 전환)
        # 뱀위 시작방향은 오른쪽이고 'D'의 방향 순서(우하좌상)
        d = ((0,1), (1,0), (0,-1), (-1,0)) # (dr, dc)
 
        # 뱀위 초기 위치
        stage[1][1] = 1
        snake = deque([(1,1)])
 
        # 상태 변수(뱀의 머리위치, 현재 방향, 시간)
        r, c, cur_dir, t = 1, 1, 0, 0 # cur_dir는 현재 방향(d의 인덱스로 표시 , 오른쪽)
        idx = 0 # 처리할 이동 경로의 인덱스
 
        # 뱀의 이동을 시뮬레이션
        while 1:
                dr, dc = d[cur_dir]
                r, c, t = r + dr, c + dc, t + 1
                 
                # 벽에 부딪혀서 끝
                if not 1 <= r <= N: return t
                if not 1 <= c <= N: return t
                # 자기 몸에 부딪혀서 끝
                if stage[r][c] == 1: return t
                # 뱀의 머리가 이동한 위치에 과일이 없었다면 꼬리를 제거
                if stage[r][c] == 0:
                        tail_r, tail_c = snake.popleft()
                        stage[tail_r][tail_c] = 0
 
                # 뱀의 머리 위치를 큐에 저장하고 표시
                snake.append((r,c))
                stage[r][c] = 1
 
                # 이동경로에 의해 방향 전환
                if t == cmd_list[idx][0]:
                        cur_dir = (cur_dir + 1)%4 if cmd_list[idx][1] == 'D' else (cur_dir - 1 + 4)%4
                        idx += 1
 
sol = -1
# 입력받는 부분
N, K, pos, L, cmd_list = Input_Data()
 
# 여기서부터 작성
sol = solve()
 
# 출력하는 부분
print(sol)