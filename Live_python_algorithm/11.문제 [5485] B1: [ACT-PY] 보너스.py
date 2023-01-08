# 문제 [5485] B1: [ACT-PY] 보너스

# 문제 설명
# 중소기업인 K 회사에서 직원들에게 보너스를 지급하려고 한다.
# 그런데 직원들의 자존심이 강해서 상급자들이 직급이 낮은 사람보다는 한 푼이라도 더 받기를 원한다.
# 단, 자기랑 직접적 관련이 없는 사람의 보너스 금액에는 관심 없다.
# 중소기업 특성상 정확한 직급이 존재하지 않고 누가 누구 상급자고 하급자인지만 정해져 있는 상황에서 사장은 골치가 아프다.
# 예를 들어 아래와 같은 조직인 경우에는 아래와 같다.
# 편의상 이름은 숫자로 대체한다.
# 1은 언제나 사장이다.
 

#  5명이 있고 보너스 금액은 51, 30, 35, 30, 31 일 경우 1번부터 51, 35, 31, 30, 30으로 배정하면 된다.
# 중소기업 사장을 도와서 모두가 만족할 수 있는 보너스 금액을 배정하자.
# * 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.
# import sys


# def Input_Data():
# 	readl = sys.stdin.readline
# 	N, M = map(int, readl().split())
# 	relation = [list(map(int, readl().split())) for i in range(M)]	
# 	bonus = list(map(int, readl().split()))
# 	return N, M, relation, bonus


# sol = []
# # 입력받는 부분
# N, M, relation, bonus = Input_Data()

# # 여기서부터 작성


# # 출력하는 부분
# print(*sol[1:])
# 입력 설명
# 첫 줄에 N과 M이 입력된다. N은 직원 수 (3≤N≤10), M은 상하관계의 개수(2≤M≤100) 이다.
# 다음 줄부터 M줄에 걸쳐 상하관계가 입력된다. 각 줄에는 상급자 하급자 순으로 입력되며 공백으로 구분된다. (상하관계 오류가 발생하는 입력은 없음)
# 마지막 줄에는 보너스 금액이 N개만큼 공백으로 구분되어 입력된다. 보너스 금액은 1이상 1,000,000 이하 이다.
# 출력 설명
# 1번부터 N번까지 순서대로 공백으로 구분하여 보너스 금액을 출력한다. (답이 여러 개일 경우 그 중 한가지만 출력하면 됨)
# 입력 예시
# 5 6
# 1 2
# 2 3
# 1 4
# 2 4
# 1 5
# 3 5
# 51 30 35 30 31
# 출력 예시
# 51 35 31 30 30 

import sys
 
 
def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    relation = [list(map(int, readl().split())) for i in range(M)]  
    bonus = list(map(int, readl().split()))
    return N, M, relation, bonus
 
def isPossible(n, bonus):
        # 상하급자 관계 확인할 대상은 1~n-1(보너스 지급이 된 직원들을 대상)
        for i in range(1, n):
                # n번 직원이 상급자이고 i번 직원이 하급자
                if link[n][i] == 1 and bonus <= sol[i]: return False
                # n번 직원이 하급자이고 i번 직원이 상급자
                if link[i][n] == 1 and bonus >= sol[i]: return False
        return True
 
 
def DFS(n):
        # 종료조건
        # 모든 직원에게 상하관계 위배없이 보너스 지급이 완료(탐색을 종료)
        if n == N+1 : return True
 
        # n번 직원에게 i번 보너스 지급 시도
        for i in range(N):
                if used[i] == 1: continue # i번 보너스는 이미 지급됨
                # 상하관계 위배 판단(리턴이 True : 상하관계 위배되지 않음, False : 상하관계 위배됨)
                if isPossible(n, bonus[i]) == False : continue
 
                used[i] = 1 # i번 보너스 지급 표시
                sol[n] = bonus[i] # n번 직원에게 i번 보너스를 지급
                if DFS(n+1) : return True
                used[i] = 0 # i번 보너스 미사용 표시
                sol[n] = 0
        return False
 
def Make_Link():
        # [ 상급자번호 ][ 하급자번호 ] (1: 상하급자 관계임, 0: 무관계)
        link = [[0] * (N+1) for _ in range(N+1)]
        for r, c in relation:
                link[r][c] = 1
        return link
 
sol = []
# 입력받는 부분
N, M, relation, bonus = Input_Data()
 
# 여기서부터 작성
# 보너스 사용  여부
used = [0] * N # 1: 사용됨, 0: 미사용
# 각 직원이 지급받은 보너스 금액(인덱스 1~N)
sol = [0] * (N+1)
# 상하관계정보를 리스트로 표현
link = Make_Link()
 
DFS(1) # 1번 직원부터 보너스 지급 시도
 
# 사장이 가장 큰 보너스 금액을 지급받음
'''
bonus.sort()
sol[1] = bonus[-1]
used[-1] = 1
 
DFS(2) 
'''
 
# 출력하는 부분
print(*sol[1:])