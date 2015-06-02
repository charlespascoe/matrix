import copy

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

    def __str__(self):
        return '{}x{}'.format(self.rows, self.columns)

    def __mul__(self, other):
        if isinstance(other, int):
            # Scalar multiplication
            m = copy.deepcopy(self._m)
            for i in range(self.rows):
                for j in range(self.columns):
                    m[i][j] *= other
            return Matrix(m)
        elif isinstance(other, Matrix):
            # Matrix multiplication
            if self.rows != other.columns:
                raise Exception('Cannot multiply - invalid matrix sizes')



            pass
        else:
            raise Exception()

    def __add__(self, other):
        if isinstance(other, Matrix) and Math

    def __mod__(self, other):
        for i in range(self.rows):
            for j in range(self.columns):
                self._m[i][j] %= other



m = Matrix.empty_matrix(0, 0)

m * 10

m * Matrix(1, 1)
