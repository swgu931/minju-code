
#01.문제 [6040] A1: [ACT-PY] 색종이(중).png
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 둘레의 길이를 구하는 프로그램을 작성하시오.

# 예를 들어 흰색 도화지 위에 네 장의 검은색 색종이를 <그림 1>과 같은 모양으로 붙였다면 검은색 영역의 둘레는 96 이 된다.


# 입력 설명
# 첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다.

# 출력 설명
# 첫째 줄에 색종이가 붙은 검은 영역의 둘레의 길이를 출력한다.

# 입력 예시
# 4
# 3 7
# 5 2
# 15 7
# 13 14

# 출력 예시
# 96


import sys 

def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    info = [list(map(int, readl().split())) for _ in range(N)] 
    return N, info 

# 도화지에 색종이가 놓여지는 곳을 1 로 표시
def Fill_Paper(paper):
    for sc, sr in info:
        for r in range(sr, sr+10):
            for c in range(sc, sc+10):
                paper[r][c] = 1

def Count_Edge(paper):
    # 상화좌우 변위 
    d = ((-1,0), (1,0), (0,-1), (0,1)) # (dr, dc)
    edge = 0 # 둪레의 길이를 누적

    # 도화지에서 색종이가 놓인 곳에서 상하좌우 판단
    for r in range(100):
        for c in range(100):
            if paper[r][c] == 1:
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if (not 0 <= nr < 100) or (not 0 <= nc < 100) or paper[nr][nc] == 0:
                        edge += 1
    
    return edge


def solve():
    # 도화지
    paper = [[0] * 100 for _ in range(100)]
    
    Fill_Paper(paper)

    return Count_Edge(paper)



sol = 0 

# 입력받는 부분 
N, info = input_data() 

# 여기서부터 작성 
sol = solve()





# 출력하는 부분 

print(sol) 



