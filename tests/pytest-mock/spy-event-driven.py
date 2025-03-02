class TaskProcessor:
    def process(self, task):
        if task == "fail":
            self.handle_error("Task failed")

    def handle_error(self, message):
        print(f"Error: {message}")

def test_retry_mechanism(mocker):
    processor = TaskProcessor()
    spy = mocker.spy(processor, "handle_error")

    processor.process("fail")

    spy.assert_called_once_with("Task failed")
