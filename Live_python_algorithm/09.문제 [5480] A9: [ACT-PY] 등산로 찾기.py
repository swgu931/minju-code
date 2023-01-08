# 문제 [5480] A9: [ACT-PY] 등산로 찾기

# 문제 설명
# n×n의 행렬로 지형도가 표시된 산이 있다. 행렬의 원소의 값은 양의 정수 값으로 그 위치에서의 높이를 말해준다. 등산가들은 산의 바깥지역(높이 0)으로부터 목적지에 도달하기 위하여 가장 경제적인 루트를 탐색하려고 한다. 경제적인 경로란 힘을 가장 적게 들이고 목적지까지 올라갈 수 있는 길을 말한다.
 
# 예를 보면서 설명해보자. 다음은 행렬 Mount[5,5]로 표시된 산악지형이다. 산의 목적지는 Mount[3,3]의 위치에 있으며, 그 높이는 6이다. 그리고 이 산의 바깥지역은 모두 해발이 0이다. 등산가가 산에 오르는 시작점의 위치는 산의 바깥지역의 어디에서 시작해도 좋다.
 

# 등산가는 어떤 한 지역에서 그 위치에 인접한 네 방향(위, 아래, 왼쪽, 오른쪽)으로만 움직일 수 있다. 인접한 지역으로 움직일 수 있는 경우는 (1) 평지로 이동할 경우, (2) 내려갈 경우, (3) 올라갈 경우의 세 가지이다. 이 세 가지 경우에 필요한 "힘"의 양은 다음과 같이 표현될 수 있다.
 
 
# (1)인접한 같은 높이의 지역을 수평 이동할 경우에는 그냥 평지를 걸어가면 되므로 힘이 전혀 들지 않는다고 가정한다. 예를 들면 Mount[5,2]에서 Mount[5,3]으로 이동하는 경우와 Mount[4,5]에서 Mount[5,5]로 이동하는 경우에는 전혀 힘이 들지 않는다.
#  (2)내리막길을 따라갈 경우(예를 들면, Mount[2,3]에서 Mount[2,2]로 갈 때)에는 그 높이 차이만큼의 힘이 든다. 즉 이 경우에는 5-3=2만큼의 힘이 든다.
#  (3)오르막길을 오를 경우에는 이동할 두 지역의 높이 차의 제곱만큼의 힘이 든다. 즉 Mount[1,2]에서 Mount[1,3]으로 갈 경우는 (4-2)2=4 만큼의 힘이 든다.
# * 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.
# import sys


# def Input_Data():
# 	readl = sys.stdin.readline
# 	N = int(readl())
# 	r_top, c_top = map(int, readl().split())
# 	map_mountine = [[0] + list(map(int,readl().split())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
# 	return N, r_top, c_top, map_mountine


# sol = -1
# # 입력받는 부분
# N, r_top, c_top, map_mountine = Input_Data()

# # 여기서부터 작성


# # 출력하는 부분
# print(sol)
# 입력 설명
# 첫째 줄에는 산의 크기인 Mount[n,n]의 n값이 주어지고, 두 번째 줄에는 목적지의 위치 Mount[y,x]의 y, x값이 주어진다.
# 단, Mount[n,n]에서 n은 100이하이고, 각 지형의 최대 높이는 50이하라고 가정한다.
# 그 다음 n개의 줄은 산의 크기에 따른 각 지점의 높이가 양의 정수 값으로 주어진다.
# 출력 설명
# 첫째 줄에 목적지까지 도달하는 가장 경제적인 경로를 따라 올라가는데 사용된 힘을 출력한다.
# 입력 예시
# 5
# 3 3
# 1 2 4 3 2
# 1 3 5 4 4
# 2 3 6 5 1
# 3 1 4 1 3
# 2 3 3 5 3
# 출력 예시
# 8
# 부가정보
# 경로는 다음과 같다.
# 2[1,5]->3[1,4]->4[2,4]->5[3,4]->6[3,3]
#  = 2*2 + 1*1 + 1*1 + 1*1 + 1*1
#  = 8

import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    r_top, c_top = map(int, readl().split())
    map_mountine = [[0] + list(map(int,readl().split())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
    return N, r_top, c_top, map_mountine
 
def BFS():
        # 상하좌우 변위
        d = ((-1,0), (1,0), (0,-1), (0,1))
 
        q = deque()
         
        # 1. 필요시 초기화(큐, 방문정보, ...)
        # 각 위치의 현재까지 최소 힘의 양
        # 최소값 갱신을 해야 하므로 초기값은 불가능한 큰값
        # 50*50*100*100 => 한칸 이동시 드는 최대힘 * 최대크기의 모든 칸을 이동하는 경우로 가정
        visit = [[50*50*100*100] * (N+2) for _ in range(N+2)]
         
        # 2. 큐에 초기값 저장(현재 문제는 시작위치가 여러개)
        # 1) 시작 위치가 될수 있는 바깥지역의 모든 위치를 큐에 저장하고 시작
        # 2) 바깥 지역의 위치중 하나의 위치만 큐에 저장하고 시작(나머지 바깥지역들은 드는 힘이 0으로 탐색되어 큐에 저장될것임)
        q.append((0,0))
        visit[0][0] = 0 # 시작위치이고 드는 힘은 0
         
        # 3. 주변탐색 반복(큐가 빌때까지)
        while q:
                r, c = q.popleft()
 
                # 주변 4방향 탐색
                for dr, dc in d:
                        nr, nc = r + dr, c + dc
 
                        # 범위체크
                        if not 0 <= nr <= N+1: continue
                        if not 0 <= nc <= N+1: continue
                         
                        # (r,c) -> (nr,nc)로 갈때 드는 힘계산
                        power = map_mountine[r][c] - map_mountine[nr][nc]
                        if power < 0 : power *= power
 
                        # (nr,nc)의 힘의 양과 ((r,c)의 힘의 양 + power)를 비교해서 중복탐색 여부 판단
                        if visit[nr][nc] <= visit[r][c] + power: continue
 
                        # 기존의 힘의 양보다 (r,c)에서 (nr,nc)로 가는 힘의 양의 더 작다.
                        q.append((nr,nc))
                        visit[nr][nc] = visit[r][c] + power
                         
        # 4. 탐색 완료처리
        return visit[r_top][c_top]
 
sol = -1
# 입력받는 부분
N, r_top, c_top, map_mountine = Input_Data()
 
# 여기서부터 작성
sol = BFS()
 
# 출력하는 부분
print(sol)
