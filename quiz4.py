#  Kip Fletcher  MATH 4330  6-26-2018
#  Quiz 4

#function that returns the product of a matrix and a vector.
def matVec(matrix, vector):
    '''
    This function takes a matrix and a vector as its arguments and uses
    if-else statements with for-loops to validate the input matrix and vector.
    It then creates a new matrix by multiplying the input matrix by the input
    vector and returns the new matrix. 
    '''
    new_matrix = []         # holds the matrix vector product.
    if len(matrix[0]) == len(vector):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if type(matrix[i][j]) != int and type(matrix[i][j]) != float and type(matrix[i][j]) != complex:
                   return("Invalid matrix element in matVec function.")
        for i in vector:
             if type(i) != int and type(i) != float and type(i) != complex:
                   return("Invalid vector element in matVec function.")
    
        for i in range(len(matrix)):
            row_product = 0     # holds the product of each matrix row.
            for j in range(len(vector)):
                row_product += (matrix[i][j]*vector[j])
            new_matrix.append(row_product) # adds each row product entry to new matrix.
        return new_matrix
    else:
        return("Incompatible matrix-vector in matVec function.")
        
#function that returns the difference of two vectors.
def vec_sub(vector01,vector02):
    '''
    This function take two vectors, verifies that they are valid with
    an if-else statement and for-loops, and subtracts them using a for loop.
    It returns the difference of the two vectors as a new vector.
    '''

    if len(vector01) == len(vector02): # validates compatibility of vectors
        for i in vector01:
            if type(i) != int and type(i) != float and type(i) != complex:
               return("Invalid vector element in vec_sub function.")  
        for i in vector02:
            if type(i) != int and type(i) != float and type(i) != complex:
               return("Invalid vector element in vec_sub function.") 
        new_vec = [] # to store the difference of the two vectors as a new vector. 
        j = len(vector01)
        for i in range(j):
         new_vec.append(vector01[i]-vector02[i])#computes and stores elements of the new vector.
        return new_vec
    else:
      return("Invalid vector lengths for vec_sub function")  

#function that returns the product of a vector and a scalar.
def scavec(vector,scalar):
    '''
    This function take a vector and a scalar as its arguments and validates them
    using if statements and for-loops. It then multiplies the vector and scalar
    together with a for loop, and returns the product as a new vector.
    '''
    if type(vector) != list or (type(scalar) != int and type(scalar) != float and type(scalar) != complex):
        return("Invalid vector/scalar in function scavec function")
    for i in vector:
        if type(i) != int and type(i) != float and type(i) != complex:
               return("Invalid vector element in scavec function.")
    new_vec = []
    for i in vector:
        new_vec.append(i * scalar)#computes and stores elements of the new vector. 
    return new_vec 

#function that returns the dot product of two vectors.
def dot(vector01, vector02):
    '''
    This function takes two compatible vectors as its arguments, uses if-else
    and for statements to validate them, and returns their dot product. It first
    uses an if-else statement to verify that both vectors are vectors. It utilizes
    an if-else statement to determine if the two vectors are compatible and a
    for loop computes the dot product of the two vectors. If the two vectors are
    not compatible it returns "Invalid vector lengths in dot function."
    '''
    dot_prod = 0

    if len(vector01) == len(vector02):
        for i in vector01:
            if type(i) != int and type(i) != float and type(i) != complex:
               return("Invalid vector element in dot function.")  
        for i in vector02:
            if type(i) != int and type(i) != float and type(i) != complex:
               return("Invalid vector element in dot function.") 
        for i in range(len(vector01)): 
            dot_prod += vector01[i]*vector02[i] #computes and stores elements of the new vector.
        return dot_prod
    else:
        return("Invalid vector lengths in dot function")

#function that returns the 2-norm of a vector.
def norm_2(vector):
    '''
    This function takes a vector, validates it using if statements and for-loops,
    and computes its 2-norm using a for loop. It computes the sum of the squares
    of the absolute values of the vector elements. Then it takes the square root
    of that sum and returns its value as the 2-norm.
    '''
    if type(vector) != list:
        return("Invalid vector in norm_2 function")
    for i in vector:
        if type(i) != int and type(i) != float and type(i) != complex:
               return("Invalid vector element in norm_2 function.")
    sum1 = 0 #sum of the squares of the absolute values of the vector elements.
    norm = 0 
    for i in range(len(vector)):
        sum1 += (vector[i]) ** 2 #computes and stores sum of squares of abs. vals of vector elements.
    norm = sum1 ** (1/2)#computes and stores sq. root of total sum as value of norm.
    return norm

#function that returns the transpose of a matrix.
def matrix_transposer(matrix):
    '''
    This function takes a single matrix and first validates it using if statements
    and for-loops. Then it computes the matrix transpose. It uses nested for loops to
    move each entry of the matrix to its corresponding position in the transposed matrix.
    It then returns the transpose of the original matrix.
    '''
    if type(matrix) != list:
        return("Invalid matrix in matrix_transposer function.")
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if type(matrix[i][j]) != int and type(matrix[i][j]) != float and type(matrix[i][j]) != complex:
                   return("Invalid matrix element in matrix_transposer function.")
    matrix_trans = []

    for i in range(len(matrix[0])): #iterates through columns of input matrix.
        new_row = [] #holds elements of one transposed row at a time.
        for j in range(len(matrix)): #iterates through rows of input matrix.
            new_row.append(matrix[j][i])
        matrix_trans.append(new_row)# stores each transposed row into new matrix.

    return matrix_trans

#function that prints the Reduced QR factorization of a matrix.
def gramSchmitt_mod(matrix):
    '''
    This function takes a matrix and validates it using if statements and for-loops.
    If the matrix is valid, it decomposes the matrix into a reduced orthogonal
    matrix q and a reduced upper triangular matrix r using the modified Gram
    Schmitt process. It first transposes the matrix to put the column vectors
    into rows and then creates three zero matrices of appropriate size to hold
    a copy of the input matrix, the q matrix, and the r matrix.  It uses a
    for-loop to copy the input matrix into matrix v, and then nested for-loops
    to produce matrices q and r.  To do this it implements 4 other functions:
    the norm_2, scavec,dot and vec_sub functions. It also contains an if-else
    statement to validate that none of the main diagonal entries of the r matrix
    are zero.
    '''
    if type(matrix) != list:
        return("Invalid matrix in gramSchmitt_mod function.")
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if type(matrix[i][j]) != int and type(matrix[i][j]) != float and type(matrix[i][j]) != complex:
                   return("Invalid matrix element in gramSchmitt_mod function.")
    rows = len(matrix)
    cols = len(matrix[0])
    a = []
    a = matrix_transposer(matrix) #transposes column vectors to row vectors.

    v = [[0]*rows] #creates new zero matrix to hold v values.
    for i in range(cols-1):
        v.append([0]*cols)

    r = [[0]*cols] #creates new zero matrix to hold R values. 
    for i in range(cols-1):
        r.append([0]*cols)

    q = [[0]*rows] #creates new zero matrix to hold Q values. 
    for i in range(cols-1):
        q.append([0]*cols)

    for i in range(0,cols,1): #copies input matrix into new matrix v.
        v[i] = a[i]
         
    for i in range(0,cols,1):
        r[i][i] = norm_2(v[i]) #computes main diagonal entries of R matrix.
        if r[i][i] != 0:    #validates that main diagonal entries of R matrix != 0.
          q[i] = scavec(v[i],(1/r[i][i])) #computes each column of Q matrix.
        else:
          return("Error: R values on main diagonal cannot be 0")
        for j in range(i+1,cols,1):
            r[i][j] = dot(q[i],v[j]) #computes the upper triangle entries of R matrix.
            v[j] = vec_sub(v[j],scavec(q[i],r[i][j]))
    
    qt = matrix_transposer(q) #switches row vectors of Q matrix back to column vectors. 
    
    print("Q = ")
    for i in range(len(q[0])):
      print(qt[i])
    print("R = ")
    for j in range(len(r)):
       print(r[j])
    return None

#These are test variables for the matVec function.
m1 = [[4,6],
      [3,0],
      [2,4]]
v1 =  [5,1]

m2 = [[4,6,1],
      [3,0,2],
      [2,4,8]]
v2 =  [5,1]
#These are test cases for the matVec function.
#print(matVec(m1,v1))
#print(matVec(m2,v2))

#These are test variables for the vec_sub function.
v1a = [3,6,2]
v1b = [-1,4,0]

v2a = [3,6,2]
v2b = [1,4,"cool"]
#These are test cases for the vec_sub function.
#print(vec_sub(v1a,v1b))
#print(vec_sub(v2a,v2b))

#These are test variables for the scavec function.
v1 = [1,-2,3]
s1 = 4

v2 = [1,2]
s2 = "oops"
#These are test cases for the scavec function.
#print(scavec(v1,s1))
#print(scavec(v2,s2))

#These are test variables for the dot function.
v1a = [2,4,6]
v1b = [3,-1,1]

v2a = [2,4,6]
v2b = [0,3,"nope"]
#These are test cases for the dot function.
#print(dot(v1a,v1b))
#print(dot(v2a,v2b))
       
#These are test variables for the norm_2 function.
v1 = [2,7,-9,3]
v2 = [5,2,8,"bad"]
#These are test cases for the norm_2 function.
#print(norm_2(v1))
#print(norm_2(v2))
    
#These are test variables for the matrix_transposer function.
m1 = [[3,7,3],
      [2,1,-6],
      [4,0,9]]
m2 = [[6,"%"],
      [1,-1]]
#These are test cases for the matrix_transposer function.
#print(matrix_transposer(m1))
#print(matrix_transposer(m2))


#These are the test variables for the gramSchmitt_mod function.
m1 = [[2,1,-2],
      [3,1,1],
      [4,2,5]]

m2 = [[1,2],
      [0,1],
      [1,0]]

m3 = [[4,5,2],
      [1,"BAM",3],
      [0,9,2]]
#These are the test cases for the gramSchmitt_mod function.
print(gramSchmitt_mod(m1))
#print(gramSchmitt_mod(m2))
#print(gramSchmitt_mod(m3))
