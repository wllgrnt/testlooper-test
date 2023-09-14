import pytest 

@pytest.mark.group_two
def test_b():
    assert 2 == 2

@pytest.mark.group_one
def test_a():
    assert 1 == 1
