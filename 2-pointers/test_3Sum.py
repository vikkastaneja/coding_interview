import pytest
from ThreeSum import threeSum

testdata = [([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0,0,0], [[0,0,0]]),
            ([1,2,-2,-1], []),
            ([-4,-2,-2,-2,0,1,2,2,2,2,2,3], [[-4, 1, 3], [-4, 2, 2], [-2, 0, 2]]),
            ([], [])]

@pytest.mark.parametrize("nums, expected", testdata)
def test_threeSum(nums, expected):
    assert threeSum(nums) == expected
