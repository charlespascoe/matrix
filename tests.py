from matrix import Matrix, MatrixArithmeticError
import unittest

class MatrixMultiplication(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1, 2, 3], [4, 5, 6]])

    def test_invalid_type_mutiplication(self):
        with self.assertRaises(TypeError):
            self.m * 'string'

    def test_invalid_maxtrix_size_multiplication(self):
        m2 = Matrix([[7, 8], [9, 10]])

        with self.assertRaises(MatrixArithmeticError):
            self.m * m2

    def test_scalar_multiplication(self):
        result = self.m * 2
        self.assertEqual(result.get_matrix(), [[2, 4, 6], [8, 10, 12]])
        self.assertEqual(self.m.get_matrix(), [[1, 2, 3], [4, 5, 6]])

    def test_matrix_multiplication(self):
        m2 = Matrix([[7, 8], [9, 10], [11, 12]])
        result = self.m * m2
        self.assertEqual(result.get_matrix(), [[58, 64], [139, 154]])
        self.assertEqual(self.m.get_matrix(), [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(m2.get_matrix(), [[7, 8], [9, 10], [11, 12]])


class MatrixAddition(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1, 2, 3], [4, 5, 6]])

    def test_invalid_type_addition(self):
        with self.assertRaises(TypeError):
            self.m + 10

    def test_invalid_matrix_size_addition(self):
        m2 = Matrix([[7, 8], [9, 10], [11, 12]])

        with self.assertRaises(MatrixArithmeticError):
            self.m + m2

    def test_matrix_addition(self):
        m2 = Matrix([[7, 8, 9], [10, 11, 12]])

        result = self.m + m2

        self.assertEqual(result.get_matrix(), [[8, 10, 12], [14, 16, 18]])
        self.assertEqual(self.m.get_matrix(), [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(m2.get_matrix(), [[7, 8, 9], [10, 11, 12]])


class MatrixModulo(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1, 2, 3], [4, 5, 6]])

    def test_invalid_type_modulo(self):
        with self.assertRaises(TypeError):
            self.m % 'string'

    def test_modulo(self):
        result = self.m % 3

        self.assertEqual(result.get_matrix(), [[1, 2, 0], [1, 2, 0]])
        self.assertEqual(self.m.get_matrix(), [[1, 2, 3], [4, 5, 6]])


class MatrixExponentation(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1, 2], [3, 4]])

    def test_invalid_exp_pow(self):
        with self.assertRaises(TypeError):
            self.m**1.5

    def test_pow_2(self):
        result = self.m**2

        self.assertEqual(self.m.get_matrix(), [[1, 2], [3, 4]])
        self.assertEqual(result.get_matrix(), [[7, 10], [15, 22]])

    def test_pow_5(self):
        result = self.m**5

        self.assertEqual(self.m.get_matrix(), [[1, 2], [3, 4]])
        self.assertEqual(result.get_matrix(), [[1069, 1558], [2337, 3406]])

    def test_pow_inv(self):
        result = self.m**-1

        self.assertEqual(self.m.get_matrix(), [[1, 2], [3, 4]])
        self.assertEqual(result.get_matrix(), [[-2, 1], [1.5, -0.5]])


class MatrixClassMethodsAndProperties(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1, 2, 3], [4, 5, 6]])

    def test_rows(self):
        self.assertEqual(self.m.rows, 2)

    def test_columns(self):
        self.assertEqual(self.m.columns, 3)

    def test_empty_matrix(self):
        m = Matrix.empty_matrix(3, 2)

        self.assertEqual(m.get_matrix(), [[0, 0], [0, 0], [0, 0]])

    def test_identity_matrix(self):
        i_m = Matrix.identity_matrix(3)

        self.assertEqual(i_m.get_matrix(), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])


class MatrixSubmatrix(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_submatrix(self):
        result = self.m.submatrix(0, 0)
        result2 = self.m.submatrix(1, 1)

        self.assertEqual(self.m.get_matrix(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(result.get_matrix(), [[5, 6], [8, 9]])
        self.assertEqual(result2.get_matrix(), [[1, 3], [7, 9]])


class MatrixDeterminant(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_non_square_matrix_determinant(self):
        m = Matrix([[1, 2, 3], [4, 5, 6]])

        with self.assertRaises(MatrixArithmeticError):
            m.determinant()

    def test_1x1_determinant(self):
        m = Matrix([[1]])

        det = m.determinant()

        self.assertEqual(m.get_matrix(), [[1]])
        self.assertEqual(det, 1)

    def test_2x2_determinant(self):
        m = Matrix([[1, 2], [3, 4]])
        det = m.determinant()

        self.assertEqual(m.get_matrix(), [[1, 2], [3, 4]])
        self.assertEqual(det, -2)

    def test_3x3_determinant(self):
        det = self.m.determinant()

        self.assertEqual(self.m.get_matrix(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(det, 0)

    def test_another_3x3_determinant(self):
        m = Matrix([[2, 3, 5], [7, 11, 13], [17, 19, 23]])

        det = m.determinant()

        self.assertEqual(m.get_matrix(), [[2, 3, 5], [7, 11, 13], [17, 19, 23]])
        self.assertEqual(det, -78)

    def test_4x4_determinant(self):
        m = Matrix([[2, 3, 5, 7], [11, 13, 17, 19], [23, 29, 31, 37], [41, 43, 47, 53]])

        det = m.determinant()

        self.assertEqual(m.get_matrix(), [[2, 3, 5, 7], [11, 13, 17, 19], [23, 29, 31, 37], [41, 43, 47, 53]])
        self.assertEqual(det, 880)


class MatrixCofactorMatrix(unittest.TestCase):
    def test_1x1_cofactor_matrix(self):
        m = Matrix([[1]])

        cof_m = m.cofactor_matrix()

        self.assertEqual(m.get_matrix(), [[1]])
        self.assertEqual(cof_m.get_matrix(), [[1]])

    def test_2x2_cofactor_matrix(self):
        m = Matrix([[1, 2], [3, 4]])

        cof_m = m.cofactor_matrix()

        self.assertEqual(m.get_matrix(), [[1, 2], [3, 4]])
        self.assertEqual(cof_m.get_matrix(), [[4, -3], [-2, 1]])

    def test_3x3_cofactor_matrix(self):
        m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        cof_m = m.cofactor_matrix()

        self.assertEqual(m.get_matrix(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(cof_m.get_matrix(), [[-3, 6, -3], [6, -12, 6], [-3, 6, -3]])


class MatrixTranspose(unittest.TestCase):
    def test_1x1_transpose(self):
        m = Matrix([[1]])

        t_m = m.transpose()

        self.assertEqual(m.get_matrix(), [[1]])
        self.assertEqual(t_m.get_matrix(), [[1]])

    def test_2x2_transpose(self):
        m = Matrix([[1, 2], [3, 4]])

        t_m = m.transpose()

        self.assertEqual(m.get_matrix(), [[1, 2], [3, 4]])
        self.assertEqual(t_m.get_matrix(), [[1, 3], [2, 4]])

    def test_3x3_transpose(self):
        m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        t_m = m.transpose()

        self.assertEqual(m.get_matrix(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(t_m.get_matrix(), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])


class MatrixTransformations(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_non_sqaure_inverse(self):
        m = Matrix([[1, 2, 3], [4, 5, 6]])

        with self.assertRaises(MatrixArithmeticError):
            m.inverse()

    def test_matrix_with_no_inverse(self):
        m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        inv_m = m.inverse()

        self.assertIsNone(inv_m)


    def test_inverse(self):
        m = Matrix([[1, 2], [3, 4]])

        inv_m = m.inverse()

        self.assertEqual(m.get_matrix(), [[1, 2], [3, 4]])
        self.assertEqual(inv_m.get_matrix(), [[-2, 1], [1.5, -0.5]])
