import numpy as np

dMatrix = np.array([[100, 27, 12, 23, 74],
                    [27, 100, 47, 15, 71],
                    [12, 47, 100, 28, 84],
                    [23, 15, 28, 100, 75],
                    [74, 71, 84, 75, 100]])




chosenColumn = [0]

spanningTree = []
while len(spanningTree) < dMatrix.shape[0] - 1:
    arrays = np.argsort(dMatrix[:, chosenColumn], axis=None)
    newArray = []


    list(map(lambda x: newArray.append(x) if all([np.floor(x / len(chosenColumn)) != columnIndex for columnIndex in chosenColumn]) else None, arrays))
    flatIndex = newArray[0]
    column = chosenColumn[flatIndex % len(chosenColumn)]
    row = int(np.floor(flatIndex / len(chosenColumn)))
    spanningTree.append([row, column])

    chosenColumn.append(row)

    print("chosenColumn", chosenColumn)

    print("column", column)
    print("row", row)
    print()

print(spanningTree)
