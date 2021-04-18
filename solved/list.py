"""
https://www.hackerrank.com/challenges/python-lists/problem


Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]




"""



array = []
if __name__ == '__main__':
    N = int(input())
    

    def insertList(pos,num,array):
        array.insert(pos,num)
        return(array)

    def appendList(num,array):
        array.append(num)
        return(array)

    def printList(array):
        print(array)

    def removeList(num,array):
        array.remove(num)
        return(array)

    def sortList(array):
        array.sort()
        return(array)

    def popList(array):
        last = len(array) - 1
        array.pop(last)
        return(array)

    def reverseList(array):
        array.reverse()
        return(array)

    for i in range(0,N):
        comm = input().split()

        if(str(comm[0]) == 'insert'):
            array = insertList(int(comm[1]), int(comm[2]), array)

        if(str(comm[0]) == 'print'):
            printList(array)

        if(str(comm[0]) == 'append'):
            array = appendList(int(comm[1]), array)

        if(str(comm[0]) == 'remove'):
            array = removeList(int(comm[1]), array)

        if(str(comm[0]) == 'sort'):
            array = sortList(array)

        if(str(comm[0]) == 'pop'):
            array = popList(array)

        if(str(comm[0]) == 'reverse'):
            array = reverseList(array)
