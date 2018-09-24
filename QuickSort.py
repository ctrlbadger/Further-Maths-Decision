import random
import math

unsortedList = list(range(25000000))
random.shuffle(unsortedList)

def quickSort(unsortedList):
    middle = (int(math.ceil(len(unsortedList) + 1) / 2)) - 1
    reference = unsortedList.pop(middle)
    list1, list2 = [], []
    list(map(lambda x: list1.append(x) if x < reference else list2.append(x), unsortedList))
    checkListLength = lambda newList: quickSort(newList) if len(newList) > 1 else newList
    return checkListLength(list1) + [reference] + checkListLength(list2)
quickSort(unsortedList)
