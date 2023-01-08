# 문제 [6041] A7: [ACT-PY] 크게 만들기

# 문제 설명
# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
# * 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.
# import sys
 
# def Input_Data():
#     readl = sys.stdin.readline
#     N, K = map(int, readl().split())
#     num = readl().strip()
#     return N, K, num
 
# sol = -1
# # 입력받는 부분
# N, K, num = Input_Data()

# # 여기서부터 작성

# # 출력하는 부분
# print(sol)

# 입력 설명
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

# 둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.
# 출력 설명
# 입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.
# 입력 예시
# 4 2
# 1924
# 출력 예시
# 94
# 부가정보
# [ 입력 예시 2 ]
# 4 2
# 1924

# [ 출력 예시 2 ]
# 94


# [ 입력 예시 3 ]
# 7 3
# 1231234


# [ 출력 예시 3 ]
# 3234


# [ 입력 예시 4 ]
# 10 4
# 4177252841


# [ 출력 예시 4 ]
# 775841

import sys
from collections import deque
  
def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    num = readl().strip()
    return N, K, num
 
def solve(K):
        stk = deque()
        l = []
        for n in num:
                # pop을 해야 하는 상황
                # 스택이 비어 있지 않아야하고 K가 0보다 큰값이고 스택의 마지막 값이 n보다 작으면 제거
                while len(stk) and K > 0 and stk[-1] < n :
                        stk.pop()
                        K -= 1
                # n을 스택에 push
                stk.append(n)
        # K가 0보다 큰값이라면 K번 pop을 해서 제거(N=10, K=2, num=9876543210 -> 답 : 98765432)
        while K > 0:
                stk.pop()
                K -= 1
         
        while stk:
                l.append(stk.popleft())
        return ''.join(l)
 
sol = -1
# 입력받는 부분
N, K, num = Input_Data()
 
# 여기서부터 작성
sol = solve(K)
 
# 출력하는 부분
print(sol)
 