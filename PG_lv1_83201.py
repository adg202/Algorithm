#프로그래머스 위클리 챌린지 2주차
#상호 평가

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''

    for i in range(len(scores)):
        #학생이 받은 점수가 들어갈 리스트
        tmp = []

        for j in range(len(scores)):
            tmp.append(scores[j][i])

        #조건: 자신에게 준 점수가 최고점 또는 최저점일 때, 그 점수가 리스트 내에 유일하다면 제거
        if tmp[i] == min(tmp) or tmp[i] == max(tmp):
            if tmp.count(tmp[i]) == 1:
                tmp.remove(tmp[i])

        score = sum(tmp) / len(tmp)
        answer += grade(score)

    return answer