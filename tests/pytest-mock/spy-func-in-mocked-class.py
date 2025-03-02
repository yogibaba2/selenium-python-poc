def test_instance_method_spy(mocker):
    class Messenger:
        def send_message(self, message):
            return f"Sent: {message}"
    
    instance = Messenger()
    spy = mocker.spy(instance, "send_message")

    assert instance.send_message("Hello!") == "Sent: Hello!"
    assert spy.call_count == 1
    spy.assert_called_once_with("Hello!")
