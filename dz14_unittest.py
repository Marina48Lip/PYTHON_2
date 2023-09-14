import unittest

def Triangle(a, b, c):
    if a + b < c or a + c < b or c + b < a:
        return "Такого треугольника не существует"
    elif a == b == c:
        return 'Треугольник равносторонний'
    elif a != b != c:
        return 'Треугольник разносторонний'
    else:
        return 'Треугольник равнобедренный'

class TriangleTest(unittest.TestCase):
     
    def test_equilateral(self):
        self.assertEqual(Triangle(2,3,4), 'Треугольник разносторонний')
        
        
    def test_isosceles (self):
        self.assertEqual(Triangle(2,3,3), 'Треугольник равнобедренный')


if __name__ == "__main__":
    unittest.main(verbosity=0)