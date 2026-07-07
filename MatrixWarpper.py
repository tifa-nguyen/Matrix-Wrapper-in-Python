Matrix wrapper · PY
import random
 
 
class MatrixWrapper:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.tempMatrix = [[0 for _ in range(col)] for _ in range(row)]
 
    def __str__(self):  # Convert the int array values into string.
        stringArr = "Matrix:\n"
        for i in range(self.row):
            for j in range(self.col):
                stringArr += str(self.tempMatrix[i][j]) + " "
            stringArr += "\n"
        return stringArr
 
    def randomMatrix(self):  # Loop option 1 - Randomize the matrix by setting every element from 0 to 99.
        for i in range(self.row):
            for j in range(self.col):
                randomValue = random.randint(0, 99)
                self.tempMatrix[i][j] = randomValue
 
    def changeMatrix(self):  # Loop option 2 - Change the rows and columns of the matrix (and reinitialize all values to 0)
        self.row = int(input("Enter the number of matrix rows you wish to change to: "))
        self.col = int(input("Enter the number of matrix columns you wish to change to: "))
 
        tempArr = [[0 for _ in range(self.col)] for _ in range(self.row)]
 
        self.tempMatrix = tempArr
 
        for i in range(self.row):
            for j in range(self.col):
                self.tempMatrix[i][j] = 0
 
    def changeElement(self):  # Loop option 3 - Allow the user to change a particular row and column of the matrix.
        selectRow = int(input("What is the row of the number you want to change? "))
        selectCol = int(input("What is the column of the number you want to change? "))
        newValue = int(input("Please enter the number you wish to set: "))
        self.tempMatrix[selectRow - 1][selectCol - 1] = newValue
 
    def matrixMinMax(self):  # Loop option 4 - Display the maximum and minimum value of the matrix.
        max_val = 0
        min_val = 1000
        for i in range(self.row):
            for j in range(self.col):
                if self.tempMatrix[i][j] > max_val:
                    max_val = self.tempMatrix[i][j]
                if self.tempMatrix[i][j] < min_val:
                    min_val = self.tempMatrix[i][j]
        print(f"The maximum value of the matrix is [ {max_val} ] and the minimum value of the matrix is [ {min_val} ].")
 
    def transpose(self):  # Loop option 5 - Flip the matrix over its diagonal (the transpose of a matrix).
        transposeArr = [[0 for _ in range(self.row)] for _ in range(self.col)]
        for i in range(self.row):
            for j in range(self.col):
                transposeArr[j][i] = self.tempMatrix[i][j]
 
        tempValue = self.row
        self.row = self.col
        self.col = tempValue
 
        self.tempMatrix = [[0 for _ in range(self.col)] for _ in range(self.row)]
 
        for i in range(self.row):
            for j in range(self.col):
                self.tempMatrix[i][j] = transposeArr[i][j]
