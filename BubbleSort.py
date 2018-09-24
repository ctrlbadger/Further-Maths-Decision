import random

unsortedList = list(range(25000000))
random.shuffle(unsortedList)

swapped = True
while swapped:
    swapped = False
    for index in range(0, len(unsortedList) - 1):
        if unsortedList[index] > unsortedList[index + 1]:
            unsortedList[index], unsortedList[index + 1] = unsortedList[index + 1], unsortedList[index]
            swapped = True
