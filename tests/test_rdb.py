from utils import rdb

class DummyCursor:
    def __init__(self):
        self.queries = []
        self.closed = False
    def execute(self, query, params=None):
        self.queries.append((query, params))
    def close(self):
        self.closed = True

class DummyConnection:
    def __init__(self):
        self.cursor_obj = DummyCursor()
        self.committed = False
        self.closed = False
    def cursor(self):
        return self.cursor_obj
    def commit(self):
        self.committed = True
    def close(self):
        self.closed = True


def test_insert_message(monkeypatch):
    conn = DummyConnection()
    def mock_connect(**kwargs):
        return conn
    monkeypatch.setattr(rdb.mariadb, 'connect', mock_connect)
    rdb.insert_message('hello')
    assert conn.committed is True
    assert conn.closed is True
    assert conn.cursor_obj.closed is True
    assert conn.cursor_obj.queries[1] == ("INSERT INTO messages (message) VALUES (?)", ('hello',))

