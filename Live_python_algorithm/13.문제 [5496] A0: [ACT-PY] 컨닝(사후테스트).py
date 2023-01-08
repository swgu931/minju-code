# 문제 [5496] A0: [ACT-PY] 컨닝

# 문제 설명
# 세계 프로그래밍 경진 대회의 참가자들은 총 N명이고 각각 1개의 솔루션 파일 F1, …, FN을 채점 시스템에 제출했습니다. 심사위원들은 최종 결과를 발표하기 전에 남의 것을 컨닝한 사람이 있는지 찾아내려고 한다. 이 대회의 주최측은 두 파일을 비교해서 너무 비슷한지 아닌지 판별하는 프로그램이 있다.
# 그러나 파일의 수가 상당히 많아서 모든 쌍을 비교하는데 너무 많은 시간 걸립니다. 따라서, 파일 크기가 너무 다른 경우에는 그러한 쌍을 검사하지 않고 넘어가기로 했다.
# 좀더 정확하게 하기 위해서, 심사위원들은 두 파일이 있을 때, 작은 파일의 크기가 큰 파일의 크기의 90%미만인 경우 이러한 쌍은 검사하지 않고 넘어가기로 했다. 따라서 비교 프로그램은 i≠j이고, size(Fi)≤size(Fj) 이면서 size(Fi)≥0.9*size(Fj) 인 파일의 쌍(Fi, Fj)만을 조사해야 한다.
# 검사해야 할 파일 쌍의 수를 계산하는 프로그램을 작성하시오.
# * 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.
# import sys


# def Input_Data():
# 	readl = sys.stdin.readline
# 	N = int(readl())
# 	list_file = list(map(int, readl().split()))
# 	return N, list_file


# sol = -1
# # 입력받는 부분
# N, list_file = Input_Data()

# # 여기서부터 작성


# # 출력하는 부분
# print(sol)
# 입력 설명
# 첫 번째 줄에는 제출한 솔루션의 개수 N이 입력된다.
# 두 번째 줄에는 각 솔루션 파일의 크기 size(F1), size(F2), …, size(FN)이 입력된다. (1≤N≤100,000) (1≤size(Fi)≤100,000,000)

# 출력 설명
# 검사해야 하는 파일의 개수를 출력한다.

# 입력 예시
# 5
# 1 1 1 1 1
# 출력 예시
# 10

import sys
from collections import deque
from bisect import bisect_left, bisect_right

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	list_file = list(map(int, readl().split()))
	return N, list_file


# # 1. 파일크기 비교
# def compare(size_fi, size_fj):
#     if size_fi <= size_fj and size_fi >= 0.9*size_fj:
#         return size_fi
#     elif size_fj <= size_fi and size_fj >= 0.9*size_fi:
#         return size_fj
#     else:
#         return 0    

# # 시간초과
# def solve():
#     num = 0
#     for i in range(N-1):  # 1~N ---> 0~N-1, loop 0~N-2
#         for j in range(i+1, N):
#             # if i == N-1 and j == N-1 break
#             ret = compare(list_file[i], list_file[j])

#             if ret != 0:
#                 num += 1
        
#     return num
 
def solve2():
    num = 0
    list_file.sort()
    for i in range(N):
        ret = bisect_left(list_file, list_file[i]*0.9, 0, i)
        if ret < i: num += i - ret

    return num

sol = -1
# 입력받는 부분
N, list_file = Input_Data()

# 여기서부터 작성

sol = solve2()


# 출력하는 부분
print(sol)

