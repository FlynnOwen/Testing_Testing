import pytest
from src.add import add

def test_add():
	assert 5 == add(2,3)
