# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature. If there is no future day for which this is possible, put 0 instead.
#
# Input
# The length of temperatures will be in the range [1, 30000]. Each
# temperature will be an integer in the range [30, 100].

def dailyTemperatures(dailyTemps):
    for index, temperature in enumerate(dailyTemps):
        print("index", index)
        print("temperature", temperature)
    #iterate through elements
    # for each elements iterate through remaining elements until greater number is found
    stack = []
    for i in range(len(dailyTemps)):
        daysUntil = 0
        for j in range(i, len(dailyTemps)):
            if dailyTemps[i] >= dailyTemps[j]:
                daysUntil += 1
            else :
                break
        if daysUntil + i == len(dailyTemps):
            stack.append(0)
        else :
            stack. append(daysUntil)
    return stack

#
# Sample
# Input#1
T = [73, 74, 75, 71, 69, 72, 76, 73]
dailyTemperatures(T)
# Output#1
# [1, 1, 4, 2, 1, 1, 0, 0]
sampleInput = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(sampleInput))

# Liz Howards Solution
def dailyTemperatures(dailyTemps):
    answerArray = [0] * len(dailyTemps)
    stack = []
    for index, temperature in enumerate(dailyTemps):
        while stack and dailyTemps[stack[-1]] < temperature:
            indexOfPreviousLowerTemp = stack.pop()
            answerArray[indexOfPreviousLowerTemp] = index - indexOfPreviousLowerTemp
        stack.append(index)
    return answerArray
