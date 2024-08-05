import numpy as np

def DominantValue(matrix):
    eigenvalues, _ = np.linalg.eig(matrix)
    dominant_eigenvalue = max(eigenvalues, key=abs)
    return dominant_eigenvalue


def inverseMatrix(matrix):
    return np.linalg.inv(matrix)


# def IdentityMatrix(matrix):
#     # return np.dot(matrix, inverseMatrix(matrix)) note : something wrong with this function :(

def IdentityMatrix(matrix):
    n = matrix.shape[0]
    identity = np.eye(n)
    return identity


matrix = np.array([[1, 2], [3, 4]])
print("Dominant value: {:.2f}".format(DominantValue(matrix)))
print("Inverse matrix: \n", inverseMatrix(matrix))
print("Identity matrix: \n", IdentityMatrix(matrix))
