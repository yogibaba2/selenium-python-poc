import logging
def log_message():
    logging.info("Test log message.")
def test_spy_with_unspy(mocker):
    # Spy on logging.info
    spy = mocker.spy(logging, "info")
    log_message()  # Call the function
    spy.assert_called_once_with("Test log message.")  # Verify the spy tracked it

    # Unspy the function
    mocker.stop(spy)

    log_message()  # Call the function again

    assert spy.call_count == 1  # Ensures the second call is NOT tracked
