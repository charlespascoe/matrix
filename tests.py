from matrix import Matrix
import unittest

class MatrixArithmetic(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([[1, 2, 3], [4, 5, 6]])

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

    def test_invalid_maxtrix_size_multiplication(self):
        m2 = Matrix([[7, 8], [9, 10]])

        with self.assertRaises(Exception):
            self.m * m2

    def test_matrix_addition(self):
        m2 = Matrix([[7, 8, 9], [10, 11, 12]])

        result = self.m + m2

        self.assertEqual(result.get_matrix(), [[8, 10, 12], [14, 16, 18]])
        self.assertEqual(self.m.get_matrix(), [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(m2.get_matrix(), [[7, 8, 9], [10, 11, 12]])

    def test_invalid_matrix_size_addition(self):
        m2 = Matrix([[7, 8], [9, 10], [11, 12]])

        with self.assertRaises(Exception):
            self.m + m2

    def test_modulo(self):
        result = self.m % 3

        self.assertEqual(result.get_matrix(), [[1, 2, 0], [1, 2, 0]])
        self.assertEqual(self.m.get_matrix(), [[1, 2, 3], [4, 5, 6]])

    def test_pow_2(self):
        m = Matrix([[1, 2], [3, 4]])
        result = m**2

        self.assertEqual(m.get_matrix(), [[1, 2], [3, 4]])
        self.assertEqual(result.get_matrix(), [[7, 10], [15, 22]])

    def test_pow_5(self):
        m = Matrix([[1, 2], [3, 4]])
        result = m**5

        self.assertEqual(m.get_matrix(), [[1, 2], [3, 4]])
        self.assertEqual(result.get_matrix(), [[1069, 1558], [2337, 3406]])


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



