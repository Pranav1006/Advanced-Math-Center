#This is the start of the Advanced Math Center Project (ADMC)
#I will be starting with statistical formulas and clear, formatted explanations. We will see where it goes from there

#import the math libraries
import math
import statistics as stat

#I will start with basic functions that can be applied to any data.

#testing list(s)
values1 = [1,2,3,4,5]
values2 = [3,4,7,8,12]

#Many functions are defined in the statistics library, but I will be writing out the explanations for the advanced functions,
#such as variance, z-score, and correlation. I can't calculate area with z-score yet, which I will try to find out.

#standard deviation of a population divides by the number of people
#sd of a sample divides by the number of people minus 1

def stand_dev(list, popSamp):
    if popSamp != 0 and popSamp != 1:
        return "Please enter 0 for population or 1 for sample in the second argument"
    sumOfDiff = 0.0
    mean = stat.mean(list)

    for i in list:
        sumOfDiff = sumOfDiff + ((i-mean)**2)
    sumOfDiff /= (len(list)-popSamp)

    sumOfDiff = math.sqrt(sumOfDiff)
    return sumOfDiff

def zScore(value, mean, s):
    return (value - mean)/s


def correlation(xlist, ylist):
    
    if len(xlist) != len(ylist):
        return "Lists must be the same amount"
    total = 0
    sX = stand_dev(xlist, 1)
    sY = stand_dev(ylist, 1)
    xMean = stat.mean(xlist)
    yMean = stat.mean(ylist)
    for i in range(len(xlist)):
        multiple = (xlist[i] - xMean)/sX*(ylist[i] - yMean)/sY
        total += multiple
    
    return total/(len(xlist) - 1)


r = correlation(values1, values2)

print(f"\nThe Standard Deviation of the Data is {stand_dev(values1, 1)} \n")
print(f"The correlation of the lists are {r} \n")