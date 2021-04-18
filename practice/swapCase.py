"""
https://www.hackerrank.com/challenges/swap-case/problem


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""


def swap_case(s):
    swappedWord = ""
    for letter in s:
        if(letter.isupper()):
            swappedWord += str(letter.lower())
        else:
            swappedWord += str(letter.upper())

    return(swappedWord)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)