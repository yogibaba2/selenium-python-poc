def test_class_method_spy(mocker):
    class Calculator:
        def add(self, a, b):
            return a + b
    
    calc = Calculator()
    spy = mocker.spy(calc, "add")

    result = calc.add(3, 4)
    
    assert result == 7
    assert spy.call_count == 1
    spy.assert_called_with(3, 4)
