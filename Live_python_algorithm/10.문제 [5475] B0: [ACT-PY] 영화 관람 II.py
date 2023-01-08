# 문제 [5475] B0: [ACT-PY] 영화 관람 II

# 문제 설명
# 영화 보는걸 좋아하는 철수가 드디어 연애를 하게 되었다. 여자친구랑 하루 종일 영화를 보려고 하는데 여자친구는 2시간 미만의 짧은 영화는 싫어한다.
# 극장에 알아보니 N개의 영화가 상영될 예정이다.
# 한 영화를 보는 중에 다른 영화를 볼 수는 없으며 영화가 끝난 후에 다른 영화를 볼 수 있다.
# 한 영화의 종료시간과 다음에 보고자 하는 영화의 시작시간이 같다면 관람할 수 있는데 상영시간이 2시간 미만은 볼 수 없다.
# N개의 영화의 시작시간과 종료시간이 주어질 때 철수가 여자친구와 관람할 수 있는 최대 영화의 수를 구하라.
# * 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.
# import sys

# def Input_Data():
# 	readl = sys.stdin.readline
# 	N = int(readl())
# 	info = [list(map(int,input().split())) for _ in range(N)]
# 	return N, info


# sol = -1
# # 입력받는 부분
# N, info = Input_Data()
 
# # 여기서부터 작성


# # 출력하는 부분 
# print(sol)
# 입력 설명
# 첫 줄에 영화의 수 N이 입력된다. (3≤N≤100,000)
# 둘째 줄부터 N개의 줄에 영화시작시간과 종료시간이 공백으로 구분되어 입력된다.
# (1≤시간≤100,000,000) 종료시간이 시작시간보다 크다.

# 출력 설명
# 관람할 수 있는 최대영화의 수를 출력하라.

# 입력 예시
# 5
# 7 8
# 1 2
# 18 20
# 1 3
# 13 15
# 출력 예시
# 3

import sys
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int,input().split())) for _ in range(N)]
    return N, info
 
def solve():
        # 영화상영시간 정보를 각 영화의 종료시간 기준 오름차순으로 정렬
        info.sort(key=lambda x : x[1])
 
        cnt = 0 # 선택된 영화의 개수
        last = 0 # 이전에 선택된 영화의 종료시간
 
        for s, e in info:
                if e - s < 2: continue # 상영시간 2시간 미만인 영화는 볼수 없음
                if last > s : continue # 이전에 선택된 영화와 상영시간이 겹치므로 볼수 없음
 
                # 선택가능한 영화임
                cnt += 1
                last = e # 새로 선택된 영화의 종료시간으로 갱신
        return cnt
 
sol = -1
# 입력받는 부분
N, info = Input_Data()
  
# 여기서부터 작성
sol = solve()
 
# 출력하는 부분 
print(sol)