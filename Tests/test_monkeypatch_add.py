import pytest

from src import add


def test_add_monkeypatch(monkeypatch):
    def mockreturn(x, y):
        return 10

    # From module add, we wish to patch function "add" with the result from mockreturn
    monkeypatch.setattr(add, "add", mockreturn)

    result = add.add(1,3)
    assert result == 10