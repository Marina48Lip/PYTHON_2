import pytest

def Triangle(a, b, c):
    if a + b < c or a + c < b or c + b < a:
        return "Такого треугольника не существует"
    elif a == b == c:
        return 'Треугольник равносторонний'
    elif a != b != c:
        return 'Треугольник разносторонний'
    else:
        return 'Треугольник равнобедренный'

@pytest.fixture
def triangle():
    return Triangle(2,3,4)

def test_equilateral(triangle):
    assert triangle == 'Треугольник разносторонний'
    
    
def test_isosceles():
    assert Triangle(2,3,3) == 'Треугольник равнобедренный'


if __name__ == "__main__":
    pytest.main(['-v'])

