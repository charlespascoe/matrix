import copy


class MatrixArithmeticError(Exception):
    pass

class Matrix:
    def __init__(self, matrix):
        self._rows = len(matrix)
        self._columns = len(matrix[0]) if len(matrix) > 0 else 0
        self._m = matrix

    @classmethod
    def empty_matrix(cls, rows, columns):
        return cls([[0 for j in range(columns)] for i in range(rows)])

    @classmethod
    def identity_matrix(cls, size):
        return cls([[int(i == j) for j in range(size)] for i in range(size)])

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    def __getitem__(self, index):
        if index < 0 or index >= len(self._m):
            raise Exception()

        return self._m[index]

    def get_matrix(self):
        return copy.deepcopy(self._m)

    def __str__(self):
        return '{}x{}'.format(self.rows, self.columns)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            # Scalar multiplication
            m = self.get_matrix()
            for i in range(self.rows):
                for j in range(self.columns):
                    m[i][j] *= other
            return Matrix(m)
        elif isinstance(other, Matrix):
            # Matrix multiplication
            if self.columns != other.rows:
                raise MatrixArithmeticError('Cannot multiply - invalid matrix sizes')

            m = [[0 for j in range(other.columns)] for i in range(self.rows)]

            for i in range(self.rows):
                for j in range(other.columns):
                    val = 0
                    for x in range(self.columns):
                        val += self[i][x] * other[x][j]
                    m[i][j] = val

            return Matrix(m)
        else:
            raise TypeError('Invalid multiplication type: {}'.format(type(other)))

    def __div__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self * (1 / float(other))
        else:
            raise TypeError('Invalid division type: {}'.format(type(other)))

    def __pow__(self, exp):
        if self.rows != self.columns:
            raise MatrixArithmeticError('Only square matricies can be raised to a power')

        if not isinstance(exp, int):
            raise TypeError('Exponent must be an int')

        result = Matrix.identity_matrix(self.rows)

        m = Matrix(self.get_matrix())

        if exp < 0:
            m = m.inverse()

            if m is None:
                raise MatrixArithmeticError('Matrix is non-invertible')

            exp = -exp

        while exp > 0:
            if exp & 1:
                result *= m

            m *= m

            exp >>= 1

        return result

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Matrix addition requires another matrix')

        if self.rows != other.rows or self.columns != other.columns:
            raise MatrixArithmeticError('Cannot add - invalid matrix sizes')

        m = [[0 for j in range(self.columns)] for i in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.columns):
                m[i][j] = self[i][j] + other[i][j]

        return Matrix(m)

    def __mod__(self, other):
        if not isinstance(other, int) or isinstance(other, float):
            raise TypeError('Invalid modulus type: {}'.format(type(other)))

        m = self.get_matrix()
        for i in range(self.rows):
            for j in range(self.columns):
                m[i][j] %= other

        return Matrix(m)

    def submatrix(self, not_i, not_j):
        return Matrix([[self._m[i][j] for j in range(self.columns) if j != not_j] for i in range(self.rows) if i != not_i])

    def determinant(self):
        if self.rows != self.columns or self.rows == 0:
            raise MatrixArithmeticError('Determinant can only be calculated for square matrices')

        if self.rows == 1:
            return self[0][0]

        if self.rows == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]

        coefficient = 1

        det = 0

        for j in range(self.columns):
            det += coefficient * self[0][j] * self.submatrix(0, j).determinant()
            coefficient *= -1

        return det

    def cofactor_matrix(self):
        if self.rows != self.columns or self.rows == 0:
            raise MatrixArithmeticError('Cofactor matrix can only be calculated for square matrices')

        if self.rows == 1:
            return Matrix([[self[0][0]]])

        c = Matrix.empty_matrix(self.rows, self.columns)

        for i in range(self.rows):
            for j in range(self.columns):
                c[i][j] = pow(-1, i+j) * self.submatrix(i, j).determinant()

        return c

    def transpose(self):
        return Matrix([[self[i][j] for i in range(self.rows)] for j in range(self.columns)])

    def inverse(self):
        det = self.determinant()

        if det == 0:
            return None

        return self.cofactor_matrix().transpose() / det


