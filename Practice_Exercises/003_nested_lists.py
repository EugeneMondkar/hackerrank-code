# Problem Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':

    students = list()
    scores = list()

    lowest_score = 9999
    highest_score = 0

    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score > highest_score:
            highest_score = score

        if score < lowest_score:
            lowest_score = score

        student = [name, score]
        students.append(student)
        scores.append(score)


    second_lowest = highest_score
    for score in scores:
        if score > lowest_score and score < second_lowest:
            second_lowest = score

    losers = list()

    for student in students:
        if second_lowest == student[1]:
            losers.append(student[0])

    losers.sort()

    # print(highest_score, lowest_score, second_lowest) 
    
    for loser in losers:
        print(loser)