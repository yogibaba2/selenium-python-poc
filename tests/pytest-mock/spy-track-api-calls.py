import requests

class APIClient:
    def get_data(self, url):
        return f"Function called with {url}"

def test_api_client(mocker):
    client = APIClient()
    spy = mocker.spy(client, "get_data")
    client.get_data("https://api.example.com/data")
    spy.assert_called_once_with("https://api.example.com/data")
