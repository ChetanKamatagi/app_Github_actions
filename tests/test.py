from src.math_operation import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(10,20) == 30

def test_sub():
    assert sub(20,10) == 10
    assert sub(6,3) == 3
    