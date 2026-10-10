'''
    A MATHEMATICS & COMPUTING ARCHIVE BY YASHASS MATHAPATHI
    Solving system of linear equations using gauss seidel method

    For a system of lienar equations Gauss Seidel method is an iterative numerical technique used to solve system of linear equations.
    
    The method: 
    1. Check for diagonal relationships
    2. Create equations of x(y, z), y(z, x) and z(x, y).
    3. Start with x0 = 0, y0=0, z0=0;
    4. Substitue y0 and z0 in x to get x1.
    5. To find y1 put x=x1 and z=z0 in y.
    6. Similarly find for z1 = z(x1, y1)    
    
    This completes one iteration, peform more iterations to get the number with the most accurate value or 4 decimal place accuracy.
    
    Round off the values of xn, yn, zn (where n=iteration when you get 4 decimal accuracy), they are the solutions to the linear equations.
    
    ONLY FOR 3 UNKOWNS
    
'''


# Entering the coefficient matrix by the user
def enterLinearEquations():
    e1 = []
    e2 = []
    e3 = []
    A = [e1, e2, e3]
    print("Enter a, b, c and d of 1st equation")
    for n in range(4):
        ele = int(input(">>"))
        e1.append(ele)
    print("Enter a, b, c and d of 2nd equation")
    for n in range(4):
        ele = int(input(">>"))
        e2.append(ele)
    print("Enter a, b, c and d of 3rd equation")
    for n in range(4):
        ele = int(input(">>"))
        e3.append(ele)
        
    return A

    # Index variable equivalent
def IndexVariableEquivalent(i):
    return ['x', 'y', 'z'][i]

# checking diagonal relationship and building equation for x(y, z); y(x, z); z(x, y).
def diagonalCheck(A):
    inds = []
    # checking diagonal relationship
    for i in range(len(A)):
        coeffs = A[i][:3]
        abs_coeffs = [abs(x) for x in coeffs]
        larg = max(abs_coeffs)
        largI = abs_coeffs.index(larg)
        oth_sum = sum(abs_coeffs)-larg
        
        if larg >= oth_sum:
            inds.append(IndexVariableEquivalent(largI))
    return inds

# The difference between the two consecutive values must be < 0.0001 OR 4 decimal place accuracy
def toleranceChecker(xi, yi, zi, xf, yf, zf):
    tolerance = 0.0001
    diffx = abs(xf - xi)
    diffy = abs(yf - yi)
    diffz = abs(zf - zi)
    
    if diffx < tolerance and diffy < tolerance and diffz < tolerance:
        return False
    else:
        return True
        
# The main logic of the program
def IterationsAndAnswer(x, y , z, inds, A, iteration):
    xind = inds.index('x')
    yind = inds.index('y')
    zind = inds.index('z')
    ans = [round(x, 1), round(y, 1), round(z, 1)]
    xinitial, yinitial, zinitial = x, y, z
    
    # iterations
    x = (1/A[xind][0])*(A[xind][3] - (y * A[xind][1]) - (z*A[xind][2]))
    y = (1/A[yind][1])*(A[yind][3] - (x * A[yind][0]) - (z*A[yind][2]))
    z = (1/A[zind][2])*(A[zind][3] - (y * A[zind][1]) - (x*A[zind][0]))
    
    if toleranceChecker(xinitial, yinitial, zinitial, x, y, z):
        IterationsAndAnswer(x, y, z, inds, A, iteration=iteration+1)
    else:
        solutions(ans, iteration)

# just a function to show the result
def solutions(ans, noi):
    print("The number of iterations took: ", noi)
    print(f"x = {ans[0]}, y={ans[1]}, z={ans[2]}")
        
      
if __name__ == "__main__":
    A=enterLinearEquations()
    IterationsAndAnswer(0.0, 0.0, 0.0, diagonalCheck(A), A, 0)