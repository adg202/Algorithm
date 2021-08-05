#기능개발
def solution(progresses, speeds):
    answer = []
    deploy = 0

    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1

        if i == 0:
            deploy = count
            app = 0
        else:
            if count > deploy:
                deploy = count
                answer.append(app + 1)
                app = 0
            else:
                app += 1
    answer.append(app + 1)

    return answer
