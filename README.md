# COMPETATIVE PROGRAMMING   


This repo will be used for my self-development towards learning how to compete in global coding challenges. 

| Nav | 
|-----|
|[LEARNING OBJECTIVES ](#LEARNING-OBJECTIVES) |
|[[Speed Boosts](#Speed-Boosts) |
|[RESOURCES](#RESOURCES) |  
|[Useful Code Snippets](#Useful-Code-Snippets) |
|[Sample Questions](#Sample-Questions) |





## LEARNING OBJECTIVES
    

**CS METHDOLOGIES**  

- `BINARY TREE SEARCH`  
- `GRAPH TRAVERSALS` 
- `DYNAMIC PROGRAMMING` 
- DATASTRUCTURES SUCH AS `STACKS` `QUEUES` & `BINARY TREES`  
- `List comprehension`  
- `lambda function`  
- Advanced Python
  
**CS MATH**  
  
- `BIG O`
- `Graph theory` 
- Measure compute time  
- `linear time`, `polynomial time` etc..  

## Speed Boosts
  
To be good at competative programming you need to move fast.   


### Mac ShortCuts 

**JUMP TO ADDRESS BAR**   `⌘ + L`  
**Full Screen** `⌘ + CTL + F`  
**quit app** `⌘ q`


### Windows Shortcuts

**JUMP TO ADDRESS BAR**   `ctl + L`  
    
# Useful Code Snippets  



## BE CARFUL OF ARRAY : 
```python

array = [1,2,3,4,5,6,7,8,9]
middle = array // 2



array[0:middle]
## DOES NOT INCLUDE MIDDLE
[1,2,3,4]


array[middle:]
## DOES INCLUDE MIDDLE
[5,6,7,8,9]
```


## RESOURCES  
  
#### Hands On  

- [hackerank](https://www.hackerrank.com/)
- [lambda excercises](https://www.w3resource.com/python-exercises/lambda/index.php)
  
### Theory and Tips  
  

- [Google Introvid](https://www.youtube.com/watch?v=cMHY4UouGCk&list=PLllx_3tLoo4csmLveWHpjcRTXVMCcvvmc&index=8&ab_channel=LifeatGoogle)  
- [Google Playlist](https://www.youtube.com/playlist?list=PLllx_3tLoo4csmLveWHpjcRTXVMCcvvmc)
- [Coding Tips](https://www.youtube.com/watch?v=WZkTPJE0aRE&list=PLllx_3tLoo4csmLveWHpjcRTXVMCcvvmc&index=5&ab_channel=GoogleStudents)
- [Google FAQ](https://codingcompetitions.withgoogle.com/kickstart/faq)





# Sample Questions
 
[Challenges](https://www.hackerrank.com/interview/interview-preparation-kit)  
  
## Mean, Median ,Mode 

```python
numberArray = list(map(int, inputnum.split()))


def getMean(numberArray):
    meanOut = sum(numberArray)/len(numberArray)
    print(meanOut)


def getMedian(numberArray):
    numberArray.sort()
    index = len(numberArray) // 2
    if(len(numberArray) % 2): 
        print(numberArray[index])
    else:
        result = (numberArray[index - 1] + numberArray[index])/2
        print(result)
        
def getMode(numberArray):
    nums = numberArray
    nums.sort()
    counts = dict()
    for i in nums:
        # Get i then adds 1, alternatively updates 0 if not found (then adds 1)
        counts[i] = counts.get(i, 0) + 1
    mode = max(counts, key=counts.get)
    print(mode)
    
getMean(numberArray)
getMedian(numberArray)
getMode(numberArray)

```
  
## Weighted Mean  

```python
#inputs

size        = "5"
inputArray  = "10 40 30 50 20 "
weightArray = "1 2 3 4 5 "

# format inputs

size = int(size)
inputArray = list(map(int, inputArray.split()))
weightArray = list(map(int, weightArray.split()))

# weighted mean
def getWeightedMean(inputArray,weightArray):
    combinedArray = []
    for x in range(0, len(inputArray)):
        weightedValue = inputArray[x] * weightArray[x]
        combinedArray.append(weightedValue)
    
    weightedMeanValue =  sum(combinedArray)/sum(weightArray)
    
    print(weightedMeanValue)
    
getWeightedMean(inputArray,weightArray)
```



## Quartiles and median

```python
array = [3, 5, 7, 8, 12, 13, 14, 18, 21]
import random 


def getMid(chosenRange):
    if(len(chosenRange) % 2):
        return(chosenRange[len(chosenRange)//2])
    else:
        return((chosenRange[len(chosenRange)//2 - 1]  + chosenRange[len(chosenRange)//2 ] ) // 2)


M = getMid(array)


Q1r = array[0:len(array) // 2]

if(len(array)%2):
    # odd (skip median as already used)
    q3r = array[len(array) // 2 + 1:]
    # even
else:
    q3r = array[len(array) // 2:]



print(getMid(Q1r))
print(M)
print(getMid(q3r))
```

