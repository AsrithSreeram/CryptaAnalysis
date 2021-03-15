import numpy as np

def levenshtein_distance(string1, string2):
    x_dimension = len(string1) + 1
    y_dimension = len(string2) + 1
    npMatrix = np.zeros ((x_dimension, y_dimension))
    for x in range(x_dimension):
        npMatrix [x, 0] = x
    for y in range(y_dimension):
        npMatrix [0, y] = y

    for x in range(1, x_dimension):
        for y in range(1, y_dimension):
            if string1[x-1] == string2[y-1]:
                npMatrix [x,y] = min(
                    npMatrix[x-1, y] + 1,
                    npMatrix[x-1, y-1],
                    npMatrix[x, y-1] + 1
                )
            else:
                npMatrix [x,y] = min(
                    npMatrix[x-1,y] + 1,
                    npMatrix[x-1,y-1] + 1,
                    npMatrix[x,y-1] + 1
                )
    return (npMatrix[x_dimension - 1, y_dimension - 1])

string1 = "tht"
string2 = "that"
string3 = "The"
string4 = "these"

print(levenshtein_distance(string1, string2))
print(levenshtein_distance(string1, string3))
print(levenshtein_distance(string1, string4))
