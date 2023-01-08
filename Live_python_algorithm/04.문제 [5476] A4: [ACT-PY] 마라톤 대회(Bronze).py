# 문제 [5476] A4: [ACT-PY] 마라톤 대회(Bronze)

# 문제 설명
# 학생들이 건강하지 못하다고 생각한 선생님은 학생들을 위한 마라톤 대회를 열었고, 우승 후보인 기연이도 이 대회에 참가할 예정이다.
 
# 마라톤 코스는 N(3≤N≤100,000)개의 체크 포인트로 구성되어 있으며, 1번 체크포인트에서 시작해서 모든 체크 포인트를 순서대로 방문한 후 N번 체크포인트에서 마라톤이 끝난다. 기연이는 우승해야 한다는 부담감 때문에 중간에 있는 체크포인트 한 개를 몰래 건너 뛰려고 한다. 단, 1번과 N번 체크포인트는 건너 뛰지 않을 생각이다.
 
# 기연이가 체크포인트 한 개를 # 실행시간 제한: 1 Sec  메모리사용 제한: 128 MB
# 제출: 586  통과: 42.7%
# [제출]건너뛰면서 달릴 수 있다면, 과연 달려야 하는 최소 거리는 얼마일까?
 
# 참고로, 마라톤 대회는 수원시내 한복판에서 진행될 예정이기 때문에 거리는 “맨하탄 거리”로 측정한다. 위치(X1, Y1)와 위치(X2, Y2)의 거리는 |X1-X2| + |Y1-Y2|이다. (|X|는 절대값 기호이다)
# * 입출력 Template이 필요한 경우 CPython 제출은 다음 코드를 복사하여 코드를 작성하시오.
# import sys

# def Input_Data():
# 	readl = sys.stdin.readline
# 	N = int(readl())
# 	pos = [list(map(int,readl().split())) for _ in range(N)]
# 	return N, pos

# sol = -1
# # 입력 받는 부분
# N, pos = Input_Data()

# # 여기서부터 작성


# # 출력하는 부분
# print(sol)

# 입력 설명
# 첫 번째 줄에는 체크포인트 수 N이 입력된다
# 두 번째 줄부터 N줄에 걸쳐 각 체크포인트의 X, Y좌표가 공백으로 구분되어 입력된다
# (-1,000≤X≤1,000), (-1,000≤Y≤1,000)
# 체크포인트는 방문해야 하는 순서대로 입력된다. 동일한 위치에 여러 체크포인트가 있을 수 있다. 기연이는 이러한 체크포인트가 있을 때도 한 체크포인트만 건너 뛰지 동일 위치의 모든 체크포인트를 건너 뛰지 않는다.
# 출력 설명
# 기연이가 체크포인트 1개를 건너뛰고 달릴 수 있는 최소 거리를 출력한다
# 입력 예시
# 4
# 0 0
# 8 3
# 11 -1
# 10 0
# 출력 예시
# 14

import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [list(map(int,readl().split())) for _ in range(N)]
	return N, pos

def solve():  # Time limit exceeded
    # 달린 거리 중 최소값 (불가능한 큰값으로 초기화)
    min_dist = 4000*100000  # 체크포인트간 최대거리 * 모든 체크포인트의 개수
    # 건너뛰려는 체크포인트 2~N-1 (pos index : 1~N-2)
    for s in range(1, N-1):
        sum_dist = 0 # s체크포인트를 건너뛰고 달릴때의 누적거리
        # 1 ~ N 까지 s체크포인트를 건너뛰고 달릴때 거리
        # i <-> i+1 체크포인트 간의 거리, i는 1~N-1 (pos index: 0~N-2)  
        for i in range(0, N-1):
            if i == s: continue
            if i+1 == s: sum_dist += abs(pos[i][0] - pos[i+2][0]) + abs(pos[i][1] - pos[i+2][1])
            else: sum_dist += abs(pos[i][0] - pos[i+1][0]) + abs(pos[i][1] - pos[i+1][1])
        if min_dist > sum_dist:
            min_dist = sum_dist
    return min_dist


def solve2():
    # 특정 체크포인트를 건너뛸때 줄어드는 거리가 최대인 값
    max_dist = 0 # 최대값 갱신(초기값은 불가능한 작은 값)
    #건너뛰려는 체크포인트는 2~N-1(pos index : 1~N-2)
    for s in range(1, N-1):
            dist = abs(pos[s-1][0] - pos[s][0]) + abs(pos[s-1][1] - pos[s][1]) + \
                    abs(pos[s][0] - pos[s+1][0]) + abs(pos[s][1] - pos[s+1][1]) - \
                    (abs(pos[s-1][0] - pos[s+1][0]) + abs(pos[s-1][1] - pos[s+1][1]))
            if max_dist < dist :
                    max_dist = dist
                        
    # 모든 체크포인트를 거쳐서 달릴때의 거리
    total_dist = 0
    # i <-> i+1 체크포인트 간의 거리, i는 1~N-1(pos index : 0~N-2) 
    for i in range(0, N-1) :
            total_dist += abs(pos[i][0] - pos[i+1][0]) + abs(pos[i][1] - pos[i+1][1])
        
    return total_dist - max_dist
# 실행시간 제한: 1 Sec  메모리사용 제한: 128 MB
# 제출: 586  통과: 42.7%
# [제출]
sol = -1
# 입력 받는 부분
N, pos = Input_Data()

# 여기서부터 작성
# sol = solve()
sol = solve2()

# 출력하는 부분
print(sol)


