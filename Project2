from matrix_wrapper import MatrixWrapper


def main():  # Main method that prompts the user for the size of the matrix.
    matrixRow = int(input("Enter the number of matrix rows: "))
    matrixCol = int(input("Enter the number of matrix columns: "))

    matrix = [[0 for _ in range(matrixCol)] for _ in range(matrixRow)]  # Creates a matrix based on user input.

    # For loop to set the array to 0 in all elements.
    for i in range(matrixRow):
        for j in range(matrixCol):
            matrix[i][j] = 0

    myMatrix = MatrixWrapper(matrixRow, matrixCol)  # Pass the matrix parameters to the MatrixWrapper.
    print(myMatrix)  # Outputs the current array size and values.

    while True:  # The loop menu to interact with the array.
        print("Matrix Menu")
        print("1. Randomize the matrix")
        print("2. Change the rows and columns of the matrix")
        print("3. Change the value of a particular row and column")
        print("4. Display the maximum and minimum value of the matrix")
        print("5. Transpose the matrix")
        print("Please select an option:")

        choice = int(input())

        # The if/elif chain to call the methods to interact with the array (Python has no switch/case).
        if choice == 1:
            myMatrix.randomMatrix()
            print(myMatrix)
        elif choice == 2:
            myMatrix.changeMatrix()
            print(myMatrix)
        elif choice == 3:
            myMatrix.changeElement()
            print(myMatrix)
        elif choice == 4:
            myMatrix.matrixMinMax()
            print(myMatrix)
        elif choice == 5:
            myMatrix.transpose()
            print(myMatrix)
        else:
            print("This is not a valid option. Please select again.")


if __name__ == "__main__":
    main()
