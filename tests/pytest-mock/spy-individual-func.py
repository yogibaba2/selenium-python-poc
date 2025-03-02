def multiply(x, y):
    return x * y

def test_function_spy(mocker):
        print(__name__)
        spy = mocker.spy(multiply, "__call__")

        assert multiply(2, 5) == 10
        assert spy.call_count == 1
        spy.assert_called_once_with(2, 5)
