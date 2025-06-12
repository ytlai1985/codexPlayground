from utils import ptt_crawler

class MockResponse:
    def __init__(self, text):
        self.text = text
    def raise_for_status(self):
        pass

def test_fetch_board_titles(monkeypatch):
    html = """
    <div class='title'>Title 1</div>
    <div class='title'>Title 2</div>
    """
    def mock_get(url, headers=None):
        return MockResponse(html)
    monkeypatch.setattr(ptt_crawler.requests, 'get', mock_get)
    titles = ptt_crawler.fetch_board_titles('dummy')
    assert titles == ['Title 1', 'Title 2']
