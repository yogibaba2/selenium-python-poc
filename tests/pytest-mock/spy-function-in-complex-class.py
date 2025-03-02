class Database:
    def fetch_data(self, query):
        return f"Data for {query}"

def test_database_fetch(mocker):
    db = Database()
    spy = mocker.spy(db, "fetch_data")

    db.fetch_data("SELECT * FROM users")
    
    spy.assert_called_once_with("SELECT * FROM users")
    assert spy.call_count == 1
