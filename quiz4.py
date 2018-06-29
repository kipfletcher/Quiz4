#  Kip Fletcher  MATH 4330  6-26-2018
#  Quiz 4

#function that returns the product of a matrix and a vector.
def matVec(matrix, vector):
    '''
    This function takes a matrix and a vector as its arguments. It then
    creates a new matrix by multiplying the input matrix by the input vector
    and returns the new matrix. 
    '''
    new_matrix = []         # holds the matrix vector product.
    for i in range(len(matrix)):
        row_product = 0     # holds the product of each matrix row.
        for j in range(len(vector)):
            row_product += (matrix[i][j]*vector[j])
        new_matrix.append(row_product) # adds each row product entry to new matrix.
    return new_matrix

#function that returns the difference of two vectors.
def vec_sub(vector1,vector2):
    '''
    This function take two vectors, verifies that they are the same length with
    an if-else statement, and subtracts them using a for loop. It returns the
    difference of the two vectors as a new vector.
    '''

    if len(vector1) == len(vector2):
      b = []
      j = len(vector1)
      for i in range(j):
         b.append(vector1[i]-vector2[i])
      return b
    else:
      return "Invalid vector lengths for vec_sub function"  

#function that returns the product of a vector and a scalar.
def scavec(vector,scalar):
    '''
    This function take a vector and a scalar as its arguments, multiplies them
    together with a for loop, and returns the product as a new vector.
    '''
    b = []
    for i in vector:
         b.append(i * scalar)

    return b

#function that returns the dot product of two vectors.
def dot(vector01, vector02):
    '''
    This function takes two compatible vectors as its arguments and returns
    their dot product. It first uses an if-else statement to verify that both
    vectors are vectors. It utilizes an if-else statement to determine if the two
    vectors are compatible and a for loop computes the dot product of the two
    vectors. If the two vectors are not compatible it returns "Invalid
    Input."
    '''
    dot_prod = 0

    if type(vector01) != list or type(vector02) != list:
        print("Invalid Input")

    if len(vector01) == len(vector02):
        for i in range(len(vector01)): 
            dot_prod += vector01[i]*vector02[i]
        return dot_prod
    else:
        print("Invalid Input") 
        return None

#function that returns the 2-norm of a vector.
def norm_2(vector):
    '''
    This function takes a vector and computes its 2-norm using a for loop. It
    computes the sum of the squares of the absolute values of the vector elements.
    Then it takes the square root of that sum and returns its value as the 2-norm.
    '''
    sum1 = 0
    norm = 0
    for i in range(len(vector)):
        sum1 += (vector[i]) ** 2
    norm = sum1 ** (1/2)
    return norm

#function that returns the transpose of a matrix.
def matrix_transposer(matrix01):
    '''
    This function takes a single matrix and computes its transpose. It uses nested
    for loops to move each entry of the matrix to its corresponding position in
    the transposed matrix. It then returns the transpose of the original matrix.
    '''

    matrix01_trans = []

    for i in range(len(matrix01[0])):
        new_row = []
        for j in range(len(matrix01)):
            new_row.append(matrix01[j][i])
        matrix01_trans.append(new_row)

    return matrix01_trans

#function that returns the Reduced QR factorization of a matrix.
def gramSchmitt_mod(matrix):
    '''
    This function takes a matrix and decomposes it into a reduced orthogonal
    matrix q and a reduced upper triangular matrix r.  It first transposes
    the matrix to put the column vectors into rows and then creates three
    zero matrices of appropriate size to hold a copy of the input matrix,
    the q matrix, and the r matrix.  It uses a for-loop to copy the input
    matrix into matrix v, and then nested for-loops to produce matrices q
    and r.  To do this it implements 4 other functions: the norm_2, scavec,
    dot and vec_sub functions. It also contains an if-else statement to
    validate that none of the main diagonal entries of the r matrix are zero.
    '''
    
    rows = len(matrix)
    cols = len(matrix[0])
    a = []
    a = matrix_transposer(matrix)

    v = [[0]*rows]
    for i in range(cols-1):
        v.append([0]*cols)

    r = [[0]*cols]
    for i in range(cols-1):
        r.append([0]*cols)

    q = [[0]*rows]
    for i in range(cols-1):
        q.append([0]*cols)

    for i in range(0,cols,1):
        v[i] = a[i]
         
    for i in range(0,cols,1):
        r[i][i] = norm_2(v[i])
        if r[i][i] != 0:
          q[i] = scavec(v[i],(1/r[i][i]))
        else:
          print("Error: R values on main diagonal cannot be 0")
        for j in range(i+1,cols,1):
            r[i][j] = dot(q[i],v[j])
            v[j] = vec_sub(v[j],scavec(q[i],r[i][j]))
    
    qt = matrix_transposer(q)
    
    print("Q = ")
    for i in range(len(q[0])):
      print(qt[i])
    print("R = ")
    for j in range(len(r)):
       print(r[j])
    
    list1 = [qt,r]
    return list1

#These are the test variables for the QR matrix factorization.
m1 = [[2,1,-2],
      [3,1,1],
      [4,2,5]]

m2 = [[1,2],
      [0,1],
      [1,0]]

gramSchmitt_mod(m1)

#these for loops print gramSchmitt_mod(m1) in readable matrix form
'''
for i in range(len(m1)):
    print(gramSchmitt_mod(m1)[0][i])
print()
for j in range(len(m1[0])):
    print(gramSchmitt_mod(m1)[1][j])

#these for loops print gramSchmitt_mod(m2) in readable matrix form


for i in range(len(m2)):
    print(gramSchmitt_mod(m2)[0][i])
print()
for j in range(len(m2[0])):
    print(gramSchmitt_mod(m2)[1][j])
'''

