from urllib.parse import urljoin

from requests import Session

class RestSession(Session):
    def __init__(self, prefix_url=None, *args, **kwargs):
        super(RestSession, self).__init__(*args, **kwargs)
        self.prefix_url = prefix_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.prefix_url, url)
        return super(RestSession, self).request(method, url, *args, **kwargs)