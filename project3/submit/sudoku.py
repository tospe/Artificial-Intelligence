from z3 import *
# Create matrix and variables X_1_2 ...
X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(9) ]
      for i in range(9) ]

#first restrain only values between 1 and 9
cells_c  = [ And(1 <= X[i][j], X[i][j] <= 9)
             for i in range(9) for j in range(9) ]

# each row only one of the digits
rows_c   = [ Distinct(X[i]) for i in range(9) ]

# each column only one of the digits
cols_c   = [ Distinct([ X[i][j] for i in range(9) ])
             for j in range(9) ]

# each 3x3 square only one of the digits
sq_c     = [ Distinct([ X[3*i0 + i][3*j0 + j]
                        for i in range(3) for j in range(3) ])
             for i0 in range(3) for j0 in range(3) ]

sudoku_c = cells_c + rows_c + cols_c + sq_c

# sudoku instance, we use '0' for empty cells
instance = ((9,8,0,6,0,0,0,3,1),
            (0,0,7,0,0,0,0,0,0),
            (6,0,0,5,4,0,0,0,0),
            (0,0,0,0,0,8,3,7,4),
            (0,0,0,0,6,0,1,0,0),
            (0,0,0,0,0,0,9,0,2),
            (0,3,2,0,0,7,4,0,0),
            (0,4,0,3,0,0,0,1,0),
            (0,0,0,0,0,0,0,0,0))

instance_c = [ If(instance[i][j] == 0,
                  True,
                  X[i][j] == instance[i][j])
               for i in range(9) for j in range(9) ]

s = Solver()
s.add(sudoku_c + instance_c)
if s.check() == sat:
    m = s.model()
    print(s.model())
    r = [ [ m.evaluate(X[i][j]) for j in range(9) ]
          for i in range(9) ]
    print_matrix(r)
else:
    print("failed to solve")
