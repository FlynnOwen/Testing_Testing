import pytest
from src.add import add

print('success')
def test_add():
	assert 5 == add(2,3)
