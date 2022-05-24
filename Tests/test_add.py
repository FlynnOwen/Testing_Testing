import pytest
from src.add import add


# We can mark a set of values to test - and whether any of them should fail
@pytest.mark.parametrize(
	"test_input, expected",
	[((2,3), 5), ((3,5), 8), pytest.param((100,100), 20, marks=pytest.mark.xfail)]
)
def test_add(test_input, expected):
	assert add(*test_input) == expected
