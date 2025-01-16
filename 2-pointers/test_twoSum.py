from TwoSum import twoSum
import pytest

testdata = [
    ([2, 7, 11, 15], 9, (0, 1)),
    ([2, 7, 11, 15], 17, (0, 3)),
    ([], 0, None),
    ([2, 7, 11, 15], 27, None)
]

@pytest.mark.parametrize("arr, target, expected", testdata)
def test_twoSum(arr, target, expected):
    assert twoSum(arr, target) == expected
