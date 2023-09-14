import pytest
import testlooper_test.core


@pytest.mark.group_one
def test_core_function_one():
    result = testlooper_test.core.main()
    assert result == "Hello World!", "The result did not match the expected output"


@pytest.mark.group_two
def test_core_function_two():
    with pytest.raises(AssertionError):
        result = testlooper_test.core.main()
        assert (
            result == "Goodbye World!"
        ), "The result did not match the expected output"


@pytest.mark.group_one
def test_core_function_three():
    result = testlooper_test.core.alternate()
    assert result == "Greetings", "The result did not match the expected output"

@pytest.mark.group_one
def test_core_function_four():
    assert 3 == 3
