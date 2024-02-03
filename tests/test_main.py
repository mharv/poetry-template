import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from utils.functions import alter, get_n_numbers, multiply_array


def test_alter():
    i = 1
    assert type(alter(i)) == int
    o = alter(i)
    assert o == 2
    assert type(alter(0)) == int


def test_get_n_numbers():
    i = 5
    assert get_n_numbers(i) == [1, 2, 3, 4, 5]
    assert type(get_n_numbers(i)) == list
    assert len(get_n_numbers(i)) == i


def test_multiply_array():
    i1 = [1, 2, 3]
    i2 = 2
    assert multiply_array(i1, i2) == [2, 4, 6]
