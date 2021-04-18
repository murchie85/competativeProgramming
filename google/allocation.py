"""
LESSON: I was reading in values for anarrayusing input.split()
What i should have been doing was converting each val to an int first so the sort function can work

"""

t = int(input())


for test in range(1, t+1):
    s = input().split(' ')
    a = list(map(int,input().split()))
    
    N = s[0]
    B = s[1]
    
    budget = int(B)
    array = sorted(a)
    purchased = 0
    
    for house in array:
        if budget >=0:
            if (budget - int(house)) >= 0:
                budget -= int(house)
                purchased+=1
    
    print("Case #{}: ".format(str(test)),str(purchased))

