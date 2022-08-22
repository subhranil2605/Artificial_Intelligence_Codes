import pytest
from genetic_algorithm import *


def test_mutate():
    assert mutate('01010', 1) == '00010'
    assert mutate('01010', 0) == '11010'
    assert mutate('01010', 2) == '01110'



if __name__ == '__main__':
    pytest.main()
