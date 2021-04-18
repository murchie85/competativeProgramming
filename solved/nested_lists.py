# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    array = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        array.append([score,name])
    
    array.sort()

    scoreArray = [x[0] for x in array]
    scoreArray = list(dict.fromkeys(scoreArray))

    target = scoreArray[1]

    targetArray = []
    for item in array:
        if item[0] == target:
            targetArray.append(item)
    studentArray = []
    for item in targetArray:
        studentArray.append([item[1],item[0]])
    studentArray.sort()
    [print(x[0]) for x in studentArray]

