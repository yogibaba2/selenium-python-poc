import logging
def log_message():
    logging.info("This is a test log.")
def test_log_spy(mocker):
    spy = mocker.spy(logging, "info")
    log_message()
    spy.assert_called_once_with("This is a test log.")
