import requests

class APIClient:
    def get_data(self, url):
        return requests.get(url).json()

def test_spy_with_patch(mocker):
    client = APIClient()
    
    # Patch the method to return a controlled response
    mocker.patch.object(client, "get_data", return_value={"data": "mocked response"})

    # Spy on the method
    spy = mocker.spy(client, "get_data")
    
    result = client.get_data("https://api.example.com/data")

    assert result == {"data": "mocked response"}  # Ensures the function returns the patched response
    spy.assert_called_once_with("https://api.example.com/data")  # Ensures the function was called
