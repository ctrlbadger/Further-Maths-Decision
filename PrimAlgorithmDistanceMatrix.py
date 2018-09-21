import numpy as np

dMatrix = np.array([[None, 27, 12, 23, 74],
           [27, None, 47, 15, 71],
           [12, 47, None, 28, 84],
           [23, 15, 28, None, 15],
           [24, 71, 87, 15, None]])


# Choose any Vertex
Columnns = np.array([0])

#Delete the Row from Vertex
dMatrix = np.delete(dMatrix, Columns[-1], 0)

# Get the smallest from each
smallestInColumn = dMatrix.argmin(axis=1)[Columns]

smallestOverallIndex = dMatrix[smallestInColumn, Columns]


print(dMatrix)
print(dMatrix[0,:])



