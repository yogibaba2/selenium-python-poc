def send_email(callback_func):
    return callback_func("test@example.com", "Hello")
    

def test_spy_with_stub(mocker):
    # Create a stub function
    stub = mocker.stub(name="send_email_stub")
    
    # Spy on the stub function
    spy = mocker.spy(send_email, "__call__")

    # Call the stub function
    response = send_email(stub)
    stub.assert_called_once_with("test@example.com", "Hello")  # Ensures it was called correctly
