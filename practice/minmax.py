"""

https://www.hackerrank.com/challenges/np-min-and-max/problem


get min using numpy accross axis one 

then get max of that value 

Sample Input

4 2
2 5
3 7
1 3
4 0
Sample Output

3

axis = none , per number 
axis = 0, per array 
axis = 1 per nested array 


"""



import numpy as np
integer_list = map(int, input().split())	
header = list(integer_list)

array = [] 
for x in range(0, header[0]):
	element = list(map(int, input().split()))
	array.append(element)

my_array = np.array(array)
array_min =  np.min(my_array, axis=1)
array_max = np.max(array_min)
print(array_max)