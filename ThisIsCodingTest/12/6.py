# Q12 기둥과 
# 난이도 중하 | 풀이 시간 40분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 2020 카카오 신입 공채 | 링크 https://programmers.co.kr/learn/courses/30/lessons/60059
# 풀이 시간 : 20분 소요
'''
def solution(n, build_frame):
    data = [[0] * n for _ in range(n)]
    
    x = build_frame[index][0][0][0]
    y = build_frame[0][index][0][0]
    a = build_frame[0][0][index][0]
    b = build_frame[0][0][0][index]
    data[x][y] = 1
        
    while True :
        if a == 0 and b == 0:
            data[x][y + 1] = 0
        elif a == 0 and b == 1:
            data[x][y + 1] = 1
        elif a == 1 and b == 0:
            data[x + 1][y] = 0
        elif a == 1 and b == 1:
            data[x + 1][y] = 1
    data[x][y]
    answer = [[]]
    return answer
'''

# 코드 리뷰

# A12.py 답안 예시
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer) :
    for x, y, stuff in answer :
        if stuff == 0 : # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위' 라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer :
                continue
            return False # 아니라면 거짓(False) 반환
        elif stuff == 1 : # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer) :
                continue
            return False # 아니라면 거짓(False) 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame : # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0 : # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer) : # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1 : # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
            if not possible(answer) : # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환
