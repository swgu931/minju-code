# 문제 [5484] B2: [ACT-PY] 사회적 거리두기

# 문제 설명
# 농부 John은 전염성이 높은 COWVID-19이 발생한 이후, 소들의 건강이 걱정되었다. 
# 병의 전염을 막기 위해서, 농부 John의 N마리 소들은 '사회적 거리두기' 실행하기로 결정하고 농장 전체에 흩어졌다. (2<=N<=105)
# 농부 John의 농장은 1차원 직선의 모양으로, M개의 서로 분리된 구간의 방목할 잔디가 구성되어 있다. (1<=M<=105)
# 소는 D의 값을 최대화하기 위해 각각 잔디구간의 정수 지점에 위치하려고 한다. 여기서 D는 가장 가까운 소 두 마리 사이의 거리를 말한다. 소가 D의 가능한 가장 큰 값을 가질수 있도록 도와주자.
# (입력 예시에 대한 상황이 아래 '부가정보'에 그림으로 잘 표현되어 있다. 해당 내용을 참고하자.)
# * 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.

# import sys

# def Input_Data():
# 	readl = sys.stdin.readline
# 	N, M = map(int,readl().split())
# 	intvals = [list(map(int,readl().split())) for _ in range(M)]
# 	return N, M, intvals


# sol = -1
# #입력받는 부분
# N, M, intvals = Input_Data()

# # 여기서부터 작성


# # 출력하는 부분
# print(sol)
# 입력 설명
# 첫째 줄에는 N과 M이 주어진다. (2<=N<=105, 1<=M<=105)
# 다음 M개 줄에는 잔디구간을 나타내는 두개의 정수 a,b가 주어진다.(0<=a<=b<=1018)
# 구간이 겹치거나 같은 지점에서 만나는 경우는 존재하지 않는다. 그리고 소들은 각 구간의 끝지점에도 서있을 수 있다.
# 출력 설명
# 가능 최대값 D를 출력하라. 모든 소들의 쌍은 D이상 떨어져 있어야 한다.
# 모든 입력은 0보다 큰 D값이 항상 존재한다.
# 입력 예시
# 5 3
# 0 2
# 4 7
# 9 9
# 출력 예시
# 2

import sys
 
def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int,readl().split())
    intvals = [list(map(int,readl().split())) for _ in range(M)]
    return N, M, intvals
 
def isPossible(d):
        # d간격으로 N마리의 소를 M개의 잔디 구간에 배치하는게 가능?
        last = intvals[0][0] # 이전 소가 배치된 위치,초기값 : 첫번째 소의 위치(정렬된 첫번째 잔디 구간의 시작위치)
        midx = 0 # 현재 소가 위치한 잔디 구간의 인덱스
 
        # N-1 마리의 소를 잔디구간에 배치 시도(첫번째소는 첫번째 잔디 구간의 시작위치에 배치)
        for _ in range(N-1):
                # 소를 배치할 잔디 구간을 찾기
                while midx < M and last + d > intvals[midx][1]:
                        midx += 1
                if midx == M : return False # 소를 배치하기 위한 잔디 구간이 존재 않음, 모든 소를 배치하는게 불가능
                 
                # 소를 배치하려는 위치(last + d)를 선택된 잔디구간(midx)의 시작위치 와 비교해서 결정
                last = intvals[midx][0] if intvals[midx][0] > last + d else last + d
        return True
 
def solve():
        # 잔디 구간의 정보를 시작위치 기준 오름차순 정렬
        intvals.sort()
 
        # 이진 탐색의 범위를 지정
        s, e = 0, (intvals[-1][1] - intvals[0][0]) // (N-1)# intvals[-1][1] - intvals[0][0] # 10**18
 
        # 탐색 가능한 범위가 존재하면
        while s <= e:
                m = (s+e)//2
                if isPossible(m): # 최소 m 간격으로 소들을 배치하는게 가능한지 판단
                        sol = m # m은 D 값이 될수 있는 후보
                        s = m + 1 # 더 큰값의 범위에서 찾도록 범위를 조정
                else :
                        e = m - 1 # 더 작은 값의 범위에서 찾도록 범위를 조정
        return sol
         
sol = -1
#입력받는 부분
N, M, intvals = Input_Data()
 
# 여기서부터 작성
sol = solve()
 
# 출력하는 부분
print(sol)

