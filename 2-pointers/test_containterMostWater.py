from container_with_most_water import max_area
import pytest

testdata = [([1,8,6,2,5,4,8,3,7], 49),
            ([1,1], 1),
            ([4,3,2,1,4], 16),
            ([1,2,1], 2),
            ([3,4,1,2,2,4,1,3,2], 21),
            ([] , 0)]

@pytest.mark.parametrize("heights, expected", testdata)
def test_max_area(heights, expected):
    assert max_area(heights) == expected